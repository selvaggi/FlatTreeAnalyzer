'''
# absolute measurements
python scripts/higgs_analysis.py --objlist1 a1 a2 --indir1 haa --param1 templates/FCC/haa.py  --outdir plots/pt_haa
python scripts/higgs_analysis.py --objlist1 m1 m2 --indir1 hmumu --param1 templates/FCC/hmumu.py  --outdir plots/hmumu

python scripts/higgs_analysis.py --objlist1 m1 m2 a --indir1 hmumua --param1 templates/FCC/hmumua.py  --outdir plots/hmumua
python scripts/higgs_analysis.py --objlist1 e1 e2 a --indir1 heea --param1 templates/FCC/heea.py  --outdir plots/heea
python scripts/higgs_analysis.py  --indir1 hlla --param1 templates/FCC/hlla.py  --outdir plots/hlla

python scripts/higgs_analysis.py --objlist1 m1 m2 m3 m4 --indir1 h4mu --param1 templates/FCC/h4mu.py  --outdir plots/h4mu
python scripts/higgs_analysis.py --objlist1 e1 e2 m1 m2 --indir1 h2e2mu --param1 templates/FCC/h2e2mu.py  --outdir plots/h2e2mu
python scripts/higgs_analysis.py --objlist1 e1 e2 e3 e4 --indir1 h4e --param1 templates/FCC/h4e.py  --outdir plots/h4e
python scripts/higgs_analysis.py  --indir1 h4l --param1 templates/FCC/h4l.py  --outdir plots/h4l

# ratios
python scripts/higgs_analysis.py --objlist1 m1 m2 --indir1 hmumu --param1 templates/FCC/hmumu.py  --objlist2 m1 m2 m3 m4 --indir2 h4mu --param2 templates/FCC/h4mu.py --outdir plots/mumu_4mu
python scripts/higgs_analysis.py --objlist1 a1 a2 --indir1 haa --param1 templates/FCC/haa.py  --objlist2 e1 e2 m1 m2 --indir2 h2e2mu --param2 templates/FCC/h2e2mu.py --outdir plots/aa_2e2mu
python scripts/higgs_analysis.py --objlist1 a1 a2 --indir1 haa --param1 templates/FCC/haa.py  --objlist2 m1 m2 --indir2 hmumu --param2 templates/FCC/hmumu.py --outdir plots/aa_mumu
python scripts/higgs_analysis.py --objlist1 m1 m2 a --indir1 hmumua --param1 templates/FCC/hmumua.py  --objlist2 m1 m2 --indir2 hmumu --param2 templates/FCC/hmumu.py --outdir plots/mumua_mumu
'''

import ROOT, collections, os, sys
from ROOT import TFile, TTree, TTreeFormula, gROOT, TH1D, TH2D, kRed, TLegend, THStack, TVector2,  TGraph, TMultiGraph
import subprocess, glob, argparse, json, ast, os, sys, collections
import ntpath
import importlib
import yaml
import math
import warnings, re
from math import sqrt

warnings.filterwarnings(action="ignore", category=RuntimeWarning, message="creating converter.*")
warnings.filterwarnings(action="ignore", category=RuntimeWarning, message="Deleting canvas.*")
warnings.filterwarnings(action="ignore", category=RuntimeWarning, message="Replacing existing*")

colors = []
colors.append(ROOT.kRed);
colors.append(ROOT.kOrange-3);
colors.append(ROOT.kGreen+2);
colors.append(ROOT.kGreen+2);
colors.append(ROOT.kBlue-3);
colors.append(ROOT.kGreen+2);
colors.append(ROOT.kBlack);
colors.append(ROOT.kOrange-3);
colors.append(ROOT.kRed-9);
colors.append(ROOT.kYellow+2);
colors.append(ROOT.kMagenta+1);


ratio = dict()
ratio[25.00 ] = 1.695
ratio[50.000] = 1.741
ratio[75.000] = 1.777
ratio[100.00] = 1.812
ratio[125.00] = 1.846
ratio[150.00] = 1.879
ratio[175.00] = 1.912
ratio[200.00] = 1.945
ratio[225.00] = 1.976
ratio[250.00] = 2.009
ratio[275.00] = 2.040
ratio[300.00] = 2.072
ratio[325.00] = 2.102
ratio[350.00] = 2.132
ratio[375.00] = 2.161
ratio[400.00] = 2.190
ratio[425.00] = 2.218
ratio[450.00] = 2.246
ratio[475.00] = 2.273
ratio[500.00] = 2.300
ratio[525.00] = 2.326

