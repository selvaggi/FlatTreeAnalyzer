import ROOT
import collections

variables = {
    "ptta1":{"name":"ta1_pt","title":"p_{T}^{max}(#tau) [GeV]","bin":50,"xmin":20.0,"xmax":400.0},
    "ptta2":{"name":"ta2_pt","title":"p_{T}^{min}(#tau) [GeV]","bin":50,"xmin":20.0,"xmax":200.0},
    "ptb1":{"name":"b1_pt","title":"p_{T}^{max}(b) [GeV]","bin":50,"xmin":20.0,"xmax":400.0},
    "ptb2":{"name":"b2_pt","title":"p_{T}^{min}(b) [GeV]","bin":50,"xmin":20.0,"xmax":200.0},
    "etata1":{"name":"ta1_eta","title":"#eta^{max}(#tau) ","bin":50,"xmin":-6.0,"xmax":6.0},
    "etata2":{"name":"ta2_eta","title":"#eta^{min}(#tau) ","bin":50,"xmin":-6.0,"xmax":6.0},
    "etab1":{"name":"b1_eta","title":"#eta^{max}(b) ","bin":50,"xmin":-6.0,"xmax":6.0},
    "etab2":{"name":"b2_eta","title":"#eta^{min}(b) ","bin":50,"xmin":-6.0,"xmax":6.0},

    "pthtata":{"name":"htata_pt","title":"p_{T}(h #rightarrow #tau #tau) [GeV]","bin":50,"xmin":0.0,"xmax":500.0},
    "pthtata_metcorr":{"name":"htata_metcorr_pt","title":"p_{T}(h #rightarrow #tau #tau) (MET Corr.)[GeV]","bin":50,"xmin":0.0,"xmax":500.0},
    "pthbb":{"name":"hbb_pt","title":"p_{T}(h #rightarrow b b) [GeV]","bin":50,"xmin":0.0,"xmax":500.0},
    "drtata":{"name":"drtata","title":"#Delta R (#tau_{1},#tau_{2})","bin":50,"xmin":0.0,"xmax":6.00},
    "drbb":{"name":"drbb","title":"#Delta R (b_{1},b_{2})","bin":10,"xmin":0.0,"xmax":6.00},
    "htata_m":{"name":"htata_m","title":"m_{#tau#tau} [GeV]","bin":50,"xmin":20.0,"xmax":200.0},
    "hbb_m":{"name":"hbb_m","title":"m_{b b} [GeV]","bin":50,"xmin":50.0,"xmax":150.0},
    "hh_m":{"name":"hh_m","title":"m_{j j #tau #tau} [GeV]","bin":50,"xmin":100.0,"xmax":2000.0},

    "htata_metcorr_m":{"name":"htata_metcorr_m","title":"m_{#tau #tau}(MET corr.) [GeV]","bin":50,"xmin":50.0,"xmax":250.0},
    "hh_metcorr_m":{"name":"hh_metcorr_m","title":"m_{j j #tau #tau} (MET corr.) [GeV]","bin":50,"xmin":100.0,"xmax":2000.0},

    "mT2":{"name":"mT2","title":"m_{T2} [GeV]","bin":50,"xmin":20.0,"xmax":500.0},
    "sT":{"name":"sT","title":"H_{T} [GeV]","bin":50,"xmin":0.0,"xmax":2000.0},
    "ta1_mt":{"name":"ta1_mt","title":"m_{T}(#tau_{1}) [GeV]","bin":50,"xmin":0.0,"xmax":500.0},
    "ta2_mt":{"name":"ta2_mt","title":"m_{T}(#tau_{2}) [GeV]","bin":50,"xmin":0.0,"xmax":500.0},


    "nljets":{"name":"nljets","title":"N_{jets}^{light}","bin":10,"xmin":-.05,"xmax":9.5},
    "nlep":{"name":"nlep","title":"N_{lep}","bin":10,"xmin":-.05,"xmax":9.5},
    "ntajets":{"name":"ntajets","title":"N_{jets}^{#tau}","bin":10,"xmin":-.05,"xmax":9.5},
    "nbjets":{"name":"nbjets","title":"N_{jets}^{b}","bin":10,"xmin":-.05,"xmax":9.5},
    "met":{"name":"met_pt","title":"E_{T}^{miss}","bin":50,"xmin":0,"xmax":500.},
    #"bdt":{"name":"tmva_bdt","title":"BDT output","bin":50,"xmin":-0.6,"xmax":0.6},
    "bdt":{"name":"tmva_bdt","title":"BDT output","bin":50,"xmin":-1.0,"xmax":1.0},

}

