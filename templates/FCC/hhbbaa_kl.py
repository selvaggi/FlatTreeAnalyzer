import ROOT
import collections


kl_list=['000','040','070','100','130','150','170','200','220','240','260','300']

'''
"pta1":{"name":"a1_pt","title":"p_{T}^{max}(#gamma) [GeV]","bin":50,"xmin":20.0,"xmax":400.0},
"pta2":{"name":"a2_pt","title":"p_{T}^{min}(#gamma) [GeV]","bin":50,"xmin":20.0,"xmax":200.0},
"ptb1":{"name":"b1_pt","title":"p_{T}^{max}(b) [GeV]","bin":50,"xmin":20.0,"xmax":400.0},
"ptb2":{"name":"b2_pt","title":"p_{T}^{min}(b) [GeV]","bin":50,"xmin":20.0,"xmax":200.0},
"pthaa":{"name":"haa_pt","title":"p_{T}(h #rightarrow #gamma gamma) [GeV]","bin":50,"xmin":0.0,"xmax":500.0},
"pthbb":{"name":"hbb_pt","title":"p_{T}(h #rightarrow b b) [GeV]","bin":50,"xmin":0.0,"xmax":500.0},
"draa":{"name":"draa","title":"#Delta R (#gamma_{1},#gamma_{2})","bin":50,"xmin":0.0,"xmax":6.00},
"drbb":{"name":"drbb","title":"#Delta R (b_{1},b_{2})","bin":50,"xmin":0.0,"xmax":6.00},
"nljets":{"name":"nljets","title":"N_{jets}^{light}","bin":10,"xmin":-.05,"xmax":9.5},
"nbjets":{"name":"nbjets","title":"N_{jets}^{b}","bin":10,"xmin":-.05,"xmax":9.5},
"nlep":{"name":"nlep","title":"N_{leptons}","bin":5,"xmin":-.05,"xmax":4.5},
"met":{"name":"met_pt","title":"E_{T}^{miss}","bin":50,"xmin":0,"xmax":500.},
'''


variables = {
    

    "haa_m":{"name":"haa_m","title":"m_{#gamma#gamma} [GeV]","bin":50,"xmin":118.0,"xmax":132.0},
    "hbb_m":{"name":"hbb_m","title":"m_{bb} [GeV]","bin":50,"xmin":70.0,"xmax":150.0},
    "hh_m":{"name":"hh_m","title":"m_{hh} [GeV]","bin":50,"xmin":200.0,"xmax":1000.0},
    "pta1":{"name":"a1_pt","title":"p_{T}^{max}(#gamma) [GeV]","bin":50,"xmin":20.0,"xmax":400.0},
    "ea1":{"name":"a1_e","title":"E^{max}(#gamma) [GeV]","bin":50,"xmin":20.0,"xmax":400.0},
    "ea2":{"name":"a2_e","title":"E_{T}^{min}(#gamma) [GeV]","bin":50,"xmin":20.0,"xmax":200.0},
    "etaa1":{"name":"a1_eta","title":"#eta^{max}(#gamma)","bin":50,"xmin":-6,"xmax":6},
    "etaa2":{"name":"a2_eta","title":"#eta^{min}(#gamma)","bin":50,"xmin":-6,"xmax":6},
    "etab1":{"name":"b1_eta","title":"#eta^{max}(b)","bin":50,"xmin":-6,"xmax":6},
    "etab2":{"name":"b2_eta","title":"#eta^{min}(b)","bin":50,"xmin":-6,"xmax":6},
    "pta1":{"name":"a1_pt","title":"p_{T}^{max}(#gamma) [GeV]","bin":50,"xmin":20.0,"xmax":400.0},
    "ptb1":{"name":"b1_pt","title":"p_{T}^{max}(b) [GeV]","bin":50,"xmin":20.0,"xmax":400.0},
    "ptb2":{"name":"b2_pt","title":"p_{T}^{min}(b) [GeV]","bin":50,"xmin":20.0,"xmax":200.0},
    "pthaa":{"name":"haa_pt","title":"p_{T}(h #rightarrow #gamma #gamma) [GeV]","bin":50,"xmin":0.0,"xmax":500.0},
    "pthbb":{"name":"hbb_pt","title":"p_{T}(h #rightarrow b b) [GeV]","bin":50,"xmin":0.0,"xmax":500.0},
    "draa":{"name":"draa","title":"#Delta R (#gamma_{1},#gamma_{2})","bin":50,"xmin":0.0,"xmax":6.00},
    "drbb":{"name":"drbb","title":"#Delta R (b_{1},b_{2})","bin":50,"xmin":0.0,"xmax":6.00},
}

