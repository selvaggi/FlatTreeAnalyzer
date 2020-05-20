import ROOT
import collections

### variable list
variables = {
    "pth":{"name":"higgs_pt","title":"p_{T}^{H} [GeV]","bin":100,"xmin":0,"xmax":1000},
    "pthl":{"name":"higgs_pt","title":"p_{T}^{H} [GeV]","bin":100,"xmin":0,"xmax":3000},
    "mh":{"name":"higgs_m","title":"m_{H} [GeV]","bin":100,"xmin":110,"xmax":140},
    "mhl":{"name":"higgs_m","title":"m_{H} [GeV]","bin":100,"xmin":50,"xmax":600},
    "ptm1":{"name":"l1_pt","title":"p_{T}^{1}(#mu) [GeV]","bin":100,"xmin":0,"xmax":500},
    "ptm2":{"name":"l2_pt","title":"p_{T}^{2}(#mu) [GeV]","bin":100,"xmin":0,"xmax":500},
    "ptm3":{"name":"l3_pt","title":"p_{T}^{3}(#mu) [GeV]","bin":100,"xmin":0,"xmax":500},
    "ptm4":{"name":"l4_pt","title":"p_{T}^{4}(#mu) [GeV]","bin":100,"xmin":0,"xmax":500},
}

variables2D = {
}


colors = {}
colors['H(125)'] = ROOT.kRed
colors['ZZ*'] = ROOT.kGreen+2

signal_groups = collections.OrderedDict()
signal_groups['H(125)'] = ['mgp8_pp_h012j_5f_HT_0_27000_hllll', 
                           'mgp8_pp_vbf_h01j_5f_HT_0_27000_hllll', 
			   'mgp8_pp_tth01j_5f_HT_0_27000_hllll', 
			   'mgp8_pp_vh012j_5f_HT_0_27000_hllll']



background_groups = collections.OrderedDict()
#background_groups['ZZ'] = ['mgp8_pp_llll01j_5f']

background_groups['ZZ*'] = [
                            'mgp8_pp_llllj_mhcut_5f_HT_20_100',
                            'mgp8_pp_llllj_mhcut_5f_HT_100_400',
                            'mgp8_pp_llllj_mhcut_5f_HT_400_27000',
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


# base selections
selbase_nomasscut = ('zed1_m > 40. && zed1_m < 120. &&'
                'zed2_m > 12. && zed2_m < 120. &&'
                'l1_pt > 20. && l2_pt > 10. && l3_pt > 7. && l4_pt > 5. &&'
                'abs(l1_eta) < 4 && abs(l2_eta) < 4')

selbase_nomasscut += ' && abs(l1_pdgid)==13 && abs(l2_pdgid)==13  && abs(l3_pdgid)==13 && abs(l4_pdgid)==13'

selbase_masscut = ('zed1_m > 40. && zed1_m < 120. &&'
                'zed2_m > 12. && zed2_m < 120. &&'
                'l1_pt > 20. && l2_pt > 10. && l3_pt > 7. && l4_pt > 5. &&'
                'abs(l1_eta) < 4 && abs(l2_eta) < 4 &&'
                'higgs_m > 122.5 && higgs_m < 127.5')

selbase_masscut += ' && abs(l1_pdgid)==13 && abs(l2_pdgid)==13  && abs(l3_pdgid)==13 && abs(l4_pdgid)==13'

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


