import ROOT
import collections

### variable list
variables = {
    "pth":{"name":"higgs_pt","title":"p_{T}^{H} [GeV]","bin":100,"xmin":50,"xmax":1000},
    "pthl":{"name":"higgs_pt","title":"p_{T}^{H} [GeV]","bin":100,"xmin":0,"xmax":2000},
    "mhl":{"name":"higgs_m","title":"m_{H} [GeV]","bin":100,"xmin":50,"xmax":2000},
    "mh":{"name":"higgs_m","title":"m_{H} [GeV]","bin":100,"xmin":110,"xmax":140},
    "ptm1":{"name":"mu1_pt","title":"p_{T}^{max}(#mu) [GeV]","bin":100,"xmin":0,"xmax":1000},
    "ptm2":{"name":"mu2_pt","title":"p_{T}^{min}(#mu) [GeV]","bin":100,"xmin":0,"xmax":1000},
}

variables2D = {
}


colors = {}
colors['H(125)'] = ROOT.kRed
colors['#mu#mu'] = ROOT.kBlue+2

signal_groups = collections.OrderedDict()
signal_groups['H(125)'] = ['mgp8_pp_h012j_5f_HT_0_27000_hmumu', 
                           'mgp8_pp_vbf_h01j_5f_HT_0_27000_hmumu', 
                           'mgp8_pp_tth01j_5f_HT_0_27000_hmumu', 
                           #'mgp8_pp_vh012j_5f_HT_0_27000_hmumu'
                           ]



background_groups = collections.OrderedDict()

background_groups['#mu#mu'] = [
                                'mgp8_pp_mumuj_mhcut_5f_HT_20_100',
                                'mgp8_pp_mumuj_mhcut_5f_HT_100_400',
                                'mgp8_pp_mumuj_mhcut_5f_HT_400_27000',
]


# global parameters
intLumi = 15000000
delphesVersion = '3.4.2'

### signal and background uncertainties hypothesis
uncertainties = []
uncertainties.append([0., 0.])
uncertainties.append([0.02, 0.0])
uncertainties.append([0.02, 0.001])
uncertainties.append([0.02, 0.01])

# the first time needs to be set to True
runFull = True
#runFull = False

# base selections
selbase_nomasscut = ('mu2_pt > 20. && mu1_eta < 4 && mu2_eta < 4 &&'
            'nbjets == 0 &&'
            'met_pt < 50')

selbase_masscut = ('mu2_pt > 20. && mu1_eta < 4 && mu2_eta < 4 &&'
            'nbjets == 0 &&'
            'met_pt < 50 &&'
            'higgs_m > 124 && higgs_m < 126')

selections = collections.OrderedDict()
selections['H(125)'] = []
selections['H(125)'].append(selbase_nomasscut)
selections['H(125)'].append(selbase_masscut)

selections_pt = []
for i in range(20):
#for i in range(2):
   pt = 50. + i*25.
   ptstr = ' && higgs_pt > {}'.format(pt)
   selections['H(125)'].append(selbase_nomasscut + ptstr)
   selections_pt.append(selbase_masscut + ptstr)

selections['H(125)'] += selections_pt