variables2D = {
    "hmtata_mbb_metcorr":{ 
                  "namex":"htata_metcorr_m","namey":"hbb_m","titlex":"m_{#tau #tau} [GeV]","titley":"m_{b b} [GeV]",
                  "binx":50,"xmin":80.0,"xmax":150.0,"biny":50,"ymin":80.0,"ymax":140.0
               },
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
       1.02, 
       1.03, 
       1.04, 
       1.06, 
       1.08, 
       1.10,
       1.20,
      #1.30,
       1.40,
       1.45,
      #1.50,
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

#colors['HH(#kappa_{l}=0.99)'] = ROOT.kBlue+3

colors['single Higgs'] = ROOT.kAzure+1
colors['ZZ'] = ROOT.kRed-7
colors['Z+jets'] = ROOT.kOrange
colors['top pair'] = ROOT.kGreen-2
colors['ttV'] = ROOT.kViolet-2
colors['ttVV'] = ROOT.kYellow+3

'''
colors['j#gamma + Jets'] = ROOT.kAzure+1
colors['#gamma#gamma + Jets'] = ROOT.kCyan-8
colors['H'] = ROOT.kViolet-4
'''

signal_groups = collections.OrderedDict()
for k in kls:
    signal_str='HH(#kappa_{{#lambda}}={:.2f})'.format(k)
    lambda_str='lambda{:03d}_5f'.format(int(k*100))

    signal_groups[signal_str] = ['pwp8_pp_hh_{}_hhbbtata'.format(lambda_str), 'mgp8_pp_vbfhh_{}_hhbbtata'.format(lambda_str), 'mgp8_pp_tthh_{}_hhbbtata'.format(lambda_str), 'mgp8_pp_vhh_{}_hhbbtata'.format(lambda_str)]    
    #signal_groups[signal_str] = ['pwp8_pp_hh_{}_hhbbtata'.format(lambda_str), 'mgp8_pp_tthh_{}_hhbbtata'.format(lambda_str)]
    #signal_groups[signal_str] = ['pwp8_pp_hh_{}_hhbbtata'.format(lambda_str), 'mgp8_pp_vbfhh_{}_hhbbtata'.format(lambda_str), 'mgp8_pp_vhh_{}_hhbbtata'.format(lambda_str)]
    #signal_groups[signal_str] = ['pwp8_pp_hh_{}_hhbbtata'.format(lambda_str)]
    #signal_groups[signal_str] = ['mgp8_pp_tthh_{}_hhbbtata'.format(lambda_str)]

#signal_groups['HH(#kappa_{l}=100)'] = ['pwp8_pp_hh_lambda100_5f_hhbbtata', 'mgp8_pp_vbfhh_lambda100_5f_hhbbtata', 'mgp8_pp_tthh_lambda100_5f_hhbbtata', 'mgp8_pp_vhh_lambda100_5f_hhbbtata']


background_groups = collections.OrderedDict() 



background_groups['ZZ'] = ['mgp8_pp_bbtata_QED']

background_groups['ttVV'] = [ 'mgp8_pp_ttzz_5f','mgp8_pp_ttww_4f', 'mgp8_pp_ttwz_5f']

background_groups['Z+jets'] = ['mgp8_pp_bbtata_QCDQED']

background_groups['ttV'] = ['mgp8_pp_ttz_5f', 'mgp8_pp_ttw_5f']

#background_groups['single Higgs'] = ['mgp8_pp_h012j_5f', 'mgp8_pp_vh012j_5f', 'mgp8_pp_tth01j_5f', 'mgp8_pp_vbf_h01j_5f']

background_groups['single Higgs'] = ['mgp8_pp_h012j_5f', 'mgp8_pp_tth01j_5f','mgp8_pp_vh012j_5f', 'mgp8_pp_vbf_h01j_5f']

#background_groups['t#bar{t}'] = ['mgp8_pp_tt012j_5f_ttau']
background_groups['top pair'] = ['mgp8_pp_tt012j_5f']



# global parameters
intLumi = 30000000
delphesVersion = '3.4.2'

uncertainties = []
uncertainties.append([0., 0.])
uncertainties.append([0.01, 0.00])
uncertainties.append([0.01, 0.01])


# base pre-selections

presel = 'ta1_pt > 0.'

sel0   = 'ta1_pt > 45. && ta2_pt > 25. && b1_pt > 30. && b2_pt > 30.'
#sel0   = 'ta1_pt > 100. && ta2_pt > 100. && b1_pt > 50. && b2_pt > 50.'
#sel   = 'ta1_pt > 100. && ta2_pt > 100. && b1_pt > 60. && b2_pt > 60.'
sel0  += ' && abs(ta1_eta) < 3.0 && abs(ta2_eta) < 3.0  && abs(b1_eta) < 3.0 && abs(b2_eta) < 3.0'

sel1 = sel0

sel1 += ' && tmva_bdt > 0.24'

sel2 = sel1
sel2 += ' && htata_m > 90. && htata_m < 130.'
sel2 += ' && hbb_m > 100. && hbb_m < 135.'

#sel  += ' && nlep == 0 && nljets <3'
#sel2 = ' && tmva_bdt > 0.2' 
'''
sel2 = sel
sel2 += ' && htata_metcorr_pt > 100. && hbb_pt > 100.'
sel2 += ' && ta1_pt > 60. && b1_pt > 60.'
sel2 += ' && ta2_pt > 30. && b2_pt > 30.'
sel2 += ' && drbb < 2.5'
'''
'''
sel3 = sel2
sel3 += ' && mT2 > 125.'
'''

'''
sel4 = sel3
sel4 += ' && htata_m > 90. && htata_m < 130.'
sel4 += ' && hbb_m > 100. && hbb_m < 135.'
'''

# cut hard on b and taus maybe > 50 GeV
# cut on pTH > 100 
# hard eta cut at 2,5-3.0??

# need to add lepton veto when varialbe is available
#presel  += 

selection  = []

#sel1 += 'a1_pt > 60. && b1_pt > 60. && '
#sel1 += 'a2_pt > 30. && b2_pt > 30. && '
#sel1 += 'haa_pt > 100. && hbb_pt > 100. &&'
#sel1 += 'draa < 3.5 && drbb < 3.5 &&'
#sel1 += 'nlep == 0 && nljets <3'

#selection.append(presel)

selection.append(sel0)
selection.append(sel1)
#selection.append(sel2)
#selection.append(sel1)

#selection.append(sel2)
#selection.append(sel3)
#selection.append(sel4)

#sel7  = 'a1_pt > 35. && a1_pt > haa_m/3.0 && abs(a1_eta) < 3.0 && '
#sel7 += 'a2_pt > 30. && a2_pt > haa_m/4.0 && abs(a2_eta) < 3.0 && '

'''
for i in range(15):
   bdt = -0.0 + i*0.04
   bdtstr = ' && tmva_bdt > {}'.format(bdt)
   selection.append(sel1 + bdtstr)
'''
'''
for i in range(1,6):
   pt = 45 + i*10.
   bdtstr = ' && ta2_pt > {} && b2_pt > {}'.format(pt, pt*2./3.)
   selection.append(sel2 + bdtstr)
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

