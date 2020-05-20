import ROOT
import collections

### variable list
variables = {
    "pth":{"name":"higgs_pt","title":"p_{T}^{H} [GeV]","bin":100,"xmin":0,"xmax":300},
    "pthl":{"name":"higgs_pt","title":"p_{T}^{H} [GeV]","bin":100,"xmin":0,"xmax":1000},
    "mh":{"name":"higgs_m","title":"m_{H} [GeV]","bin":100,"xmin":114,"xmax":136},
    "mll":{"name":"zed_m","title":"m_{ll} [GeV]","bin":100,"xmin":12,"xmax":200},
    "ptm1":{"name":"l1_pt","title":"p_{T}^{max}(#mu) [GeV]","bin":100,"xmin":0,"xmax":1000},
    "ptm2":{"name":"l2_pt","title":"p_{T}^{min}(#mu) [GeV]","bin":100,"xmin":0,"xmax":1000},
    "pta":{"name":"a_pt","title":"p_{T}^(#gamma) [GeV]","bin":100,"xmin":0,"xmax":1000},
}

variables2D = {
}


colors = {}
colors['H(125)'] = ROOT.kRed
colors['Z*#gamma'] = ROOT.kMagenta-9

signal_groups = collections.OrderedDict()
signal_groups['H(125)'] = ['mgp8_pp_h012j_5f_HT_0_27000_hlla', 
                           'mgp8_pp_vbf_h01j_5f_HT_0_27000_hlla', 
                           'mgp8_pp_tth01j_5f_HT_0_27000_hlla', 
                           'mgp8_pp_vh012j_5f_HT_0_27000_hlla'
                           ]

background_groups = collections.OrderedDict()
#background_groups['Z*#gamma'] = ['mgp8_pp_lla01j_mhcut_5f']
'''
background_groups['Z*#gamma'] = [
                                  'mgp8_pp_llaj_mhcut_5f_HT_20_100',
                                  'mgp8_pp_llaj_mhcut_5f_HT_100_400',
                                  'mgp8_pp_llaj_mhcut_5f_HT_400_27000',
                                ]
'''

'''background_groups['Z*#gamma'] = [
                                  'mgp8_pp_lla01j_mhcut_5f',
                               ]
''' 
background_groups['Z*#gamma'] = [
                                  'mgp8_pp_llaj_mhcut_5f',
                                ]


# global parameters
intLumi = 15000000
delphesVersion = '3.4.2'

### signal and background uncertainties hypothesis
uncertainties = []
uncertainties.append([0., 0.])
uncertainties.append([0.01, 0.0])

# the first time needs to be set to True
runFull = True
#runFull = False


# base selections
# base selections
selbase_nomasscut = ('zed_m > 50. && zed_m < 200. &&'
                'l1_pt > 20. && l2_pt > 20. && a_pt > 15. &&'
                'abs(l1_eta) < 4 && abs(l2_eta) < 4 && abs(a_eta) < 4')

selbase_nomasscut += ' && abs(l1_pdgid)==13  && abs(l2_pdgid)==13'


selbase_masscut = ('zed_m > 75. && zed_m < 105. &&'
                'l1_pt > 20. && l2_pt > 20. && a_pt > 15. &&'
                'abs(l1_eta) < 4 && abs(l2_eta) < 4 && abs(a_eta) < 4 &&'
                'higgs_m > 122.5 && higgs_m < 127.5')

selbase_masscut += ' && abs(l1_pdgid)==13  && abs(l2_pdgid)==13'

selections = collections.OrderedDict()
selections['H(125)'] = []
selections['H(125)'].append(selbase_nomasscut)
selections['H(125)'].append(selbase_masscut)

selections_pt = []
for i in range(20):
   pt = 50. + i*25.
   ptstr = ' && higgs_pt > {}'.format(pt)
   selections['H(125)'].append(selbase_nomasscut + ptstr)
   selections_pt.append(selbase_masscut + ptstr)

selections['H(125)'] += selections_pt

