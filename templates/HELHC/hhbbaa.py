import ROOT
import collections

variables = {
    "pta1":{"name":"a1_pt","title":"p_{T}^{max}(#gamma) [GeV]","bin":50,"xmin":20.0,"xmax":120.0},
    "pta2":{"name":"a2_pt","title":"p_{T}^{min}(#gamma) [GeV]","bin":50,"xmin":20.0,"xmax":60.0},
    "ptb1":{"name":"b1_pt","title":"p_{T}^{max}(b) [GeV]","bin":50,"xmin":20.0,"xmax":120.0},
    "ptb2":{"name":"b2_pt","title":"p_{T}^{min}(b) [GeV]","bin":50,"xmin":20.0,"xmax":60.0},
    "pthaa":{"name":"haa_pt","title":"p_{T}(h #rightarrow #gamma gamma) [GeV]","bin":50,"xmin":0.0,"xmax":500.0},
    "pthbb":{"name":"hbb_pt","title":"p_{T}(h #rightarrow b b) [GeV]","bin":50,"xmin":0.0,"xmax":500.0},
    "draa":{"name":"draa","title":"#Delta R (#gamma_{1},#gamma_{2})","bin":50,"xmin":0.0,"xmax":6.00},
    "drbb":{"name":"drbb","title":"#Delta R (b_{1},b_{2})","bin":50,"xmin":0.0,"xmax":6.00},
    "haa_m":{"name":"haa_m","title":"m_{#gamma #gamma} [GeV]","bin":28,"xmin":118.0,"xmax":132.0},
    "hbb_m":{"name":"hbb_m","title":"m_{j j} [GeV]","bin":25,"xmin":80.0,"xmax":150.0},
    "hh_m":{"name":"hh_m","title":"m_{j j #gamma #gamma} [GeV]","bin":50,"xmin":100.0,"xmax":2000.0},
    "nljets":{"name":"nljets","title":"N_{jets}^{light}","bin":10,"xmin":-.05,"xmax":9.5},
    "nbjets":{"name":"nbjets","title":"N_{jets}^{b}","bin":10,"xmin":-.05,"xmax":9.5},
    "nlep":{"name":"nlep","title":"N_{leptons}","bin":5,"xmin":-.05,"xmax":4.5},
    "met":{"name":"met_pt","title":"E_{T}^{miss}","bin":50,"xmin":0,"xmax":500.},

}

variables2D = {
    "hmaa_mbb":{ 
                  "namex":"haa_m","namey":"hbb_m","titlex":"m_{#gamma #gamma} [GeV]","titley":"m_{j j} [GeV]",
                  "binx":50,"xmin":120.0,"xmax":130.0,"biny":50,"ymin":80.0,"ymax":140.0
               },

    "hmaa_mhh":{ 
                  "namex":"haa_m","namey":"hh_m","titlex":"m_{#gamma #gamma} [GeV]","titley":"m_{h h} [GeV]",
                  "binx":50,"xmin":120.0,"xmax":130.0,"biny":75,"ymin":240.0,"ymax":1500.0
               },
    
}


colors = {}

colors['HH(#kappa_{l}=0.50)' ] = ROOT.kRed
colors['HH(#kappa_{l}=0.75)' ] = ROOT.kRed
colors['HH(#kappa_{l}=0.80)' ] = ROOT.kRed
colors['HH(#kappa_{l}=0.85)' ] = ROOT.kRed
colors['HH(#kappa_{l}=0.875)'] = ROOT.kRed
colors['HH(#kappa_{l}=0.90)' ] = ROOT.kRed
colors['HH(#kappa_{l}=0.925)'] = ROOT.kRed
colors['HH(#kappa_{l}=0.95)' ] = ROOT.kRed
colors['HH(#kappa_{l}=0.975)'] = ROOT.kRed
colors['HH(#kappa_{l}=1.00)' ] = ROOT.kRed
colors['HH(#kappa_{l}=1.025)'] = ROOT.kRed
colors['HH(#kappa_{l}=1.05)' ] = ROOT.kRed
colors['HH(#kappa_{l}=1.075)'] = ROOT.kRed
colors['HH(#kappa_{l}=1.10)' ] = ROOT.kRed
colors['HH(#kappa_{l}=1.125)'] = ROOT.kRed
colors['HH(#kappa_{l}=1.150)'] = ROOT.kRed
colors['HH(#kappa_{l}=1.20)' ] = ROOT.kRed
colors['HH(#kappa_{l}=1.25)' ] = ROOT.kRed
colors['HH(#kappa_{l}=1.50)' ] = ROOT.kRed