#_____________________________________________________________________________
def options():

    parser = argparse.ArgumentParser()
    parser.add_argument("--objlist1", nargs='+', type=str)
    parser.add_argument('--indir1', dest='indir1', type=str, default='')
    parser.add_argument('--param1', dest='param1', type=str, default='')

    parser.add_argument("--objlist2", nargs='+', type=str)
    parser.add_argument('--indir2', dest='indir2', type=str, default='')
    parser.add_argument('--param2', dest='param2', type=str, default='')

    parser.add_argument('--outdir', dest='outdir', type=str, default='')
    parser.add_argument('--ptmax', dest='ptmax', type=float, default=500.)

    parser.add_argument('--sqrts', dest='sqrts', type=int, default=100)

    return parser.parse_args()

#______________________________________________________________________________
def main():

    args = options()

    '''uncertainties = []
    uncertainties.append((0., 0., 0.)) # stat only
    uncertainties.append((0., 1., 0.)) # signal eff + stat
    uncertainties.append((0.01, 1., 0.)) # lumi+prod + signal eff (x1) + stat'''

    uncertainties = collections.OrderedDict()
    uncertainties[(0.01, 1., 0.)] = 'stat. + syst. + lumi'
    uncertainties[(0., 1., 0.)] = 'stat. + syst.'
    uncertainties[(0., 0., 0.)] = 'stat. only'

    colstr = ''
    dirstr = ''

    if args.sqrts == 100:
        colstr = 'FCC'
        dirstr = 'fcc'

    if args.sqrts == 27:
        colstr = 'HELHC'
        dirstr = 'helhc'

    if args.sqrts == 37:
        colstr = 'HELHC'
        dirstr = 'helhc'

    # optional, do ratio only if arguments with label 2 are specified
    if len(args.param2) > 0:
        param1, rdir1, hfile1, processes1 = parameters(args.param1, args.indir1)
        electrons1, muons1, photons1 = objects(args.objlist1)
        dicts1 = produceDicts(param1, hfile1, electrons1, muons1, photons1)

        param2, rdir2, hfile2, processes2 = parameters(args.param2, args.indir2)
        electrons2, muons2, photons2 = objects(args.objlist2)
        dicts2 = produceDicts(param2, hfile2, electrons2, muons2, photons2)

        label1 = produceLabel(args.indir1)
        label2 = produceLabel(args.indir2)

        # do ratio plot here
        produceRatioPlot(param1, dicts1, label1, param2, dicts2, label2, args.outdir, args.ptmax)

    
    # combination 

    #elif args.indir1 == 'h4l':
    elif 'h4l' in args.indir1:
        
        param1, rdir1, hfile1, processes1 = parameters('templates/{}/h4mu.py'.format(colstr), 'h4mu_{}'.format(dirstr))
        param2, rdir2, hfile2, processes2 = parameters('templates/{}/h4e.py'.format(colstr), 'h4e_{}'.format(dirstr))
        param3, rdir3, hfile3, processes3 = parameters('templates/{}/h2e2mu.py'.format(colstr), 'h2e2mu_{}'.format(dirstr))

        electrons1, muons1, photons1 = objects(['m1','m2','m3','m4'])
        electrons2, muons2, photons2 = objects(['e1','e2','e3','e4'])
        electrons3, muons3, photons3 = objects(['e1','e2','m1','m2'])

        print 'doing 4mu'
        dicts1 = produceDicts(param1, hfile1, electrons1, muons1, photons1)
        print 'doing 4ele'
        dicts2 = produceDicts(param2, hfile2, electrons2, muons2, photons2)
        print 'doing 2e2mu'
        dicts3 = produceDicts(param3, hfile3, electrons3, muons3, photons3)

        label = produceLabel(args.indir1)

        param = []
        dicts = []

        param.append(param1)
        param.append(param2)
        param.append(param3)
        
        dicts.append(dicts1)
        dicts.append(dicts2)
        dicts.append(dicts3)

        produceYieldPlots(param, dicts, uncertainties, args.outdir, label, args.ptmax)
        
    #elif args.indir1 == 'hlla':
    elif 'hlla' in args.indir1:
       
        param1, rdir1, hfile1, processes1 = parameters('templates/{}/hmumua.py'.format(colstr), 'hmumua_{}'.format(dirstr))
        param2, rdir2, hfile2, processes2 = parameters('templates/{}/heea.py'.format(colstr), 'heea_{}'.format(dirstr))

        electrons1, muons1, photons1 = objects(['m1','m2','a'])
        electrons2, muons2, photons2 = objects(['e1','e2','a'])

        dicts1 = produceDicts(param1, hfile1, electrons1, muons1, photons1)
        dicts2 = produceDicts(param2, hfile2, electrons2, muons2, photons2)

        label = produceLabel(args.indir1)

        param = []
        dicts = []

        param.append(param1)
        param.append(param2)
        
        dicts.append(dicts1)
        dicts.append(dicts2)

        produceYieldPlots(param, dicts, uncertainties, args.outdir, label, args.ptmax)

    else : 

        param1, rdir1, hfile1, processes1 = parameters(args.param1, args.indir1)
        electrons1, muons1, photons1 = objects(args.objlist1)
        dicts1 = produceDicts(param1, hfile1, electrons1, muons1, photons1)

        print 'here'

        dicts = []
        dicts.append(dicts1)
 
        param = []
        param.append(param1)

        label = produceLabel(args.indir1)
        produceYieldPlots(param, dicts, uncertainties, args.outdir, label, args.ptmax)