for kl in kl_list:
    variables["tmva_bdt_qcd_{}".format(kl)] = {"name":"tmva_bdt_qcd_{}".format(kl),"title":"BDT_{QCD}","bin":50,"xmin":-1,"xmax":1.}
    variables["tmva_bdt_singleh_{}".format(kl)] = {"name":"tmva_bdt_singleh_{}".format(kl),"title":"BDT_{QCD}","bin":50,"xmin":-1,"xmax":1.}


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


for kl in kl_list:
    variables2D["bdth_bdtqcd_{}".format(kl)] = { 
                  "namex":"tmva_bdt_singleh_{}".format(kl),"namey":"tmva_bdt_qcd_{}".format(kl),"titlex":"BDT_{H}","titley":"BDT_{QCD}",
                  "binx":50,"xmin":-1.0,"xmax":1.0,"biny":50,"ymin":-1.0,"ymax":1.0
               }


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

colors = {}
for k in kls:
    signal_str='HH(#kappa_{{#lambda}}={:.2f})'.format(k)
    colors[signal_str] = ROOT.kBlue+3


#colors['j#gamma + Jets'] = ROOT.kAzure+1
#colors['#gamma#gamma + Jets'] = ROOT.kCyan-8
#colors['ttH'] = ROOT.kViolet-4
#colors['ggH'] = ROOT.kGreen-2
#colors['ggH2'] = ROOT.kGreen-5
#colors['VH'] = ROOT.kOrange-1

colors['single Higgs'] = ROOT.kViolet-4
colors['j#gamma + Jets'] = ROOT.kAzure+1
colors['#gamma#gamma + Jets'] = ROOT.kCyan-8
colors['H'] = ROOT.kViolet-4

signal_groups = collections.OrderedDict()
for k in kls:
    signal_str='HH(#kappa_{{#lambda}}={:.2f})'.format(k)
    lambda_str='lambda{:03d}_5f'.format(int(k*100))
    signal_groups[signal_str] = ['pwp8_pp_hh_{}_hhbbaa'.format(lambda_str), 'mgp8_pp_vbfhh_{}_hhbbaa'.format(lambda_str), 'mgp8_pp_tthh_{}_hhbbaa'.format(lambda_str), 'mgp8_pp_vhh_{}_hhbbaa'.format(lambda_str)]
    #signal_groups[signal_str] = ['pwp8_pp_hh_{}_hhbbaa'.format(lambda_str)]


background_groups = collections.OrderedDict()



#FIXME: missing all QCD backgrounds
background_groups['#gamma#gamma + Jets'] = ['mgp8_pp_jjaa_5f']
background_groups['j#gamma + Jets'] = ['mgp8_pp_jjja_5f']

#FIXME: missing 'mgp8_pp_vh012j_5f', 'mgp8_pp_vbf_h01j_5f','mgp8_pp_tth01j_5f_haa',
background_groups['single Higgs'] = ['mgp8_pp_vh012j_5f_haa', 'mgp8_pp_vbf_h01j_5f_haa','mgp8_pp_tth01j_5f_haa','mgp8_pp_h012j_5f_haa']
#background_groups['single Higgs'] = ['mgp8_pp_tth01j_5f_haa']


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

