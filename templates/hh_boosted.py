import ROOT
import collections

### variable list
variables = {
    "h1_m":{"name":"softDropped_bJet1_m","title":"m_{j}^{(1)} [GeV]","bin":100,"xmin":0.0,"xmax":200.0},
    "h2_m":{"name":"softDropped_bJet2_m","title":"m_{j}^{(2)} [GeV]","bin":100,"xmin":0.0,"xmax":200.0},
    "hh_m":{"name":"hh_m","title":"m_{HH} [GeV]","bin":60,"xmin":100.0,"xmax":2500.0},
    "hhgen_m":{"name":"hh_gen_m","title":"m_{HH} (gen) [GeV]","bin":100,"xmin":100.0,"xmax":2500.0},
    "hh_pt":{"name":"hh_pt","title":"p_{T,HH} [GeV]","bin":100,"xmin":250.0,"xmax":3000.0},
    'h1_tau21':{'name':'bJet1_tau21','title':'#tau_{2,1} (j^{(1)})','bin':100,'xmin':0.0,'xmax':1.0},
    'h2_tau21':{'name':'bJet2_tau21','title':'#tau_{2,1} (j^{(2)})','bin':100,'xmin':0.0,'xmax':1.0},
    "drhh":{"name":"drhh","title":"#Delta R(HH)","bin":100,"xmin":0.0,"xmax":6.0},
    "dPtRel":{"name":"dPtRel","title":"#Delta p_{T}(H) / p_{T}(HH)","bin":100,"xmin":0.0,"xmax":1.0},
}

variables2D = {
    "hmbb_mbb":{ 
                  "namex":"softDropped_bJet1_m","namey":"softDropped_bJet2_m","titlex":"m_{H}^{(1)} [GeV]","titley":"m_{H}^{(2)} [GeV]",
                  "binx":50,"xmin":90.0,"xmax":140.0,"biny":50,"ymin":90.0,"ymax":140.0
               },

    "hmbb_mhh":{ 
                  "namex":"softDropped_bJet1_m","namey":"hh_m","titlex":"m_{H}^{(1)} [GeV]","titley":"m_{h h} [GeV]",
                  "binx":50,"xmin":90.0,"xmax":140.0,"biny":50,"ymin":240.0,"ymax":2500.0
               },
}


colors = {}

colors['HH(#kappa_{l}=0.50)'] = ROOT.kBlack
#colors['HH(#kappa_{l}=0.90)'] = ROOT.kRed
#colors['HH(#kappa_{l}=0.95)'] = ROOT.kRed
colors['HH(#kappa_{l}=1.00)'] = ROOT.kBlack
#colors['HH(#kappa_{l}=1.05)'] = ROOT.kRed
#colors['HH(#kappa_{l}=1.10)'] = ROOT.kRed
#colors['HH(#kappa_{l}=1.50)'] = ROOT.kRed
colors['HH(#kappa_{l}=2.00)'] = ROOT.kBlack

'''colors['EWK'] = ROOT.kAzure+5
colors['QCD+EWK'] = ROOT.kAzure+3
colors['QCD'] = ROOT.kAzure+1
'''

colors['QCD'] = ROOT.kRed+1
colors['QCD+EWK'] = ROOT.kCyan+2
colors['EWK'] = ROOT.kGreen+1



signal_groups = collections.OrderedDict()

signal_groups['HH(#kappa_{l}=0.50)'] = ['mgp8_pp_hhj_lambda050_5f_hhbbbb']
#signal_groups['HH(#kappa_{l}=0.90)'] = ['mgp8_pp_hhj_lambda090_5f_hhbbbb']
#signal_groups['HH(#kappa_{l}=0.95)'] = ['mgp8_pp_hhj_lambda095_5f_hhbbbb']
signal_groups['HH(#kappa_{l}=1.00)'] = ['mgp8_pp_hhj_lambda100_5f_hhbbbb']
#signal_groups['HH(#kappa_{l}=1.05)'] = ['mgp8_pp_hhj_lambda105_5f_hhbbbb']
#signal_groups['HH(#kappa_{l}=1.10)'] = ['mgp8_pp_hhj_lambda110_5f_hhbbbb']
#signal_groups['HH(#kappa_{l}=1.50)'] = ['mgp8_pp_hhj_lambda150_5f_hhbbbb']
signal_groups['HH(#kappa_{l}=2.00)'] = ['mgp8_pp_hhj_lambda200_5f_hhbbbb']

