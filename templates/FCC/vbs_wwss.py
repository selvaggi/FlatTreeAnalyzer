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

wlwl_label = 'W_{L}^{#pm} W_{L}^{#pm} j j, (SM)'
wtwl_label = 'W_{T}^{#pm} W_{L}^{#pm} j j'
wtwt_label = 'W_{T}^{#pm} W_{T}^{#pm} j j'


colors = {}

#kappas = ['090', '095', '098', '100', '102', '105', '110']
#kappas = ['090','100', '110']
#kappas = ['050', '090', '100', '110', '130', '150']
#kappas = ['050', '070','080','090', '095', '100', '102', '105', '110','120','130', '150']
kappas = ['090', '100', '110']
#kappas = ['105']
#kappas = ['110']

ww_label = 'W^{#pm} W^{#pm} j j'
sig_labels = dict()


for k in kappas:
   sig_labels[k]=ww_label + ' ' + k
   colors[sig_labels[k]] = ROOT.kRed

colors['WZ'] = ROOT.kBlue-7
colors['WW(TT,TL)'] = ROOT.kViolet

signal_groups = collections.OrderedDict()

for k in kappas:
    signal_groups[sig_labels[k]] = ['mgp8_pp_vbs_wwss_kw_{}_LL'.format(k)]

background_groups = collections.OrderedDict()
'''
background_groups[wtwl_label] = ['mgp8_pp_vbs_wwss_kw_100_TL']
background_groups[wtwt_label] = ['mgp8_pp_vbs_wwss_kw_100_TT']
'''
background_groups['WZ']         = ['mgp8_pp_wz012j_4f_wzlllv']
background_groups['WW(TT,TL)']  = ['mgp8_pp_vbs_wwss_kw_100_TL','mgp8_pp_vbs_wwss_kw_100_TT']

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
wz_cuts = vbs_cuts + '&& mll > 50. && met_pt > 50.'
vlvl_cuts = wz_cuts + '&& dphill < 2. && dphijj > 2.'
#vlvl_cuts = wz_cuts 

selection  = []
selection.append( 'mjj > 0.' )


'''
selection.append(presel)
selection.append(vbs_cuts)
selection.append(wz_cuts)
'''

selection.append(vlvl_cuts)

# add mass-dependent list of event selections here if needed...

selections = collections.OrderedDict()
for k in kappas:
    #selections[sig_labels[k]] = selection

    selections[sig_labels[k]] = []
    print sig_labels[k]
    #for i in range(1):
    for i in range(21):
       m = 0. + i*100.
       mstr = ' && mll > {}'.format(m)
       selections[sig_labels[k]].append(vlvl_cuts + mstr)
    
    '''selections[sig_labels[k]] = []
    print sig_labels[k]
    #for i in range(1):
    for i in range(2):
       m = 0. + i*100.
       mstr = ' && mt > {}'.format(m)
       print 
       selections[sig_labels[k]].append(vlvl_cuts + mstr)'''