tthcut = ' && nlep == 0 && nljets < 4 && met_pt < 100 && draa < 3.0 && drbb < 2.5  && drbb > 0.6'
mcut = ' && abs(haa_m - 125.) < 50 && hbb_m > 80. && hbb_m < 140.'
mbbcut = ' && hbb_m > 100. && hbb_m < 130.'
maacut = ' && abs(haa_m - 125.) < 2.5 '
#yrcut = ' && a1_pt > 60. && b1_pt > 60. && a2_pt > 30. && b2_pt > 30. && haa_pt > 100. && hbb_pt > 100. && nlep == 0'
yrcut = ' && a1_pt > 60. && b1_pt > 60. && a2_pt > 30. && b2_pt > 30. && haa_pt > 125. && hbb_pt > 125. && nlep == 0 && drbb < 2.0 &&  draa < 1.75'


selection_yr  = []
selection_cms = []
selection_new = []

selection  = []

sel0  = 'abs(b1_eta) < 6.0 && abs(b2_eta) < 6.0 && '
sel0 += 'abs(a1_eta) < 6.0 && abs(a2_eta) < 6.0 && '
sel0 += 'a1_pt > 35. && b1_pt > 35. && '
sel0 += 'a2_pt > 30. && b2_pt > 30. && '
sel0 += 'haa_m > 100. && haa_m < 150. && '
sel0 += 'hbb_m > 60. && hbb_m < 200.'

sel0 += ' && haa_m > 118. && haa_m < 132. '

sel0 += ' && abs(b1_eta) < 4.0 && abs(b2_eta) < 4.0'
sel0 += ' && abs(a1_eta) < 4.0 && abs(a2_eta) < 4.0'

'''
sel1 = sel0
sel1 += ' && a1_pt > 40. && b1_pt > 40.'
sel1 += ' && a2_pt > 40. && b2_pt > 40.'

sel2 = sel1
sel2 += ' && a1_pt > 50. && b1_pt > 50.'
sel2 += ' && a2_pt > 50. && b2_pt > 50.'

sel3 = sel2
sel3 += ' && a1_pt > 60. && b1_pt > 60.'
sel3 += ' && a2_pt > 60. && b2_pt > 60.'
'''
sel1 = sel0
sel1 += ' && tmva_bdt_singleh > -0.1 && tmva_bdt_qcd > 0.1'

sel2 = sel0
sel2 += ' && tmva_bdt_singleh > -0.0 && tmva_bdt_qcd > 0.2'

sel3 = sel0
sel3 += ' && tmva_bdt_singleh > 0.1 && tmva_bdt_qcd > 0.3'

sel4 = sel0
sel4 += ' && tmva_bdt_singleh > 0.2 && tmva_bdt_qcd > 0.4'

'''
sel5 = sel1
sel5 += ' && tmva_bdt_singleh > 0.1 && tmva_bdt_qcd > 0.4'

sel6 = sel2
sel6 += ' && tmva_bdt_singleh > 0.1 && tmva_bdt_qcd > 0.4'

sel7 = sel3
sel7 += ' && tmva_bdt_singleh > 0.1 && tmva_bdt_qcd > 0.4'
'''

selection.append(sel0)

#selection.append(sel1)
#selection.append(sel2)
#selection.append(sel3)
#selection.append(sel4)
'''
selection.append(sel5)
selection.append(sel6)
selection.append(sel7)
'''
'''
#for i in range(40):
#for i in range(1):
   bdth = 0.1 + i*0.01
   #bdtq = 0.2 + i*0.025

   bdtq = 0.4 + i*0.01

   
   bdtstr = ' && tmva_bdt_singleh > {} && tmva_bdt_qcd > {}'.format(bdth,bdtq)
   #bdtstr = ' && tmva_bdt_qcd > {}'.format(bdtq)

   selection.append(sel0 + bdtstr)
'''
'''

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


'''
for sel in selection_yr:
    for k in kls:    
        signal_str='HH(#kappa_{{#lambda}}={:.2f})'.format(k)
        selections[signal_str].append(sel)

for sel in selection_cms:
    for k in kls:    
        signal_str='HH(#kappa_{{#lambda}}={:.2f})'.format(k)
        selections[signal_str].append(sel)

for sel in selection_new:
    for k in kls:    
        signal_str='HH(#kappa_{{#lambda}}={:.2f})'.format(k)
        selections[signal_str].append(sel)
'''
