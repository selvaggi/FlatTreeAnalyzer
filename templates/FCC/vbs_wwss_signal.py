import ROOT
import collections

variables = {
    "ptl1":{"name":"lpt1_pt","title":"p_{T}^{max}(#ell) [GeV]","bin":50,"xmin":20.0,"xmax":400.0},
    "ptl2":{"name":"lpt2_pt","title":"p_{T}^{min}(#ell) [GeV]","bin":50,"xmin":20.0,"xmax":200.0},
    "etal1":{"name":"leta1_eta","title":"#eta^{min}(#ell)","bin":50,"xmin":-6.,"xmax":6.},
    "etal2":{"name":"leta2_eta","title":"#eta^{max}(#ell)","bin":50,"xmin":-6,"xmax":6.},
    "ptj1":{"name":"jpt1_pt","title":"p_{T}^{max}(j) [GeV]","bin":50,"xmin":0.0,"xmax":1000.0},
    "ptj2":{"name":"jpt2_pt","title":"p_{T}^{min}(j) [GeV]","bin":50,"xmin":0.0,"xmax":500.0},
    "etaj1":{"name":"jeta1_eta","title":"#eta^{min}(j)","bin":50,"xmin":-6.,"xmax":6.},
    "etaj2":{"name":"jeta2_eta","title":"#eta^{max}(j)","bin":50,"xmin":-6,"xmax":6.},
    
    "mll":{"name":"mll","title":"m_{#ell #ell} [GeV]","bin":50,"xmin":0.,"xmax":2500.},
    "mr":{"name":"mr","title":"m_{R} [GeV]","bin":50,"xmin":0.,"xmax":5000.},
    "mt":{"name":"mt","title":"m_{T} [GeV]","bin":50,"xmin":0.,"xmax":2500.},
    "mjj":{"name":"mjj","title":"m_{jj} [GeV]","bin":50,"xmin":0,"xmax":5000.},
    "ptll":{"name":"ptll","title":"p_{T} (#ell#ell) [GeV]","bin":50,"xmin":0,"xmax":1000.},
    "ptjj":{"name":"ptjj","title":"p_{T} (jj) [GeV]","bin":50,"xmin":0,"xmax":1000.},
    "detajj":{"name":"detajj","title":"#Delta #eta (j,j)","bin":50,"xmin":0.,"xmax":10.},
    "dphill":{"name":"dphill","title":"#Delta #phi (#ell,#ell)","bin":25,"xmin":0,"xmax":3.14},
    "dphijj":{"name":"dphijj","title":"#Delta #phi (jj)","bin":50,"xmin":0,"xmax":3.14},
    "dphillmet":{"name":"dphillmet","title":"#Delta #phi (llmet)","bin":50,"xmin":0,"xmax":3.14},
}

variables2D = {
    "dphill_etajmax":{ 
                  "namex":"dphill","namey":"jpt1_eta","titlex":"#Delta #phi (#ell,#ell)","titley":"#eta^{max}(j)",
                  "binx":25,"xmin":0,"xmax":3.14,"biny":25,"ymin":0,"ymax":5.
               },
}


#sig_label = 'W_{L}^{#pm} W_{L}^{#pm} j j, (#kappa_{V}=1.00)'

wlwl_label = 'W_{L}^{#pm} W_{L}^{#pm} j j'

colors = {}

colors[wlwl_label + ' k=0.90'] = ROOT.kRed+1
colors[wlwl_label + ' k=0.95'] = ROOT.kRed-9
colors[wlwl_label + ' k=1.00'] = ROOT.kOrange+7
colors[wlwl_label + ' k=1.05'] = ROOT.kPink
colors[wlwl_label + ' k=1.10'] = ROOT.kBlue

#colors['WZ'] = ROOT.kBlue-7

signal_groups = collections.OrderedDict()
signal_groups[wlwl_label + ' k=1.00'] = ['mgp8_pp_vbs_wwss_kw_100_LL','mgp8_pp_vbs_wwss_kw_100_TT','mgp8_pp_vbs_wwss_kw_100_TL']

background_groups = collections.OrderedDict()
background_groups[wlwl_label + ' k=0.90'] = ['mgp8_pp_vbs_wwss_kw_090_LL','mgp8_pp_vbs_wwss_kw_090_TL','mgp8_pp_vbs_wwss_kw_090_TT']
background_groups[wlwl_label + ' k=0.95'] = ['mgp8_pp_vbs_wwss_kw_095_LL','mgp8_pp_vbs_wwss_kw_095_TL','mgp8_pp_vbs_wwss_kw_095_TT']
background_groups[wlwl_label + ' k=1.05'] = ['mgp8_pp_vbs_wwss_kw_105_LL','mgp8_pp_vbs_wwss_kw_105_TL','mgp8_pp_vbs_wwss_kw_105_TT']
background_groups[wlwl_label + ' k=1.10'] = ['mgp8_pp_vbs_wwss_kw_110_LL','mgp8_pp_vbs_wwss_kw_110_TL','mgp8_pp_vbs_wwss_kw_110_TT']

# global parameters
intLumi = 30000000
delphesVersion = '3.4.2'

uncertainties = []
uncertainties.append([0., 0.])
uncertainties.append([0.01, 0.00])
uncertainties.append([0.01, 0.01])

# the first time needs to be set to True
runFull = True
#runFull = False


# base pre-selections

presel  = 'lpt2_pt > 20. && abs(lpt1_eta) < 4. &&  abs(lpt2_eta) < 4.'
presel += ' && jpt2_pt > 30. && abs(jpt1_eta) < 6. &&  abs(lpt1_eta) < 6.'

vbs_cuts = presel + ' && mjj > 500. && detajj > 3.5'
wz_cuts = vbs_cuts + '&& mll > 50. && met_pt'

selection  = []
selection.append(presel)
selection.append(vbs_cuts)
selection.append(wz_cuts)

# add mass-dependent list of event selections here if needed...
selections = collections.OrderedDict()
selections[wlwl_label + ' k=1.00'] = []
selections[wlwl_label + ' k=1.00'] = selection