colors['j#gamma + Jets'] = ROOT.kAzure+1
colors['#gamma#gamma + Jets'] = ROOT.kCyan-8
colors['ttH'] = ROOT.kViolet-4
colors['ggH'] = ROOT.kGreen-2
#colors['ggH2'] = ROOT.kGreen-5
colors['VH'] = ROOT.kOrange+3

'''
colors['j#gamma + Jets'] = ROOT.kAzure+1
colors['#gamma#gamma + Jets'] = ROOT.kCyan-8
colors['H'] = ROOT.kViolet-4
'''

signal_groups = collections.OrderedDict()

signal_groups['HH(#kappa_{l}=0.50)' ] = ['mgp8_pp_hh_5f_kl_0500_haa']
signal_groups['HH(#kappa_{l}=0.75)' ] = ['mgp8_pp_hh_5f_kl_0750_haa']
signal_groups['HH(#kappa_{l}=0.80)' ] = ['mgp8_pp_hh_5f_kl_0800_haa']
signal_groups['HH(#kappa_{l}=0.85)' ] = ['mgp8_pp_hh_5f_kl_0850_haa']
signal_groups['HH(#kappa_{l}=0.875)'] = ['mgp8_pp_hh_5f_kl_0875_haa']
signal_groups['HH(#kappa_{l}=0.90)' ] = ['mgp8_pp_hh_5f_kl_0900_haa']
signal_groups['HH(#kappa_{l}=0.925)'] = ['mgp8_pp_hh_5f_kl_0925_haa']
signal_groups['HH(#kappa_{l}=0.95)' ] = ['mgp8_pp_hh_5f_kl_0950_haa']
signal_groups['HH(#kappa_{l}=0.975)'] = ['mgp8_pp_hh_5f_kl_0975_haa']
signal_groups['HH(#kappa_{l}=1.00)' ] = ['mgp8_pp_hh_5f_kl_1000_haa']
signal_groups['HH(#kappa_{l}=1.025)'] = ['mgp8_pp_hh_5f_kl_1025_haa']
signal_groups['HH(#kappa_{l}=1.05)' ] = ['mgp8_pp_hh_5f_kl_1050_haa']
signal_groups['HH(#kappa_{l}=1.075)'] = ['mgp8_pp_hh_5f_kl_1075_haa']
signal_groups['HH(#kappa_{l}=1.10)' ] = ['mgp8_pp_hh_5f_kl_1100_haa']
signal_groups['HH(#kappa_{l}=1.125)'] = ['mgp8_pp_hh_5f_kl_1125_haa']
signal_groups['HH(#kappa_{l}=1.150)'] = ['mgp8_pp_hh_5f_kl_1150_haa']
signal_groups['HH(#kappa_{l}=1.20)' ] = ['mgp8_pp_hh_5f_kl_1200_haa']
signal_groups['HH(#kappa_{l}=1.25)' ] = ['mgp8_pp_hh_5f_kl_1250_haa']
signal_groups['HH(#kappa_{l}=1.50)' ] = ['mgp8_pp_hh_5f_kl_1500_haa']


background_groups = collections.OrderedDict()

'''
background_groups['j#gamma + Jets'] = ['mgp8_pp_jjja_5f']
background_groups['#gamma#gamma + Jets'] = ['mgp8_pp_jjaa_5f']
background_groups['H'] = ['mgp8_pp_tth01j_5f_haa','mgp8_pp_bbh_4f_haa','mgp8_pp_vh012j_5f_haa']
'''
'''
background_groups['j#gamma + Jets'] = ['mgp8_pp_jjja_5f']
background_groups['#gamma#gamma + Jets'] = ['mgp8_pp_jjaa_5f']
background_groups['ttH'] = ['mgp8_pp_tth01j_5f_haa']
background_groups['ggH'] = ['mgp8_pp_bbh_4f_haa']
#background_groups['ggH2'] = ['mgp8_pp_h012j_5f_haa']
background_groups['VH'] = ['mgp8_pp_vh012j_5f_haa']
'''

background_groups['VH'] = ['mgp8_pp_vh012j_5f_haa']
background_groups['ggH'] = ['mgp8_pp_bbh_4f_haa']
background_groups['ttH'] = ['mgp8_pp_tth01j_5f_haa']
background_groups['#gamma#gamma + Jets'] = ['mgp8_pp_jjaa_5f']
background_groups['j#gamma + Jets'] = ['mgp8_pp_jjja_5f']

# global parameters
intLumi = 15000000
delphesVersion = '3.4.2'

uncertainties = []
uncertainties.append([0., 0.])
uncertainties.append([0.01, 0.00])
uncertainties.append([0.01, 0.01])

# the first time needs to be set to True
runFull = True
#runFull = False


# base pre-selections