#_____________________________________________________________________________________________________
def objects(objlist):
    electrons = [obj for obj in objlist if 'e' in obj]
    muons = [obj for obj in objlist if 'm' in obj]
    photons = [obj for obj in objlist if 'a' in obj]
    return electrons, muons, photons

#_____________________________________________________________________________________________________
def produceLabel(indir):
    label = ''
    '''
    if   indir == 'haa'      : label = 'H #rightarrow #gamma#gamma'
    elif indir == 'hmumu'    : label = 'H #rightarrow #mu#mu'
    elif indir == 'h4mu'     : label = 'H #rightarrow #mu#mu#mu#mu'   
    elif indir == 'h2e2mu'   : label = 'H #rightarrow ee#mu#mu'
    elif indir == 'h4e'      : label = 'H #rightarrow eeee'   
    elif indir == 'hmumua'   : label = 'H #rightarrow #mu#mu#gamma'   
    elif indir == 'heea'     : label = 'H #rightarrow ee#gamma'   
    elif indir == 'h4l'      : label = 'H #rightarrow 4l, l=e/#mu'   
    elif indir == 'hlla'     : label = 'H #rightarrow ll#gamma, l=e/#mu'
    '''
    if   'haa_'     in indir : label = 'H #rightarrow #gamma#gamma'
    elif 'hmumu_'   in indir : label = 'H #rightarrow #mu#mu'
    elif 'h4mu_'    in indir : label = 'H #rightarrow #mu#mu#mu#mu'
    elif 'h2e2mu_'  in indir : label = 'H #rightarrow ee#mu#mu'
    elif 'h4e_'     in indir : label = 'H #rightarrow eeee'
    elif 'hmumua_'  in indir : label = 'H #rightarrow #mu#mu#gamma'
    elif 'heea_'    in indir : label = 'H #rightarrow ee#gamma'
    elif 'h4l_'     in indir : label = 'H #rightarrow 4l, l=e/#mu'
    elif 'hlla_'    in indir : label = 'H #rightarrow ll#gamma, l=e/#mu'
    return label

#_____________________________________________________________________________________________________
def parameters(param, indir):

    paramFile = param
    module_path = os.path.abspath(paramFile)
    module_dir = os.path.dirname(module_path)
    base_name = os.path.splitext(ntpath.basename(paramFile))[0]
    sys.path.insert(0, module_dir)
    print base_name
    param = importlib.import_module(base_name)
    rdir = "{}/root_H_125/".format(indir)
    hfile = ROOT.TFile("{}/histos.root".format(rdir))
    processes = param.colors.keys()
    return param, rdir, hfile, processes

#_____________________________________________________________________________________________________
def obj_err(objlist, hfile, selstr):

    # return 0 uncertainty if no object of this type is found
    delta_eff_obj = 0.
    for objstr in objlist:
        varpt = 'pt{}'.format(objstr)
        hname = 'H(125)_{}_{}'.format(selstr,varpt)
        h = hfile.Get(hname)
        mean = h.GetMean()

        # assume correlated errors for the same object, cannot add in quadrature
        delta_eff_obj +=  delta_eff(objstr, mean)
    return delta_eff_obj