background_groups = collections.OrderedDict()


background_groups['QCD'] = [
                            'mgp8_pp_bbbbj_QCD',
                           ]

background_groups['QCD+EWK'] = [
                            'mgp8_pp_bbbbj_QCDQED',
                           ]
                           
background_groups['EWK'] = [
                            'mgp8_pp_bbbbj_QED',
                           ]
                           

# global parameters
intLumi = 30000000

delphesVersion = '3.4.2'

uncertainties = []
uncertainties.append([0., 0.])
uncertainties.append([0.01, 0.00])
uncertainties.append([0.01, 0.01])

# the first time needs to be set to True
runFull = True

# base pre-selections

selbase  = 'bJet1_pt > 300. && abs(bJet1_eta) < 3.0 && '
selbase += 'bJet2_pt > 200. && abs(bJet2_eta) < 3.0'

selection = selbase
selection += ' && drhh < 3.0 && dPtRel < 0.9'
selection += ' && hh_pt > 250.'

selection2 = selection
selection2 += ' && bJet1_tau21 < 0.4'
selection2 += ' && bJet2_tau21 < 0.4'
selection2 += ' && softDropped_bJet1_m. < 135. && softDropped_bJet1_m. > 100.'
selection2 += ' && softDropped_bJet2_m. < 135. && softDropped_bJet2_m. > 100.'

selections = collections.OrderedDict()

selections['HH(#kappa_{l}=0.50)'] = []
#selections['HH(#kappa_{l}=0.90)'] = []
#selections['HH(#kappa_{l}=0.95)'] = []
selections['HH(#kappa_{l}=1.00)'] = []
#selections['HH(#kappa_{l}=1.05)'] = []
#selections['HH(#kappa_{l}=1.10)'] = []
#selections['HH(#kappa_{l}=1.50)'] = []
selections['HH(#kappa_{l}=2.00)'] = []

selections['HH(#kappa_{l}=0.50)'].append(selbase)
#selections['HH(#kappa_{l}=0.90)'].append(selbase)
#selections['HH(#kappa_{l}=0.95)'].append(selbase)
selections['HH(#kappa_{l}=1.00)'].append(selbase)
#selections['HH(#kappa_{l}=1.05)'].append(selbase)
#selections['HH(#kappa_{l}=1.10)'].append(selbase)
#selections['HH(#kappa_{l}=1.50)'].append(selbase)
#selections['HH(#kappa_{l}=1.50)'].append(selbase)
selections['HH(#kappa_{l}=2.00)'].append(selbase)



for i in xrange(3):
   #pt1 = float(1.+i*0.2)*300.
   #pt2 = float(1.+i*0.2)*200.

   pt1 = 300. +float(i*50.)
   pt2 = 200. +float(i*50.)
   
   ptstr = ' && bJet1_pt > {} && bJet2_pt > {} '.format(pt1, pt2)
   selections['HH(#kappa_{l}=0.50)'].append(selection + ptstr)
   #selections['HH(#kappa_{l}=0.90)'].append(selection + ptstr)
   #selections['HH(#kappa_{l}=0.95)'].append(selection + ptstr)
   selections['HH(#kappa_{l}=1.00)'].append(selection + ptstr)
   #selections['HH(#kappa_{l}=1.05)'].append(selection + ptstr)
   #selections['HH(#kappa_{l}=1.10)'].append(selection + ptstr)
   #selections['HH(#kappa_{l}=1.50)'].append(selection + ptstr)
   selections['HH(#kappa_{l}=2.00)'].append(selection + ptstr)

for i in xrange(3):

   pt1 = 300. +float(i*50.)
   pt2 = 200. +float(i*50.)
   ptstr = ' && bJet1_pt > {} && bJet2_pt > {} '.format(pt1, pt2)
   selections['HH(#kappa_{l}=0.50)'].append(selection2 + ptstr)
   #selections['HH(#kappa_{l}=0.90)'].append(selection2 + ptstr)
   #selections['HH(#kappa_{l}=0.95)'].append(selection2 + ptstr)
   selections['HH(#kappa_{l}=1.00)'].append(selection2 + ptstr)
   #selections['HH(#kappa_{l}=1.05)'].append(selection2 + ptstr)
   #selections['HH(#kappa_{l}=1.10)'].append(selection2 + ptstr)
   #selections['HH(#kappa_{l}=1.50)'].append(selection2 + ptstr)
   selections['HH(#kappa_{l}=2.00)'].append(selection2 + ptstr)


