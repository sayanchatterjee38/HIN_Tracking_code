***To setup the code, please, follow:***

ssh -XY caber@lxplus8.cern.ch

export SCRAM_ARCH=el8_amd64_gcc11

voms-proxy-init -voms cms

cmsrel CMSSW_13_2_4

cd CMSSW_13_2_4/src

cmsenv

git clone -b CMSSW_13_2_X_trkAnalysis git@github.com:CesarBernardes/TrackingCode.git .

scram b -j 8

To prepare the trees and histograms for performance plots, please, use:

HITrackingStudies/HITrackingStudies/test/run_PbPb_cfg.py

For control plots, see macros:

HITrackingStudies/HITrackingStudies/test/plottingMacro/macro_control_plots_XXX.C

For efficiency and fake rate use:

HITrackingStudies/HITrackingStudies/test/plottingMacro/plotHistXXX.C


***Very Important*** The configurations below (for full reco) are not suitable for 13_2_X MC. They can serve as examples, but are not the latest settings

1) For generating samples:
code comes from cms driver commands similar as described here:
https://twiki.cern.ch/twiki/bin/viewauth/CMS/HIRunPreparations2021HLT#Simulations

GENSIM step:

Config to b=12 events (cFlag=0) (peripheral)
You can easily get heavy (central) events by changing bFixed to 4 for example (b=4fm evts)
For MinBias (defaults), set cFlag=1 (overwrites bFixed parameter above)

cmsRun Hydjet_Quenched_MB_5020GeV_cfi_GEN_SIM.py

DIGI RAW:

cmsRun step2_DIGI_L1_DIGI2RAW_HLT_PU.py



2) Running Reconstruction (works on output of step 1 OR official MC.  If you want to test performance, the input MC MUST BE RAWDEBUG OR Full Event Content)

RECO:

Defaults to RECODEBUG event content.  If you want to check event sizes, etc. you need to change the output module data type to AODSIM or MINIAOD.  The timing information is stored to out.txt.  If you do not want timing info, you can omit everything after '.py'.

cmsRun step3_RAW2DIGI_L1Reco_RECO.py > out.txt 2>&1 &


We added also a config "step3_RAW2DIGI_L1Reco_RECO_MINIAOD.py" to produce a MINIAOD format with output with detailed timing information to use 
in the procedure below. Please, see the special lines at the very end of the configuration.



3) Checking timing

code written by Cheng-Chieh Peng

Copy out.txt into the Timing directory, and then run Timing/timeRecord.sh:

cp out.txt Timing/; cd Timing; ./timeRecord.sh

A timing summary can then be found in Timing/TimingModule.txt



4) Making performance tree and hit matched collections (this last for recodebug only)

Standard tracking group efficiency code + HIForest-style tree for debugging

navigate to the analyzer directory:

cd HITrackingStudies/test/

edit run_PbPb_cfg.py to get the settings you want (the cuts are the most relevant thing here)

One example:

cmsRun run_PbPb_cfg.py sample="Data_Reco_AOD" n=100 runOverStreams=False >& OutPut.txt &

Output file is trk.root



5) Plotting efficiency/fake

In the 'plottingMacro' directory from the above path:

root -l -b -q plotHist2D.C

Output plots will be in the 'files' directory. And TGraphs in "test.root" file


6) For doing control plots run

root -l -b -q macro_control_plots_OneSample.C

root -l -b -q macro_control_plots_signal_vs_fake_MCrecodebugOnly.C

root -l -b -q macro_control_plots_TwoSamples.C

root -l -b -q macro_control_plots_ThreeSamples.C