tthcut = ' && nlep == 0 && nljets < 4 && met_pt < 100 && draa < 3.0 && drbb < 2.5  && drbb > 0.6'
mcut = ' && abs(haa_m - 125.) < 50 && hbb_m > 80. && hbb_m < 140.'
mbbcut = ' && hbb_m > 90. && hbb_m < 140.'
maacut = ' && abs(haa_m - 125.) < 5.0 '
yrcut = ' && a1_pt > 60. && b1_pt > 60. && a2_pt > 30. && b2_pt > 30. && haa_pt > 100. && hbb_pt > 100. &&  nlep == 0'


selection_yr  = []
selection_cms = []
selection_new = []


sel0  = 'abs(b1_eta) < 6.0 && abs(b2_eta) < 6.0 && '
sel0 += 'abs(a1_eta) < 6.0 && abs(a2_eta) < 6.0 && '
sel0 += 'a1_pt > 35. && b1_pt > 35. && '
sel0 += 'a2_pt > 30. && b2_pt > 30. && '
sel0 += 'haa_m > 100. && haa_m < 150. && '
sel0 += 'hbb_m > 60. && hbb_m < 200.'

sel1 = sel0
sel1 += ' && abs(b1_eta) < 4.5 && abs(b2_eta) < 4.5 && '
sel1 += 'abs(a1_eta) < 4.5 && abs(a2_eta) < 4.5 && '
sel1 += 'a1_pt > 60. && b1_pt > 60. && '
sel1 += 'a2_pt > 30. && b2_pt > 30. && '
sel1 += 'haa_pt > 100. && hbb_pt > 100. &&'
sel1 += 'draa < 3.5 && drbb < 3.5 &&'
sel1 += 'nlep == 0'

sel2 = sel1 + mbbcut
sel3 = sel2 + maacut

selection_yr.append(sel0)
selection_yr.append(sel1)
selection_yr.append(sel2)
selection_yr.append(sel3)


sel4  = 'a1_pt > 30. && a1_pt > haa_m/3.0 && abs(a1_eta) < 2.5 && '
sel4 += 'a2_pt > 20. && a2_pt > haa_m/4.0 && abs(a2_eta) < 2.5 && '
sel4 += 'b1_pt > 25. && abs(b1_eta) < 2.5 && '
sel4 += 'b2_pt > 25. && abs(b2_eta) < 2.5 && '
sel4 += 'haa_m > 100 && haa_m < 180 && '
sel4 += 'hbb_m > 70 && hbb_m < 190'

sel5 = sel4 + mbbcut
sel6 = sel5 + maacut

selection_cms.append(sel4)
selection_cms.append(sel5)
selection_cms.append(sel6)


sel7  = 'a1_pt > 35. && a1_pt > haa_m/3.0 && abs(a1_eta) < 3.0 && '
sel7 += 'a2_pt > 30. && a2_pt > haa_m/4.0 && abs(a2_eta) < 3.0 && '
sel7 += 'b1_pt > 35. && abs(b1_eta) < 3.0 && '
sel7 += 'b2_pt > 30. && abs(b2_eta) < 3.0 && '
sel7 += 'haa_m > 100. && haa_m < 150. && '
sel7 += 'hbb_m > 60. && hbb_m < 200.'

sel8 = sel7 + yrcut
sel9 = sel8 + tthcut
sel10 = sel9 + mbbcut
sel11 = sel10 + maacut

selection_new.append(sel7)
selection_new.append(sel8)
selection_new.append(sel9)
selection_new.append(sel10)
selection_new.append(sel11)


# add mass-dependent list of event selections here if needed...
selections = collections.OrderedDict()


selections['HH(#kappa_{l}=0.50)' ]  =  []
selections['HH(#kappa_{l}=0.75)' ]  =  []
selections['HH(#kappa_{l}=0.80)' ]  =  []
selections['HH(#kappa_{l}=0.85)' ]  =  []
selections['HH(#kappa_{l}=0.875)']  =  []
selections['HH(#kappa_{l}=0.90)' ]  =  []
selections['HH(#kappa_{l}=0.925)']  =  []
selections['HH(#kappa_{l}=0.95)' ]  =  []
selections['HH(#kappa_{l}=0.975)']  =  []
selections['HH(#kappa_{l}=1.00)' ]  =  []
selections['HH(#kappa_{l}=1.025)']  =  []
selections['HH(#kappa_{l}=1.05)' ]  =  []
selections['HH(#kappa_{l}=1.075)']  =  []
selections['HH(#kappa_{l}=1.10)' ]  =  []
selections['HH(#kappa_{l}=1.125)']  =  []
selections['HH(#kappa_{l}=1.150)']  =  []
selections['HH(#kappa_{l}=1.20)' ]  =  []
selections['HH(#kappa_{l}=1.25)' ]  =  []
selections['HH(#kappa_{l}=1.50)' ]  =  []

