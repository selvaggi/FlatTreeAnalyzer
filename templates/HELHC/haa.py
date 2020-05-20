import ROOT
import collections

### variable list
variables = {
    "pth":{"name":"higgs_pt","title":"p_{T}^{H} [GeV]","bin":100,"xmin":0,"xmax":1000},
    "pthl":{"name":"higgs_pt","title":"p_{T}^{H} [GeV]","bin":100,"xmin":0,"xmax":5000},
    "mh":{"name":"higgs_m","title":"m_{H} [GeV]","bin":50,"xmin":110,"xmax":140},
    "mhl":{"name":"higgs_m","title":"m_{H} [GeV]","bin":100,"xmin":50,"xmax":500},
    "pta1":{"name":"a1_pt","title":"p_{T}^{max}(#gamma) [GeV]","bin":100,"xmin":0,"xmax":1000},
    "pta2":{"name":"a2_pt","title":"p_{T}^{min}(#gamma) [GeV]","bin":100,"xmin":0,"xmax":1000},
}

variables2D = {
}


colors = {}

colors['H(125)'] = ROOT.kRed
colors['pp #rightarrow #gamma#gamma'] = ROOT.kYellow
colors['gg #rightarrow #gamma#gamma'] = ROOT.kOrange

signal_groups = collections.OrderedDict()
signal_groups['H(125)'] = ['mgp8_pp_h012j_5f_HT_0_27000_haa', 
                           'mgp8_pp_vbf_h01j_5f_HT_0_27000_haa', 
                           'mgp8_pp_tth01j_5f_HT_0_27000_haa', 
                           #'mgp8_pp_vh012j_5f_HT_0_27000_haa'
                           ]



background_groups = collections.OrderedDict()
#background_groups['gg #rightarrow #gamma#gamma'] = ['gg_aa01j_mhcut_5f']
#background_groups['pp #rightarrow #gamma#gamma'] = ['mgp8_pp_aa012j_mhcut_5f']

background_groups['gg #rightarrow #gamma#gamma'] = [
                                                     'mgp8_gg_aa01j_5f_HT_0_200',
                                                     'mgp8_gg_aa01j_5f_HT_200_600',
                                                     'mgp8_gg_aa01j_5f_HT_600_27000',
                                                   ]
background_groups['pp #rightarrow #gamma#gamma'] = [
                                                     'mgp8_pp_aa012j_5f_HT_0_200',
                                                     'mgp8_pp_aa012j_5f_HT_200_600',
                                                     'mgp8_pp_aa012j_5f_HT_600_27000',
                                                    ]


# global parameters
intLumi = 15000000
delphesVersion = '3.4.2'

### signal and background uncertainties hypothesis
uncertainties = []
uncertainties.append([0., 0.])
uncertainties.append([0.02, 0.0])
uncertainties.append([0.02, 0.005])
uncertainties.append([0.02, 0.01])

# the first time needs to be set to True
runFull = True

# base selections
selbase_nomasscut = ('a1_pt > 30. && a2_pt > 25. &&'
                     'abs(a1_eta) < 4.0 && abs(a2_eta) < 4.0')

selbase_masscut = ('a1_pt > 30. && a2_pt > 25. &&'
                'abs(a1_eta) < 4.0 && abs(a2_eta) < 4.0 &&'
                'higgs_m > 122.5 && higgs_m < 127.5')

selections = collections.OrderedDict()

selections['H(125)'] = []
selections['H(125)'].append(selbase_nomasscut)
selections['H(125)'].append(selbase_masscut)

selections_pt = []
for i in range(20):
   pt = 50. + i*25.
   ptstr = ' && higgs_pt > {}'.format(pt)
   masscut = ' && abs(higgs_m - 125.) < 2.5 + higgs_pt/200.'
   selections['H(125)'].append(selbase_nomasscut + ptstr)
   selections_pt.append(selbase_masscut + ptstr + masscut)

selections['H(125)'] += selections_pt