#_____________________________________________________________________________________________________
def produceDicts(param, hfile, electrons, muons, photons):

    ele_errors = collections.OrderedDict()
    muo_errors = collections.OrderedDict()
    pho_errors = collections.OrderedDict()
    s_yields   = collections.OrderedDict()
    b_yields   = collections.OrderedDict()

    processes = param.colors.keys()

    if 'H(125)' not in processes:
       print 'ERROR: could not find signal'
    
    nsel = 0
    for sel_list in param.selections.values():
        for sel in sel_list:

            # any variable will do to compute yields
            v = param.variables.keys()[0]
            selstr = 'sel{}'.format(int(nsel))
            nsel += 1

            # only keep higgs pt selection
            if not sel in param.selections_pt:
                continue

            # extract cut value from string
            words = sel.split() 
            cut=float(words[words.index('higgs_pt')+2])

            # extract average pt values from histos and calculate relevant object uncertainty
            err_ele = obj_err(electrons, hfile, selstr)
            err_muo = obj_err(muons, hfile, selstr)
            err_pho = obj_err(photons, hfile, selstr)

            ele_errors[cut] = obj_err(electrons, hfile, selstr)
            muo_errors[cut] = obj_err(muons, hfile, selstr)
            pho_errors[cut] = obj_err(photons, hfile, selstr)

            #delta_eff_tot = math.sqrt(err_ele**2 + err_muo**2 + err_pho**2)
            #print cut, ele_errors[cut], muo_errors[cut], pho_errors[cut]

            b = 0
            eb = 0
            for p in processes:

                hname = '{}_{}_{}'.format(p,selstr,v)
                h = hfile.Get(hname)
                err = ROOT.Double()
                yld = h.IntegralAndError(0, h.GetNbinsX()+1, err)
                raw = h.GetEntries()

                yld *= param.intLumi
                err *= param.intLumi

                if 'H(125)' in p:
                    s = yld
                else: 
                    b += yld

            s_yields[cut] = s
            b_yields[cut] = b
    
    dicts = [ele_errors, muo_errors, pho_errors, s_yields, b_yields]
    return dicts