'''
for sel in selection_yr:
    selections['HH(#kappa_{l}=0.50)' ].append(sel)
    selections['HH(#kappa_{l}=0.75)' ].append(sel)
    selections['HH(#kappa_{l}=0.80)' ].append(sel)
    selections['HH(#kappa_{l}=0.85)' ].append(sel)
    selections['HH(#kappa_{l}=0.875)'].append(sel)
    selections['HH(#kappa_{l}=0.90)' ].append(sel)
    selections['HH(#kappa_{l}=0.925)'].append(sel)
    selections['HH(#kappa_{l}=0.95)' ].append(sel)
    selections['HH(#kappa_{l}=0.975)'].append(sel)
    selections['HH(#kappa_{l}=1.00)' ].append(sel)
    selections['HH(#kappa_{l}=1.025)'].append(sel)
    selections['HH(#kappa_{l}=1.05)' ].append(sel)
    selections['HH(#kappa_{l}=1.075)'].append(sel)
    selections['HH(#kappa_{l}=1.10)' ].append(sel)
    selections['HH(#kappa_{l}=1.125)'].append(sel)
    selections['HH(#kappa_{l}=1.150)'].append(sel)
    selections['HH(#kappa_{l}=1.20)' ].append(sel)
    selections['HH(#kappa_{l}=1.25)' ].append(sel)
    selections['HH(#kappa_{l}=1.50)' ].append(sel)

for sel in selection_cms:
    selections['HH(#kappa_{l}=0.50)' ].append(sel)
    selections['HH(#kappa_{l}=0.75)' ].append(sel)
    selections['HH(#kappa_{l}=0.80)' ].append(sel)
    selections['HH(#kappa_{l}=0.85)' ].append(sel)
    selections['HH(#kappa_{l}=0.875)'].append(sel)
    selections['HH(#kappa_{l}=0.90)' ].append(sel)
    selections['HH(#kappa_{l}=0.925)'].append(sel)
    selections['HH(#kappa_{l}=0.95)' ].append(sel)
    selections['HH(#kappa_{l}=0.975)'].append(sel)
    selections['HH(#kappa_{l}=1.00)' ].append(sel)
    selections['HH(#kappa_{l}=1.025)'].append(sel)
    selections['HH(#kappa_{l}=1.05)' ].append(sel)
    selections['HH(#kappa_{l}=1.075)'].append(sel)
    selections['HH(#kappa_{l}=1.10)' ].append(sel)
    selections['HH(#kappa_{l}=1.125)'].append(sel)
    selections['HH(#kappa_{l}=1.150)'].append(sel)
    selections['HH(#kappa_{l}=1.20)' ].append(sel)
    selections['HH(#kappa_{l}=1.25)' ].append(sel)
    selections['HH(#kappa_{l}=1.50)' ].append(sel)

for sel in selection_new:
    selections['HH(#kappa_{l}=0.50)' ].append(sel)
    selections['HH(#kappa_{l}=0.75)' ].append(sel)
    selections['HH(#kappa_{l}=0.80)' ].append(sel)
    selections['HH(#kappa_{l}=0.85)' ].append(sel)
    selections['HH(#kappa_{l}=0.875)'].append(sel)
    selections['HH(#kappa_{l}=0.90)' ].append(sel)
    selections['HH(#kappa_{l}=0.925)'].append(sel)
    selections['HH(#kappa_{l}=0.95)' ].append(sel)
    selections['HH(#kappa_{l}=0.975)'].append(sel)
    selections['HH(#kappa_{l}=1.00)' ].append(sel)
    selections['HH(#kappa_{l}=1.025)'].append(sel)
    selections['HH(#kappa_{l}=1.05)' ].append(sel)
    selections['HH(#kappa_{l}=1.075)'].append(sel)
    selections['HH(#kappa_{l}=1.10)' ].append(sel)
    selections['HH(#kappa_{l}=1.125)'].append(sel)
    selections['HH(#kappa_{l}=1.150)'].append(sel)
    selections['HH(#kappa_{l}=1.20)' ].append(sel)
    selections['HH(#kappa_{l}=1.25)' ].append(sel)
    selections['HH(#kappa_{l}=1.50)' ].append(sel)
'''

selections['HH(#kappa_{l}=1.00)'] = []

for sel in selection_yr:
    selections['HH(#kappa_{l}=1.00)'].append(sel)

for sel in selection_cms:
    selections['HH(#kappa_{l}=1.00)'].append(sel)

for sel in selection_new:
    selections['HH(#kappa_{l}=1.00)'].append(sel)
