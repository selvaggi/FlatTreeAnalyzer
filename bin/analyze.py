#!/usr/bin/env python
import subprocess, glob, optparse, json, ast, os, sys, collections, warnings, ROOT
from tools import producePlots, Process, formatted
from pprint import pprint
import ntpath
import importlib
import yaml
import commands
import time

#__________________________________________________________
def file_exist(myfile):
    import os.path
    if os.path.isfile(myfile): return True
    else: return False

#_____________________________________________________________________________
def options():
    parser = optparse.OptionParser(description="analysis parser")
    parser.add_option('-n', '--analysis_name', dest='analysis_name', type=str, default='')
    parser.add_option('-c', '--heppy_cfg', dest='heppy_cfg', type=str, default='')
    parser.add_option('-j', '--proc_file_json', dest='proc_file_json', type=str, default='/afs/cern.ch/work/h/helsens/public/FCCDicts/procDict.json')
    parser.add_option('-t', '--heppy_tree_dir', dest='heppy_tree_dir', type=str, default='')
    parser.add_option('-o', '--analysis_output', dest='analysis_output', type=str, default='')
    parser.add_option('-p', '--param_file', dest='param_file', type=str, default='')
    parser.add_option('-m', '--multi_threading', dest='MT', default=False, action='store_true')
    parser.add_option('--table', dest='table', default=False, action='store_true')
    parser.add_option('--latex_table', dest='latex_table', default=False, action='store_true')
    parser.add_option('--plots', dest='plots', default=False, action='store_true')
    parser.add_option('--nev', dest='nevents', type=int, default='-1')
    parser.add_option('--force', dest='force', default=False, action='store_true')

    parser.add_option('--lsf', dest='lsf', default=False, action='store_true')
    parser.add_option('--condor', dest='condor', default=False, action='store_true')
    parser.add_option('--collect', dest='collect', default=False, action='store_true')
    parser.add_option('-q', '--queue', help='run time (espresso, microcentury, longlunch, workday, tomorrow, testmatch, nextweek)',  dest='queue', type=str, default='1nh')
    parser.add_option('--clean', dest='clean', default=False, action='store_true')
    parser.add_option('-y', '--dry-run', action='store_true', dest='DRYRUN', default=False, help='perform a dry run (no jobs are lauched).')

    # run on single selection
    parser.add_option('--sel', dest='sel', type=str, default='')

    return parser.parse_args()

#______________________________________________________________________________
def main():

    ops, args = options()

    args = split_comma_args(args)

    # give this analysis a name
    analysisName = ops.analysis_name

    # heppy analysis configuration
    heppyCfg = ops.heppy_cfg

    # process dictionary
    processDict = ops.proc_file_json

    # heppy trees location directory
    treeDir = ops.heppy_tree_dir

    # analysis dir
    analysisDir = ops.analysis_output

    # param file
    paramFile = ops.param_file

    module_path = os.path.abspath(paramFile)
    module_dir = os.path.dirname(module_path)
    base_name = os.path.splitext(ntpath.basename(paramFile))[0]
   
    sys.path.insert(0, module_dir)
    param = importlib.import_module(base_name)
    
    # tree location
    #treePath = '/heppy.FCChhAnalyses.{}.TreeProducer.TreeProducer_1/tree.root'.format(analysisName)
    
    if 'FCChhAnalyses/HELHC' in heppyCfg:
        collider = 'HELHC'
        treePath = '/heppy.FCChhAnalyses.{}.{}.TreeProducer.TreeProducer_1/tree.root'.format(collider,analysisName)

    elif 'FCChhAnalyses/FCChh' in heppyCfg:
        collider = 'FCChh'
        treePath = '/heppy.FCChhAnalyses.{}.{}.TreeProducer.TreeProducer_1/tree.root'.format(collider, analysisName)
        #treePath = '/heppy.FCChhAnalyses.{}.TreeProducer.TreeProducer_1/tree.root'.format(analysisName)
        treePath = '/FCChhAnalyses.FCChh.{}.TreeProducer.TreeProducer_1/tree.root'.format(analysisName)

    else:
        sys.exit('did not find collider name... quit.')
    
    #treePath = '/heppy.FCChhAnalyses.{}.{}.TreeProducer.TreeProducer_1/tree.root'.format(collider,analysisName)
    #print treePath

    #multi-threading
    MT = ops.MT

    #lsf
    lsf = ops.lsf
    queue = ops.queue

    #condor
    condor = ops.condor
    queue = ops.queue

    # selection
    sel = ops.sel

    # check if output dir exists already
    if ops.force and not ops.clean:
        print( 'removing {}'.format(analysisDir))
        processCmd('rm -rf {}'.format(analysisDir))
        os.makedirs(analysisDir)

    elif os.path.exists(analysisDir) and not ops.clean and not ops.sel and not ops.table and not ops.latex_table and not ops.plots and not ops.collect:
        print ('')
        sys.exit('Output dir: "'+analysisDir+'" exists. To overwrite existing dir run with --force option')

    # retrieve list of processes from heppy cfg
    processes = []
    with open(heppyCfg) as f:
        lines = f.readlines()
        for l in lines:
            if 'splitFactor' in l:
                processes.append(l.rsplit('.', 1)[0])

    #processes = [c.name for c in heppyCfg.selectedComponents]

    with open(processDict) as f:
        procDict = json.load(f)

    # run on single signal hypothesis, also used in lsf btach submission
    if sel:
        block = collections.OrderedDict()
        formBlock(processes, procDict, param.signal_groups,param.background_groups, sel, treeDir, treePath, block, ops.nevents)
        producePlots(param, block, sel, ops)

    elif lsf:
        runLSF(processes, procDict, param, treeDir, treePath, analysisDir, ops)

    elif condor:
        runCondor(processes, procDict, param, treeDir, treePath, analysisDir, ops)

    else:
        if MT:
            runMT(processes, procDict, param, treeDir, treePath, analysisDir, MT, ops)
        else:
            for sh in param.selections.keys():

                block = collections.OrderedDict()

                formBlock(processes, procDict, param.signal_groups,param.background_groups,sh, treeDir, treePath, block, ops.nevents)

            ### run analysis
                producePlots(param, block, sh, ops)


