###For a description of the crabConfig.py parameters. See:
###https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile

import CRABClient
from WMCore.Configuration import Configuration
config = Configuration() ###create a Configuration object

config.section_('General')###add a new section of type "General"
###General: In this section, the user specifies generic parameters about the request (e.g. request name).
config.General.workArea     = 'GeneralTracksEffTables_Projects' ###fixed name for projects dir in my area

#config.General.requestName  = 'preliminary2018Cuts_effTables_generalTracks_DefaultSelection' #sub dir with prefix "crab_". Change it for each task
#config.General.requestName  = 'preliminary2018Cuts_effTables_generalTracks_TightSelection'
config.General.requestName  = 'preliminary2018Cuts_effTables_generalTracks_LooseSelection'


config.General.transferLogs = True 
config.General.transferOutputs = True

################################

config.section_('JobType')###add a new section of type "JobType"
###JobType: This section aims to contain all the parameters of the user job type and 
###related configurables (e.g. CMSSW parameter-set configuration file, additional input files, etc.).
config.JobType.pluginName     = 'Analysis'
config.JobType.psetName       = 'run_PbPb_cfg.py'

#config.JobType.allowNonProductionCMSSW = True
#config.JobType.maxMemoryMB    = 2500

#config.JobType.inputFiles     = ['']##put new selections here
config.JobType.inputFiles = ['../cfg/CentralityTable_HFtowers200_DataPbPb_periHYDJETshape_run3v1302x04_offline_374289.db']
################################

config.section_('Data')###add a new section of type "Data"
###Data: This section contains all the parameters related to the data to be analyzed, 
###including the splitting parameters.
config.Data.inputDataset      = '/Hydjet_5360GeV_GEN_SIM/subehera-MB_Hydjet_Run3_recodebug_step4-625ffd2ccfcbfe30cf75ced0ae60f7d8/USER'
config.Data.splitting         = 'FileBased'
#config.Data.unitsPerJob       = X ###files per job (but not impose)
#config.Data.totalUnits        = Y ###how many files to analyze
config.Data.unitsPerJob       = 10
config.Data.totalUnits        = 949
config.Data.inputDBS          = 'phys03'
#config.Data.inputDBS          = 'global'
#config.Data.publishDBS = 'phys03'
#config.Data.publishDataName = 'TestingJobs_RecoWithNewPixelTracks'
#config.Data.outputDatasetTag = 'HBTAnalysispp13TeV_MC_Test01' ###change for each sample(task) --only if publish

#config.Data.outLFN            = '/store/user/caber/TESTJOBS_RecoWithNewPixelTracks'

#config.Data.outLFNDirBase            = '/store/user/caber/EventSizeSubDetectors_FlowCorrDataset'
config.Data.outLFNDirBase            = '/store/group/phys_heavyions/caber/TrackingEffTables2022PbPbRun'


################################

config.section_('Site')###add a new section of type "Site"
###Site: Grid site parameters are defined in this section, including the stage out information 
###(e.g. stage out destination site, white/black lists, etc.).
###config.Site.storageSite       = 'T2_BR_SPRACE'
config.Site.storageSite       = 'T2_CH_CERN'
#config.Site.whitelist         = ['T2_US_MIT']
