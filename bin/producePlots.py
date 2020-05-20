#!/usr/bin/env python
import subprocess, glob, optparse, json, ast, os, sys, collections
from tools import producePlots, Process
from pprint import pprint
import ntpath
import importlib
import yaml

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
    parser.add_option('-l', '--latex_table', dest='latex_table', default=False, action='store_true')
    parser.add_option('--no_plots', dest='no_plots', default=False, action='store_true')
    parser.add_option('--nev', dest='nevents', type=int, default='-1')

    parser.add_option('--sel', dest='sh', type=str, default='')

    # ex: --lsf 10 will send 1 job for 10 heppy chunks
    parser.add_option('--lsf', dest='lsf', default=False, action='store_true')
    parser.add_option('-q', '--queue', dest='queue', type=str, default='1nh')
    parser.add_option('--chunks', dest='chunks', type=int, default=1)

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
    treePath = '/heppy.FCChhAnalyses.{}.TreeProducer.TreeProducer_1/tree.root'.format(analysisName)

    #multi-threading
    MT = ops.MT

    #lsf
    lsf = ops.lsf
    chunks = ops.chunks
    queue = ops.queue
    
    sh = ops.sh
    
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
    
    # prepare analysis dir
    os.system('mkdir -p {}'.format(analysisDir))


    block = collections.OrderedDict()
    formBlock(processes, procDict, param.signal_groups,param.background_groups,sh, treeDir, treePath, block, ops.nevents)

    print sh

    ### run analysis
    producePlots(param.selections[sh], 
                 block, 
                 param.colors, 
                 param.variables, 
                 param.variables2D, 
                 param.uncertainties, 
                 sh, 
                 param.intLumi, 
                 param.delphesVersion, 
                 param.runFull,
                 analysisDir,
                 MT,
                 latex_table=ops.latex_table,
                 no_plots=ops.no_plots,
                 nevents=ops.nevents
                 )
#______________________________________________________________________________
def formBlock(processes, procdict, sb, bb, shyp, treedir, treepath, block, nevents):
    
    for label, procs in sb.iteritems():
       if label == shyp:
           block[shyp] = fillBlock(procs, processes, procdict, treedir, treepath, nevents)
    for label, procs in bb.iteritems():
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
             if procstr == pname:
                 xsec = procdict[pname]['crossSection']
                 nev = procdict[pname]['numberOfEvents']
                 if nevents>0: nev=nevents
                 sumw = procdict[pname]['sumOfWeights']
                 eff = procdict[pname]['matchingEfficiency']
                 kf = procdict[pname]['kfactor']
                 matched_xsec = xsec*eff
                 tree = '{}/{}/{}'.format(os.path.abspath(treedir), pname, treepath)
                 
                 #read from heppy yaml file job efficiency       
                 filestr = os.path.abspath(treedir) + '/' + pname + '/processing.yaml'
                 corrFac = 1.

                 if not file_exist(filestr):
                     blocklist.append(Process(pname,tree,nev,sumw,xsec,eff,kf))
                     continue

                 with open(filestr, 'r') as stream:
                     try:
                        dico = yaml.load(stream)
                        try:
                            dico['processing']
                            corrFac *= float(dico['processing']['nfiles'])/dico['processing']['ngoodfiles']
                        except TypeError, e:
                            print 'I got a  TypeError - reason "%s"' % str(e)
                     except yaml.YAMLError as exc:
                        print(exc)                 
                 sumw *= corrFac
                 nev *= corrFac    
                 blocklist.append(Process(pname,tree,nev,sumw,xsec,eff,kf))
     return blocklist

#__________________________________________________________
def file_exist(myfile):
    import os.path
    if os.path.isfile(myfile): return True
    else: return False
#______________________________________________________________________________
def split_comma_args(args):
    new_args = []
    for arg in args:
        new_args.extend( arg.split(',') )
    return new_args

#______________________________________________________________________________
if __name__ == '__main__': 
    main()
