FlatTreeAnalyzer
================
This scripts allows to easily design an analysis based on produced flat trees with the [Heppy](https://github.com/HEP-FCC/heppy) framework.


Table of contents
=================
  * [FlatTreeAnalyzer](#flattreeanalyser)
  * [Table of contents](#table-of-contents)
  * [Clone and initialisation](#clone-and-initilisation)
 

Clone and initialisation
========================

If you do not attempt to contribute to the FCChhAnalyses repository, simply clone it:
```
git clone git@github.com:FCC-hh-framework/FlatTreeAnalyzer.git
```

If you aim at contributing to the heppy repository, you need to fork and then clone the forked repository:
```
git clone git@github.com:YOURGITUSERNAME/FlatTreeAnalyzer.git
```

then initialize:

```
source ./init.sh
```

Analyses are run the following way:
```
./bin/analyze.py -n [analysis_name_in_heppy] -c [heppy_cfg] -t [heppy_tree_location] -o [output_dir] -p [analysis_parameters] -j [proc_dict]
```

```
python bin/analyze.py -n hhbbaa -c ../../../FCCSW/heppy/FCChhAnalyses/FCChh/hhbbaa/analysis.py -t /eos/cms/store/cmst3/user/selvaggi/heppyTrees/hhbbaa/ -p templates/FCC/hhbbaa.py -j /afs/cern.ch/work/h/helsens/public/FCCDicts/FCC_procDict_fcc_v03.json -o hhbbaa --force --nev 50000 -m
```
To run with multi-threads, simply add "-m" to the execution line


condor submission
=================

It is also possible to send one lxbatch job per signal hypothesis. Each signal hypothesis will then run on a separate node
(multi-threading on that node is allowed). For instance:


```
python bin/analyze.py -n hhbbaa -c ../../../FCCSW/heppy/FCChhAnalyses/FCChh/hhbbaa/analysis.py -t /eos/cms/store/cmst3/user/selvaggi/heppyTrees/hhbbaa_v5/ -p templates/FCC/hhbbaa.py -j /afs/cern.ch/work/h/helsens/public/FCCDicts/FCC_procDict_fcc_v03.json -o hhbbaa -m  --condor --queue tomorrow
```

In order to collect jobs when running is over re-run the exact same command. 
If some jobs has failed, the script will automatically re-submit them.
When all jobs are completed, they will be collected and stored in the output directory specified by the ```-o``` option,
and the yield tables and final plots will be produced.