#_____________________________________________________________________________________________________
def produceYieldPlots(param, dicts, uncertainties, fname, label, ptmax):

    print ''
    print 'Preparing yield plots ...'

    # uncertainty scenarios (theory+lumi, signal_eff, background)
    # signal eff uncertainty is computed later based on object pT, here specifiy only multiplicative factor
    
    # prepare yield plots
    gr_sb = TGraph()
    mg_sign = TMultiGraph()
    mg_dmu = TMultiGraph()

    gr_sb.SetTitle(";p_{T,min}^{H} [GeV]; S/B")
    mg_sign.SetTitle(";p_{T,min}^{H} [GeV]; Significance = #frac{S}{#sqrt{S + #sigma_{S}^{2} + B + #sigma_{B}^{2}}}")
    mg_dmu.SetTitle(";p_{T,min}^{H} [GeV]; #delta #mu / #mu (%)")

    grs_sign = {}
    grs_dmu = {}

    index = 0
    gr_sb.SetLineColor(ROOT.kBlack)
    gr_sb.SetLineWidth(3)
    for unc, tit in uncertainties.iteritems():
        gr_sign = TGraph()
        gr_dmu = TGraph()
        gr_sign.SetLineColor(colors[index])
        gr_dmu.SetLineColor(colors[index])

        gr_sign.SetLineWidth(3)
        gr_dmu.SetLineWidth(3)
        gr_sign.SetMarkerSize(0.0001)
        gr_dmu.SetMarkerSize(0.0001)
        gr_sign.SetFillColor(0)
        gr_dmu.SetFillColor(0)

        grs_sign[index] = gr_sign
        grs_dmu[index] = gr_dmu

        title = tit

        grs_sign[index].SetTitle(title)
        grs_dmu[index].SetTitle(title)

        index += 1

    # fill yield graphs
    nsel = 0
    
    maxsb = -999
    minsb = 999
    maxsig = -999
    minsig = 999
    maxdmu = -999
    mindmu = 999

    nsel = 0
    
    minpt = dict()
    minss = dict()
    

    for unc, tit in uncertainties.iteritems():
        minpt[unc] = 999.
        minss[unc] = 999.

    for cut in dicts[0][0].keys():

        #print s, b
        nsel += 1
        index = 0
        
        delta_eff_ele = 0
        delta_eff_mu = 0
        delta_eff_pho = 0
        
        delta_eff_i = 0
        # loop over all final states
        
        deltas_s = 0
        deltas_s_2 = 0
        
        deltab_b = 0
        deltab_b_2 = 0
        
        s = 0
        b = 0
        
        for i in xrange(len(dicts)):

            ele_errors = dicts[i][0]
            muo_errors = dicts[i][1]
            pho_errors = dicts[i][2]
            s_yields = dicts[i][3] 
            b_yields = dicts[i][4]

            s_i = s_yields[cut]
            b_i = b_yields[cut]

            args = options()
            if args.sqrts == 37:
                s_i *= ratio[cut]
                b_i *= ratio[cut]

            #sigma_eff_i = unc[1]*delta_eff_i

            #sig_unc_i = math.sqrt(unc[0]**2 + sigma_eff_i**2)
            #bkg_unc_i = math.sqrt(unc[2]**2)

            sigma_eff_i = math.sqrt(ele_errors[cut]**2 + muo_errors[cut]**2 + pho_errors[cut]**2)

            sig_unc_i = math.sqrt(sigma_eff_i**2)
            bkg_unc_i = 0.

            s += s_i
            b += b_i

            deltas_s   += sig_unc_i*s_i
            deltas_s_2 += (sig_unc_i*s_i)**2
            
            #print '{:.0f}, {:.0f}, {:.3f}, {:.0f}'.format(s_i, b_i, sig_unc_i, sig_unc_i*s_i)
            
            deltab_b   += bkg_unc_i*b_i
            deltab_b_2 += (bkg_unc_i*b_i)**2

        if b == 0:
           gr_sb.SetPoint(nsel,cut,0.)
           if 0 < minsb : minsb = 0.
           if 0 > maxsb : maxsb = 0.
        else:
           if s/b < minsb : minsb = s/b
           if s/b > maxsb : maxsb = s/b
           gr_sb.SetPoint(nsel,cut,s/b)



        index = 0
        for unc, tit in uncertainties.iteritems():

            sig_unc = 1.0
            bkg_unc = 1.0

            s_2 = s*s
            b_2 = b*b


            # conservative case, correlated sum --> sigma_s * s = Sum sigma_i * s_i 
            if s > 0 and b > 0:
                sig_unc = deltas_s/s
                #bkg_unc = deltab_b/b
                bkg_unc = math.sqrt(deltab_b_2/b_2)

            
            '''# aggro case, un-correlated sum --> sigma_s * s = sqrt( Sum (sigma_i * s_i)^2
            if s > 0 and b > 0:
                sig_unc = math.sqrt(deltas_s_2/s_2)
                bkg_unc = math.sqrt(deltab_b_2/b_2)'''
            #print cut, s, b, unc, sig_unc


            # rescale by various uncertainty assumptions
            sig_unc = math.sqrt(unc[0]**2 + (unc[1]*sig_unc)**2)
            bkg_unc = math.sqrt(unc[2]**2)

            sign = significance(s, sig_unc, b, bkg_unc)
            rel_unc = dMuOverMu(s, sig_unc, b, bkg_unc)


            if float(cut) <= ptmax:
                if sign < minsig : minsig = sign 
                if sign > maxsig : maxsig = sign
                if rel_unc < mindmu : mindmu = rel_unc
                if rel_unc > maxdmu : maxdmu = rel_unc


            if rel_unc < minss[unc]:
                minss[unc] = rel_unc
                minpt[unc] = cut

            #print unc, cut, rel_unc

            grs_sign[index].SetPoint(nsel,cut,sign)
            grs_dmu[index].SetPoint(nsel,cut,rel_unc)

            index += 1

    index = 0
    for unc, tit in uncertainties.iteritems():
        mg_sign.Add(grs_sign[index])
        mg_dmu.Add(grs_dmu[index])
        index += 1

    intLumiab = param[0].intLumi/1e+06 

    args = options()
    if args.sqrts == 100:
        collabel = 'FCC-hh'
        sqrtslabel = args.sqrts
       
    if args.sqrts == 27:
        collabel = 'HE-LHC'
        sqrtslabel = args.sqrts

    if args.sqrts == 37:
        collabel = 'VHE-LHC'
        sqrtslabel = 37.5


    lt = "{} Simulation (Delphes)".format(collabel)
    rt = "#sqrt{{s}} = {} TeV, L = {:.0f}  ab^{{-1}}, {}".format(sqrtslabel, intLumiab, label)


    drawMultiGraph(mg_sign, 'sign', lt, rt, fname, minsig/2., maxsig*10., ptmax, True)
    #drawMultiGraph(mg_dmu, 'optim_dmu', lt, rt, fname , mindmu/2., maxdmu*4., ptmax, True)
    drawMultiGraph(mg_dmu, 'dmu', lt, rt, fname , mindmu/4., maxdmu*10., ptmax, True)
    drawMultiGraph(gr_sb, 'sb', lt, rt, fname, minsb/2., maxsb*2., ptmax, True,  False)


    # print summary
    for unc, tit in uncertainties.iteritems():
        print '{}: {:.2f}'.format(tit, minss[unc])


    print 'DONE'





