import ROOT
import collections

variables = {
    "h1_pt":{"name":"h1_pt","title":"p_{T}^{max}(h) [GeV]","bin":100,"xmin":0.0,"xmax":1000.0},
    "h2_pt":{"name":"h2_pt","title":"p_{T}^{min}(h) [GeV]","bin":100,"xmin":0.0,"xmax":1000.0},

    "h1_m":{"name":"h1_m","title":"m^{max}(h) [GeV]","bin":50,"xmin":50.0,"xmax":200.0},
    "h2_m":{"name":"h2_m","title":"m^{min}(h) [GeV]","bin":50,"xmin":20.0,"xmax":200.0},

    "hh_m":{"name":"hh_m","title":"m(hh) [GeV]","bin":50,"xmin":100.0,"xmax":1000.0},
    #"bdt":{"name":"tmva_bdt","title":"BDT output","bin":50,"xmin":-0.5,"xmax":0.6},
    "bdt":{"name":"tmva_bdt","title":"BDT output","bin":50,"xmin":-1.0,"xmax":1.0},

}

variables2D = {
}


'''
kls = [
       0.00,
       0.20,
       0.40,
       0.60,
       0.70,
       0.80,
       0.85,
       0.90, 
       0.92, 
       0.94, 
       0.96, 
       0.97, 
       0.98, 
       0.99, 
       1.00, 
       1.01, 
       1.02, 
       1.03, 
       1.04, 
       1.06, 
       1.08, 
       1.10,
       1.20,
       1.30,
       1.40,
       1.45,
       1.50,
       1.55,
       1.60,
       1.70,
      #1.80,
       1.90,
       2.00,
       2.20,
       2.40,
       2.60,
       2.80,
       3.00
       ]
'''

kls = [
       1.00, 
      ]

'''
kls = [
       0.00,
       0.20,
       0.40,
       0.60,
       0.70,
       0.80,
       0.85,
       0.90, 
       0.92, 
       0.94, 
       0.96, 
       0.97, 
       0.98, 
       0.99, 
       1.00, 
       1.01, 
       #1.02, 
       #1.03, 
       1.04, 
       1.06, 
       1.08, 
       1.10,
       1.20,
       1.30,
       1.40,
       1.45,
       1.50,
       1.55,
       1.60,
       1.70,
      #1.80,
       1.90,
       2.00,
       2.20,
       2.40,
       2.60,
       2.80,
       3.00
       ]
'''

colors = {}
for k in kls:
    signal_str='HH(#kappa_{{#lambda}}={:.2f})'.format(k)
    colors[signal_str] = ROOT.kBlue+3

colors['ZZ'] = ROOT.kCyan-8
colors['single Higgs'] = ROOT.kAzure+1 
colors['Z+bb'] = ROOT.kOrange
colors['top pair'] = ROOT.kGreen-2
colors['QCD'] =ROOT.kRed-7 

'''
colors['j#gamma + Jets'] = ROOT.kAzure+1
colors['#gamma#gamma + Jets'] = ROOT.kCyan-8
colors['H'] = ROOT.kViolet-4
'''

signal_groups = collections.OrderedDict()
for k in kls:
    signal_str='HH(#kappa_{{#lambda}}={:.2f})'.format(k)
    lambda_str='lambda{:03d}_5f'.format(int(k*100))
    signal_groups[signal_str] = ['pwp8_pp_hh_{}_hhbbbb'.format(lambda_str), 'mgp8_pp_vbfhh_{}_hhbbbb'.format(lambda_str), 'mgp8_pp_tthh_{}_hhbbbb'.format(lambda_str), 'mgp8_pp_vhh_{}_hhbbbb'.format(lambda_str)]
    #signal_groups[signal_str] = ['pwp8_pp_hh_{}_hhbbbb'.format(lambda_str)]

#signal_groups['HH(#kappa_{l}=100)'] = ['pwp8_pp_hh_lambda100_5f_hhbbbb', 'mgp8_pp_vbfhh_lambda100_5f_hhbbbb', 'mgp8_pp_tthh_lambda100_5f_hhbbbb', 'mgp8_pp_vhh_lambda100_5f_hhbbbb']

background_groups = collections.OrderedDict()

background_groups['ZZ'] = ['mgp8_pp_bbjj_QED_5f']
background_groups['single Higgs'] = ['mgp8_pp_h012j_5f', 'mgp8_pp_tth01j_5f','mgp8_pp_vh012j_5f', 'mgp8_pp_vbf_h01j_5f']
background_groups['Z+bb'] = ['mgp8_pp_bbjj_QCDQED_5f']
background_groups['top pair'] = ['mgp8_pp_tt012j_5f']
background_groups['QCD'] = ['mgp8_pp_bbjj_QCD_5f']
#background_groups['QCD'] = ['mgp8_pp_bbbb_QCD_5f']

#FIXME: missing 'mgp8_pp_vh012j_5f', 'mgp8_pp_vbf_h01j_5f'
#background_groups['single Higgs'] = []


# global parameters
intLumi = 30000000
delphesVersion = '3.4.2'

uncertainties = []
uncertainties.append([0., 0.])
uncertainties.append([0.01, 0.00])
uncertainties.append([0.01, 0.01])


# base pre-selections

sel0   = 'b4_pt > 45.'

sel1 = sel0
sel1 += ' && tmva_bdt > 0.44'

selection  = []
selection.append(sel0)
selection.append(sel1)

'''
for i in range(1,6):
   pt = 45 + i*10.
   bdtstr = ' && b4_pt > {}'.format(pt, pt*2./3.)
   selection.append(sel0 + bdtstr)
'''

'''
for i in range(10):
   bdt = 0.2 + i*0.04
   bdtstr = ' && tmva_bdt > {}'.format(bdt)
   selection.append(sel0 + bdtstr)
'''
# add mass-dependent list of event selections here if needed...
selections = collections.OrderedDict()
for k in kls:
    signal_str='HH(#kappa_{{#lambda}}={:.2f})'.format(k)
    selections[signal_str] = []

for sel in selection:
    for k in kls:    
        signal_str='HH(#kappa_{{#lambda}}={:.2f})'.format(k)
        selections[signal_str].append(sel)
