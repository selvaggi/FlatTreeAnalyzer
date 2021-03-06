import ROOT
import collections

### variable list
variables = {

        'Jet1_pf04_pt':{'name':'Jet1_pf04_pt','title':'Jet1 p_{T} [TeV]','bin':115,'xmin':2,'xmax':25, 'divide':1000},
        'Jet1_pf04_eta':{'name':'Jet1_pf04_eta','title':'Jet1 #eta','bin':50,'xmin':-5.0,'xmax':5.0},

        'Jet2_pf04_pt':{'name':'Jet2_pf04_pt','title':'Jet2 p_{T} [TeV]','bin':115,'xmin':2,'xmax':25, 'divide':1000},
        'Jet2_pf04_eta':{'name':'Jet2_pf04_eta','title':'Jet2 #eta','bin':50,'xmin':-5.0,'xmax':5.0},

        'Jet1_calo04_pt':{'name':'Jet1_calo04_pt','title':'Jet1 p_{T} [TeV]','bin':115,'xmin':2,'xmax':25, 'divide':1000},
        'Jet1_calo04_eta':{'name':'Jet1_calo04_eta','title':'Jet1 #eta','bin':50,'xmin':-5.0,'xmax':5.0},

        'Jet2_calo04_pt':{'name':'Jet2_calo04_pt','title':'Jet2 p_{T} [TeV]','bin':115,'xmin':2,'xmax':25, 'divide':1000},
        'Jet2_calo04_eta':{'name':'Jet2_calo04_eta','title':'Jet2 #eta','bin':50,'xmin':-5.0,'xmax':5.0},


        'rapiditySeparation_pf04':{'name':'rapiditySeparation_pf04','title':'Rapidity Separation','bin':50,'xmin':0.0,'xmax':10.0},
        'transverseMomentumAsymmetry_pf_04':{'name':'transverseMomentumAsymmetry_pf04','title':'Transverse Momentum Asymmetry','bin':50,'xmin':0.0,'xmax':1.0},

        'Mj1j2_pf04' :{'name':'Mj1j2_pf04','title':'m_{Z\'} [TeV] (pf04)','bin':200,'xmin':10.0,'xmax':50.0, 'divide':1000},
        'Mj1j2_calo04' :{'name':'Mj1j2_calo04','title':'m_{Z\'} [TeV] (calo04)','bin':200,'xmin':10.0,'xmax':50.0, 'divide':1000},

}

variables2D = {}


colors = {}
colors['m_{Q*} = 10 TeV'] = ROOT.kRed
colors['m_{Q*} = 15 TeV'] = ROOT.kRed
colors['m_{Q*} = 20 TeV'] = ROOT.kRed
colors['m_{Q*} = 25 TeV'] = ROOT.kRed
colors['m_{Q*} = 30 TeV'] = ROOT.kRed
colors['m_{Q*} = 35 TeV'] = ROOT.kRed
colors['m_{Q*} = 40 TeV'] = ROOT.kRed
colors['m_{Q*} = 45 TeV'] = ROOT.kRed
colors['m_{Q*} = 50 TeV'] = ROOT.kRed
colors['QCD'] = ROOT.kGreen+2

signal_groups = collections.OrderedDict()

signal_groups['m_{Q*} = 15 TeV'] = ['pp_ExcitedQ_15TeV_qq']
signal_groups['m_{Q*} = 20 TeV'] = ['pp_ExcitedQ_20TeV_qq']
signal_groups['m_{Q*} = 25 TeV'] = ['pp_ExcitedQ_25TeV_qq']
signal_groups['m_{Q*} = 30 TeV'] = ['pp_ExcitedQ_30TeV_qq']
signal_groups['m_{Q*} = 35 TeV'] = ['pp_ExcitedQ_35TeV_qq']
signal_groups['m_{Q*} = 40 TeV'] = ['pp_ExcitedQ_40TeV_qq']
signal_groups['m_{Q*} = 45 TeV'] = ['pp_ExcitedQ_45TeV_qq']
signal_groups['m_{Q*} = 50 TeV'] = ['pp_ExcitedQ_50TeV_qq']

background_groups = collections.OrderedDict()

background_groups['QCD'] = ['pp_jj_lo']



# global parameters
intLumi = 3.0e+07
delphesVersion = '3.4.2'

uncertainties = []
uncertainties.append([0., 0.])
uncertainties.append([0.02, 0.0])
uncertainties.append([0.02, 0.02])
uncertainties.append([0.02, 0.10])

# the first time needs to be set to True
runFull = True

# base pre-#selections
selbase = 'Jet1_calo04_pt > 3000. && Jet2_calo04_pt > 3000.'

selections = collections.OrderedDict()
selections['m_{Q*} = 15 TeV'] = []
selections['m_{Q*} = 15 TeV'].append(selbase)

selections['m_{Q*} = 20 TeV'] = []
selections['m_{Q*} = 20 TeV'].append(selbase)

selections['m_{Q*} = 25 TeV'] = []
selections['m_{Q*} = 25 TeV'].append(selbase)

selections['m_{Q*} = 30 TeV'] = []
selections['m_{Q*} = 30 TeV'].append(selbase)

selections['m_{Q*} = 35 TeV'] = []
selections['m_{Q*} = 35 TeV'].append(selbase)

selections['m_{Q*} = 40 TeV'] = []
selections['m_{Q*} = 40 TeV'].append(selbase)

selections['m_{Q*} = 45 TeV'] = []
selections['m_{Q*} = 45 TeV'].append(selbase)

selections['m_{Q*} = 50 TeV'] = []
selections['m_{Q*} = 50 TeV'].append(selbase)