#_____________________________________________________________________________________________________
def produceRatioPlot(param1, dicts1, label1, param2, dicts2, label2, fname, ptmax):

    print ''
    print 'Preparing ratio plots ...'

    # uncertainty scenarios (theory+lumi, signal_eff, background)
    # signal eff uncertainty is computed later based on object pT, here specifiy only multiplicative factor
    
    # prepare yield plots
    mg_dr = TMultiGraph()
    titley = "#delta ( BR({}) / BR({}) ) (%)".format(label1,label2)
    ratiolabel = '#frac{{BR({})}}{{BR({})}}'.format(label1,label2)
    mg_dr.SetTitle(";p_{T,min}^{H} [GeV];"+titley)

    grs_dr = {}

    # do 3 scenarios only: stat only, stat+ syst (agg), stat+ syst (cons) 
    uncertainties = []
    uncertainties.append((1., 2.)) # syst (cons) + stat
    uncertainties.append((1., 1.)) # syst (agg) + stat
    uncertainties.append((1., 0.)) # stat only

    uncs = collections.OrderedDict()
    uncs[(1., 2.)] = 'stat + syst (cons.)' # syst (cons) + stat
    uncs[(1., 1.)] = 'stat + syst (optim.)' # syst (agg) + stat
    uncs[(1., 0.)] = 'stat. only' # stat only

    index = 0
    for unc in uncertainties:
        gr_dr = TGraph()
        gr_dr.SetLineColor(colors[index])
        gr_dr.SetLineWidth(3)
        gr_dr.SetMarkerSize(0.0001)
        gr_dr.SetFillColor(0)

        grs_dr[index] = gr_dr
        index += 1

    # fill yield graphs
    nsel = 0
    
    maxdr = -999
    mindr = 999

    ele_errors1 = dicts1[0]
    muo_errors1 = dicts1[1]
    pho_errors1 = dicts1[2]
    s_yields1 = dicts1[3] 
    b_yields1 = dicts1[4]

    ele_errors2 = dicts2[0]
    muo_errors2 = dicts2[1]
    pho_errors2 = dicts2[2]
    s_yields2 = dicts2[3] 
    b_yields2 = dicts2[4]

    minpt = dict()
    minss = dict()

    for unc in uncertainties:
        minpt[unc] = 999.
        minss[unc] = 999.

    nsel = 0
    for cut in dicts1[0].keys():

        nsel += 1
        index = 0

        s1 = s_yields1[cut]
        b1 = b_yields1[cut]
        s2 = s_yields2[cut]
        b2 = b_yields2[cut]

        args = options()
        if args.sqrts == 37:
            s1 *= ratio[cut]
            b1 *= ratio[cut]
            s2 *= ratio[cut]
            b2 *= ratio[cut]

        de1 = ele_errors1[cut]
        de2 = ele_errors2[cut]
        dm1 = muo_errors1[cut]
        dm2 = muo_errors2[cut]
        da1 = pho_errors1[cut]
        da2 = pho_errors2[cut]

        # in ratio take difference of correlated uncertaintites, and quad. sum or uncorr. ones
        #delta_eff_tot = 100.*(math.sqrt((de1-de2)**2 + (da1-da2)**2 + (dm1-dm2)**2))
        delta_eff_tot = 100.*(math.sqrt((de1 + da1 - de2 - da2)**2 + (dm1-dm2)**2))

        # compute stat. uncertainties (TBC!!!)
        delta_stat1 = dMuOverMu(s1, 0., b1, 0.)
        delta_stat2 = dMuOverMu(s2, 0., b2, 0.)

        # add in quadrature efficiency and stat. uncertainty
        #toterr = math.sqrt(delta_eff_tot**2 + delta_stat1**2 + delta_stat2**2)
        #print cut, s1, b1, s2, b2

        for unc in uncertainties:
            
            if index == 2: 
               title = 'stat. only'
               
            if index == 1: 
               title = 'stat + syst (optim.)'
               
            if index == 0: 
               title = 'stat + syst (cons.)'

            toterr = math.sqrt((unc[1]*delta_eff_tot)**2 + delta_stat1**2 + delta_stat2**2)

            grs_dr[index].SetPoint(nsel,cut,toterr)

            if toterr < minss[unc]:
                minss[unc] = toterr
                minpt[unc] = cut

            if toterr < mindr : mindr = toterr
            if toterr > maxdr : maxdr = toterr

            grs_dr[index].SetTitle(title)
            index += 1

    index = 0
    for unc in uncertainties:
        mg_dr.Add(grs_dr[index])
        index += 1

    intLumiab = param1.intLumi/1e+06 

    #ratiolabel = ratiolabel.replace('#','\\')

    args = options()
    if args.sqrts == 100:
        collabel = 'FCC-hh'
        sqrtslabel = args.sqrts
       
    if args.sqrts == 27:
        collabel = 'HE-LHC'
        sqrtslabel = args.sqrts

    if args.sqrts == 37:
        collabel = 'VHE-LHC'
        sqrtslabel = 37.5

    lt = "{} Simulation (Delphes)".format(collabel)
    rt = "#sqrt{{s}} = {} TeV, L = {:.0f}  ab^{{-1}}".format(sqrtslabel,intLumiab)
    rt += ', {}'.format(ratiolabel)

    drawMultiGraph(mg_dr, 'ratio', lt, rt, fname , mindr/10., maxdr*10., ptmax, True)
    print 'DONE'

    # print summary
    for unc in uncertainties:
        print '{}: {:.2f}'.format(uncs[unc], minss[unc])