import multiprocessing as mp
#_____________________________________________________________________________________________________
def runMT(processes, procDict, param, treeDir, treePath, analysisDir, MT, ops):
    threads = []
    for sh in param.selections.keys():

        block = collections.OrderedDict()
        formBlock(processes, procDict, param.signal_groups,param.background_groups,sh, treeDir, treePath, block, ops.nevents)
        thread = mp.Process(target=runMT_join,args=(block, param, sh,analysisDir, MT, ops ))
        thread.start()
        threads.append(thread)
    for proc in threads:
        proc.join()

#_____________________________________________________________________________________________________
def runMT_join(block, param, sh, analysisDir, MT, ops):
    print( "START %s" % (sh))
    producePlots(param, block, sh, ops)    
    print( "END %s" % (sh))

#_____________________________________________________________________________________________________
def runCondor(processes, procDict, param, treeDir, treePath, analysisDir, ops):

    # clean if asked for it
    if ops.clean:
        print( 'Cleaning LSF for {} jobs...'.format(ops.analysis_output))
        processCmd('rm -rf BatchOutput/{} LSF*'.format(ops.analysis_output))
        sys.exit('cleaned up everything.')

    # first thing is to check whether previous submission (if any) succeeded
    selection_list_4sub = []
    nbad = 0
    for sh in param.selections.keys():
        selname = formatted(sh)
        outseldir = 'sel_'+selname
        name_batch_dir = 'BatchOutput/{}/{}'.format(ops.analysis_output, outseldir)
        rootfile = name_batch_dir + '/root_'+selname+'/histos.root'

        if not os.path.isfile(rootfile) or not isValidROOTfile(rootfile) or not getsize(rootfile):
            selection_list_4sub.append(sh)
            nbad += 1

    # keep submitting until nbad = 0
    if nbad > 0 and not ops.collect:

        print( ' ')
        print( ' =========  Submitting {} jobs on {} queue ========='.format(nbad, ops.queue))

        condor_filename = 'configs/condor_{}.sub'.format(ops.analysis_name)
        cmdfile="""# here goes your shell script
executable    = condorScript.sh

# here you specify where to put .log, .out and .err files
output                = configs/std/condor.$(ClusterId).$(ProcId).out
error                 = configs/std/condor.$(ClusterId).$(ProcId).err
log                   = configs/std/condor.$(ClusterId).log

+AccountingGroup = "group_u_CMST3.all"
+JobFlavour = "{}"\n
""".format(ops.queue)

        jobCount=0
        for sh in selection_list_4sub:

            block = collections.OrderedDict()
            formBlock(processes, procDict, param.signal_groups,param.background_groups,sh, treeDir, treePath, block, ops.nevents)
            selname = formatted(sh)
            outseldir = 'sel_'+selname
            cmd = 'arguments="DUMMYHOMEDIR DUMMYANALYSISNAME DUMMYHEPPYCFG DUMMYTREELOCATION DUMMYTEMPLATEFILE DUMMYJSONFILE DUMMYOUTSELDIR DUMMYOUTDIR DUMMYSEL DUMMYNEVTS"\n'

            print( outseldir)
            # replace relevant parts in script and dump into file
            cmd = cmd.replace('DUMMYHOMEDIR', os.getcwd())
            cmd = cmd.replace('DUMMYANALYSISNAME', ops.analysis_name)
            cmd = cmd.replace('DUMMYHEPPYCFG', os.path.abspath(ops.heppy_cfg))
            cmd = cmd.replace('DUMMYTREELOCATION', os.path.abspath(ops.heppy_tree_dir))
            cmd = cmd.replace('DUMMYTEMPLATEFILE', os.path.abspath(ops.param_file))
            cmd = cmd.replace('DUMMYJSONFILE', os.path.abspath(ops.proc_file_json))
            cmd = cmd.replace('DUMMYOUTSELDIR', outseldir)
            cmd = cmd.replace('DUMMYSEL', "'{}'".format(sh))
            cmd = cmd.replace('DUMMYNEVTS', str(ops.nevents))
            cmd = cmd.replace('DUMMYOUTDIR', ops.analysis_output)

            #print cmd
            cmdfile += cmd
            cmdfile += 'queue\n'

        with open(condor_filename, 'w') as dest_file:
            dest_file.write(cmdfile)

        print('-- launching --')
        submit_cmd = "condor_submit {}".format(condor_filename)
        print( condor_filename)

        if(ops.DRYRUN):
            print( 'Dry-run:')
            #os.system('cat {}'.format(condor_filename))
        else:
            os.system(submit_cmd)

    # no bad job is found, can thus collect output
    else:
        print( '================================================================')
        print( 'Submission was successful, now collecting output ...')
        print( '')

        # 1 root file per signal hypothesis, simply copy in properly name dir
        # and run producePlots with runFull = false
        for sh in param.selections.keys():
            selname = formatted(sh)
            outseldir = 'sel_'+selname
            name_batch_dir = 'BatchOutput/{}/{}'.format(ops.analysis_output, outseldir)
            root_dir = '{}/root_{}'.format(name_batch_dir,selname)
            cmd = 'cp -r {} {}'.format(root_dir,ops.analysis_output)

            local_root_dir = '{}/root_{}'.format(ops.analysis_output,selname)

            print( local_root_dir)

            # collecting files
            if not os.path.exists(local_root_dir):
                processCmd(cmd)

            # run analysis on histos
            block = collections.OrderedDict()
            formBlock(processes, procDict, param.signal_groups,param.background_groups,sh, treeDir, treePath, block, ops.nevents)
            producePlots(param, block, sh, ops)