#_____________________________________________________________________________________________________
def drawMultiGraph(mg, title, lt, rt, fname, ymin, ymax, ptmax, log, bl = True):


    #myStyle()
    gROOT.SetBatch(True)
    canvas = ROOT.TCanvas('bla', 'bla', 600, 600) 
    canvas.SetLogy(log)
    canvas.SetTicks(1,1)
    canvas.SetLeftMargin(0.14)
    canvas.SetRightMargin(0.08)
    ROOT.gStyle.SetOptStat(0000000)    
    
    mg.Draw("AL")
    
    '''mg.GetYaxis().SetLabelFont(132)
    mg.GetYaxis().SetTitleFont(132)
    mg.GetYaxis().SetLabelOffset(0.02)
    mg.GetYaxis().CenterTitle()
    mg.GetYaxis().SetNdivisions(505)
    mg.GetXaxis().SetNdivisions(505)
    mg.GetYaxis().SetTitleOffset(1.8)

    mg.GetXaxis().SetTitleFont(132)
    mg.GetXaxis().SetLabelFont(132)
    mg.GetXaxis().SetLabelOffset(0.02)
    mg.GetXaxis().SetTitleOffset(1.5)
    mg.GetXaxis().SetTitleSize(0.06)
    mg.GetYaxis().SetTitleSize(0.048)
    mg.GetXaxis().SetLabelSize(0.06)
    mg.GetYaxis().SetLabelSize(0.06)'''

    mg.GetXaxis().SetTitleSize(0.035)
    mg.GetYaxis().SetTitleSize(0.035)
    
    mg.GetXaxis().SetRangeUser(50.,ptmax)

    mg.GetYaxis().SetTitleOffset(1.75)
    mg.GetXaxis().SetTitleOffset(1.35)


    mg.SetMinimum(ymin)
    mg.SetMaximum(ymax)
    
    if log: ROOT.gPad.SetLogy()

    if bl:
        leg = canvas.BuildLegend(0.55,0.70,0.88,0.88)
        leg.SetFillColor(0)
        leg.SetFillStyle(0)
        leg.SetLineColor(0)
        leg.Draw() 

    Text = ROOT.TLatex()
    
    Text.SetNDC() 
    Text.SetTextAlign(31);
    Text.SetTextSize(0.04) 

    text = '#it{' + lt +'}'
    
    Text.DrawLatex(0.90, 0.92, text) 

    rt = re.split(",", rt)
    text = '#bf{#it{' + rt[0] +'}}'
    
    Text.SetTextAlign(22);
    Text.SetNDC(ROOT.kTRUE) 
    Text.SetTextSize(0.04) 
    Text.DrawLatex(0.30, 0.83, text)
    
    Text.SetTextAlign(22);
    text = '#bf{#it{' + rt[1] +'}}'
    Text.SetTextSize(0.036) 
    Text.DrawLatex(0.30, 0.76, text)
    #Text.DrawLatex(0.18, 0.78, rt[1])

    if len(rt)>2:
        text = '#it{#bf{' + rt[2] +'}}'
        if 'ell' in text:
           text = text.replace('#','\\')
        Text.SetTextSize(0.05) 
        Text.DrawLatex(0.69, 0.27, text)

    if len(rt)>3:
        text = '#it{#bf{' + rt[3] +'}}'
        if 'ell' in text:
           text = text.replace('#','\\')
        Text.SetTextSize(0.04) 
        Text.DrawLatex(0.71, 0.20, text)

    canvas.RedrawAxis()
    canvas.Update()
    canvas.GetFrame().SetBorderSize( 12 )
    canvas.Modified()
    canvas.Update()
 
    pdir = os.path.dirname(fname)
    name = os.path.basename(fname)
    name = title + '_' + name
    
    filename = pdir + '/' + name
    
    if not os.path.exists(pdir):
       os.makedirs(pdir)
    canvas.Print('{}.pdf'.format(filename), 'pdf')
    canvas.Print('{}.png'.format(filename), 'png')
#____________________________________________________
def myStyle():
    import ROOT

    font = 132
    ROOT.gStyle.SetFrameBorderMode(0)
    ROOT.gStyle.SetCanvasBorderMode(0)
    ROOT.gStyle.SetPadBorderMode(0)

    ROOT.gStyle.SetFrameFillColor(0)
    ROOT.gStyle.SetFrameFillStyle(0)

    ROOT.gStyle.SetPadColor(0)
    ROOT.gStyle.SetCanvasColor(0)
    ROOT.gStyle.SetTitleColor(1)
    ROOT.gStyle.SetStatColor(0)

    ROOT.gStyle.SetLegendBorderSize(0)
    ROOT.gStyle.SetLegendFillColor(0)
    ROOT.gStyle.SetLegendFont(font)
    
    # set the paper & margin sizes
    '''ROOT.gPad.SetLeftMargin(0.22)
    ROOT.gPad.SetRightMargin(0.10)
    ROOT.gPad.SetBottomMargin(0.18)'''
    #ROOT.gPad.SetLogy()
    #ROOT.gPad.SetGridy()
    ROOT.gStyle.SetOptStat(0000000)
    ROOT.gStyle.SetTextFont(font)

    ROOT.gStyle.SetTextFont(font)
    ROOT.gStyle.SetTextSize(0.05)
    ROOT.gStyle.SetLabelFont(font,"XYZ")
    ROOT.gStyle.SetTitleFont(font,"XYZ")
    ROOT.gStyle.SetLabelSize(0.05,"XYZ") #0.035
    ROOT.gStyle.SetTitleSize(0.05,"XYZ")
    
    ROOT.gStyle.SetTitleOffset(1.25,"X")
    ROOT.gStyle.SetTitleOffset(1.95,"Y")
    ROOT.gStyle.SetLabelOffset(0.02,"XY")
    
    # use bold lines and markers
    ROOT.gStyle.SetMarkerStyle(8)
    ROOT.gStyle.SetHistLineWidth(3)
    ROOT.gStyle.SetLineWidth(1)

    ROOT.gStyle.SetNdivisions(505,"xy")

    # do not display any of the standard histogram decorations
    ROOT.gStyle.SetOptTitle(0)
    ROOT.gStyle.SetOptStat(0) #("m")
    ROOT.gStyle.SetOptFit(0)
    
    #ROOT.gStyle.SetPalette(1,0)
    ROOT.gStyle.cd()
    ROOT.gROOT.ForceStyle()

#_____________________________________________________________________________________________________
def delta_base(pt):
    return 0.01*0.25*math.sqrt(2500./pt**2 -5./pt + 1.)

#_____________________________________________________________________________________________________
def delta_eff(obj, pt):
    
    delta = delta_base(pt)
    
    if 'e' in obj or 'a' in obj:
        delta *=2.

    return delta

#_____________________________________________________________________________________________________
def significance(s, es, b, eb):
    if s == 0 and b == 0:
        return 0.
    else:
        return s/sqrt(s + (s*es)**2 + b + (b*eb)**2)

#_____________________________________________________________________________________________________
def dMuOverMu(s, es, b, eb):
    if s == 0:
        return 1000.
    else:
        return 100*sqrt(s + (s*es)**2 + b + (b*eb)**2)/s

#_____________________________________________________________________________
if __name__ == '__main__':
    main()