#_____________________________________________________________________________________________________
def runLSF(processes, procDict, param, treeDir, treePath, analysisDir, ops):


    # clean if asked for it
    if ops.clean:
        print( 'Cleaning condor for {} jobs...'.format(ops.analysis_output))
        processCmd('rm -rf BatchOutput/{} LSF*'.format(ops.analysis_output))
        sys.exit('cleaned up everything.')

    # first thing is to check whether previous submission (if any) succeeded
    selection_list_4sub = []
    nbad = 0
    for sh in param.selections.keys():
        selname = formatted(sh)
        outseldir = 'sel_'+selname
        name_batch_dir = 'BatchOutput/{}/{}'.format(ops.analysis_output, outseldir)
        rootfile = name_batch_dir + '/root_'+selname+'/histos.root'
        
        if not os.path.isfile(rootfile) or not isValidROOTfile(rootfile) or not getsize(rootfile):
            selection_list_4sub.append(sh)
            nbad += 1

    # keep submitting until nbad = 0
    if nbad > 0:
        print( ' ')
        print( ' =========  Submitting {} jobs on {} queue ========='.format(nbad, ops.queue))

        jobCount=0
        for sh in selection_list_4sub:

            block = collections.OrderedDict()
            formBlock(processes, procDict, param.signal_groups,param.background_groups,sh, treeDir, treePath, block, ops.nevents)
            selname = formatted(sh)

            dummyscript="""
    unset LD_LIBRARY_PATH
    unset PYTHONHOME
    unset PYTHONPATH
    mkdir job
    cd job

    cp -r DUMMYHOMEDIR/init.sh .
    cp -r DUMMYHOMEDIR/bin .
    cp -r DUMMYHOMEDIR/templates .

    source ./init.sh

    python bin/analyze.py -n DUMMYANALYSISNAME -c DUMMYHEPPYCFG -t DUMMYTREELOCATION -p DUMMYTEMPLATEFILE -j DUMMYJSONFILE -o DUMMYOUTSELDIR --sel 'DUMMYSEL' -m --nev DUMMYNEVTS

    mkdir -p DUMMYHOMEDIR/BatchOutput/DUMMYOUTDIR/DUMMYOUTSELDIR
    cp -r DUMMYOUTSELDIR DUMMYHOMEDIR/BatchOutput/DUMMYOUTDIR
            """

            outseldir = 'sel_'+selname

            # replace relevant parts in script and dump into file
            dummyscript = dummyscript.replace('DUMMYHOMEDIR', os.getcwd())
            dummyscript = dummyscript.replace('DUMMYANALYSISNAME', ops.analysis_name)
            dummyscript = dummyscript.replace('DUMMYHEPPYCFG', os.path.abspath(ops.heppy_cfg))
            dummyscript = dummyscript.replace('DUMMYTREELOCATION', os.path.abspath(ops.heppy_tree_dir))
            dummyscript = dummyscript.replace('DUMMYTEMPLATEFILE', os.path.abspath(ops.param_file))
            dummyscript = dummyscript.replace('DUMMYJSONFILE', os.path.abspath(ops.proc_file_json))
            dummyscript = dummyscript.replace('DUMMYOUTSELDIR', outseldir)
            dummyscript = dummyscript.replace('DUMMYSEL', sh)
            dummyscript = dummyscript.replace('DUMMYNEVTS', str(ops.nevents))
            dummyscript = dummyscript.replace('DUMMYOUTDIR', ops.analysis_output)
            script = dummyscript

            name_batch_dir = 'BatchOutput/{}/{}'.format(ops.analysis_output, outseldir)
            if not os.path.exists(name_batch_dir):
                os.makedirs(name_batch_dir)

            scriptdir = name_batch_dir+'/cfg/'
            if not os.path.exists(scriptdir):
                os.makedirs(scriptdir)

            with open('script.sh', "w") as f:
               f.write(script)
            processCmd('chmod u+x script.sh')
            processCmd('mv script.sh {}'.format(scriptdir))

            script = scriptdir+'script.sh'

            print ('Submitting job '+str(jobCount+1)+' out of '+str(len(selection_list_4sub)))

            cmd = 'bsub -o '+name_batch_dir+'/std/STDOUT -e '+name_batch_dir+'/std/STDERR -q '+ops.queue
            cmd +=' -J '+outseldir+' "'+os.path.abspath(script)+'" '

            # submitting jobs
            output = processCmd(cmd)
            while ('error' in output):
                time.sleep(1.0);
                output = processCmd(cmd)
                if ('error' not in output):
                    print( 'Submitted after retry - job '+str(jobCount+1))

            jobCount += 1

    # no bad job is found, can thus collect output
    else:
        print( '================================================================')
        print( 'Submission was successful, now collecting output ...')
        print( '')
            
        # 1 root file per signal hypothesis, simply copy in properly name dir
        # and run producePlots with runFull = false
        for sh in param.selections.keys():
            selname = formatted(sh)
            outseldir = 'sel_'+selname
            name_batch_dir = 'BatchOutput/{}/{}'.format(ops.analysis_output, outseldir)
            root_dir = '{}/root_{}'.format(name_batch_dir,selname)
            cmd = 'cp -r {} {}'.format(root_dir,ops.analysis_output)
            
            local_root_dir = '{}/root_{}'.format(ops.analysis_output,selname)
            
            print( local_root_dir)
            
            # collecting files
            if not os.path.exists(local_root_dir):
                processCmd(cmd)
            
            # run analysis on histos
            block = collections.OrderedDict()
            formBlock(processes, procDict, param.signal_groups,param.background_groups,sh, treeDir, treePath, block, ops.nevents)
            
            producePlots(param, block, sh, ops)

#______________________________________________________________________________
def formBlock(processes, procdict, sb, bb, shyp, treedir, treepath, block, nevents):
    
    for label, procs in sb.iteritems():
       print( label)
       if label == shyp:
           print( 'signal')
           block[shyp] = fillBlock(procs, processes, procdict, treedir, treepath, nevents)
    for label, procs in bb.iteritems():
       print( 'bkg')
       
       print( label, procs)
       block[label] = fillBlock(procs, processes, procdict, treedir, treepath, nevents)

#______________________________________________________________________________
def fillBlock(procs, processes, procdict, treedir, treepath, nevents):
     blocklist = []
     for procstr in procs:
         for pname in processes:
             # fix new call name format in FCChhAnalyses/.../analysis.py
             if pname.find("sample.")>=0 : pname=pname.replace("sample.","")
             # fix commented names in lists
             if pname.find("#")>=0 : continue

             #print 'Process: ', pname, procstr

             if procstr == pname:
                 xsec = procdict[pname]['crossSection']
                 
                 neventsDict = procdict[pname]['numberOfEvents']
                 
                 ## compute number of available events (maybe only a subset are available in heppy Tree) by checking into heppy yaml
                 neventsAvailable = float(neventsDict)
                 tree = '{}/{}/{}'.format(os.path.abspath(treedir), pname, treepath)
                 #read from heppy yaml file job efficiency       
                 filestr = os.path.abspath(treedir) + '/' + pname + '/processing.yaml'

                 corr = 1.
                 with open(filestr, 'r') as stream:
                     try:
                        dico = yaml.load(stream)
                        try:
                            dico['processing']
                            corr*= dico['processing']['ngoodfiles']/float(dico['processing']['nfiles'])
                            neventsAvailable*=corr
                        except TypeError:
                            print( 'I got a  TypeError - reason "%s"' % str(e))
                     except yaml.YAMLError as exc:
                        print(exc)                 

                 sumw = procdict[pname]['sumOfWeights']
                 eff = procdict[pname]['matchingEfficiency']
                 kf = procdict[pname]['kfactor']
                 matched_xsec = xsec*eff

                 ## extract number of events present in the tree (this is different from the number of available events processed by heppy because of selection criteria)
                 rf = ROOT.TFile(tree)
                 t = rf.Get("events")
                 numberOfEntries = t.GetEntries()

                 ## first apply overall correction factor due to to heppy inefficiencies
                 corrFacHeppy = corr
                 
                 ###### additional factor to be applied if requested number of events is smaller that actually contained in the trees
                 corrFacUser = 1
                 if nevents>0 and float(nevents)<= float(numberOfEntries):
                     corrFacUser=float(nevents)/float(numberOfEntries)

                 corrFac = corrFacHeppy*corrFacUser

                 print( '')
                 print( '==============================')
                 print( 'Process: ', pname)
                 print( 'Tree: ', tree)


                 print( 'Number of events in dict: ', neventsDict)
                 print( 'Heppy Job efficiency: ', corr)
                 print( 'Number of processed events: ', neventsAvailable)
                 print( 'Heppy condor correction factor: ', corr)
                 print( 'Number of requested events: ', nevents)
                 print( 'Number of events in the tree: ', numberOfEntries)
                 print( 'Sum of Weights: ', sumw)
                 print( 'Matching eff: ', eff)
                 print( 'K-factor: ', kf)
                 print( 'xsec (inclusive): ', xsec)
                 print( 'xsec (effective): ', xsec*eff*kf)
                 print( 'Heppy condor correction factor: ', corrFacHeppy)
                 print( 'Correction factor (if nev < nevents in tree): ', corrFacUser )
                 print( 'Total Correction factor : ',  corrFac)
                 print( '==============================')
                                      
                 sumw *= corrFac
                 
                 blocklist.append(Process(pname,tree,sumw,xsec,eff,kf))
     return blocklist

#______________________________________________________________________________
def split_comma_args(args):
    new_args = []
    for arg in args:
        new_args.extend( arg.split(',') )
    return new_args

#____________________________________________________________________________________________________________
### processing the external os commands
def processCmd(cmd, quite = 0):
    status, output = commands.getstatusoutput(cmd)
    if (status !=0 and not quite):
        print( 'Error in processing command:\n   ['+cmd+']')
        print( 'Output:\n   ['+output+'] \n')
    return output

#_____________________________________________________________
def isValidROOTfile(infile):
    valid = True
    with warnings.catch_warnings(record=True) as was:
        f=ROOT.TFile.Open(infile)
        ctrlstr = 'probably not closed'
        for w in was:
            if ctrlstr in str(w.message):
                valid = False
    return valid

#__________________________________________________________
def getsize(f):
    exist=os.path.isfile(f)
    if exist:
        size = os.path.getsize(f)
        return size
    return -1

#______________________________________________________________________________
if __name__ == '__main__': 
    main()
