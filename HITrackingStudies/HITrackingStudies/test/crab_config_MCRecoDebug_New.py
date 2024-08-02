from CRABClient.UserUtilities import config
config = config()

config.General.workArea        = 'TrackingStudies_Run3'
config.General.requestName     = 'GeneralTracks_MCRecodebug_HITrackingCorrection_Cent0_10_nhits0_noptResCut'
config.General.transferLogs    = False 
config.General.transferOutputs = True
################################

config.JobType.pluginName      = 'Analysis'
config.JobType.psetName        = 'run_PbPb_cfg_MCRecoDebug.py'
#config.JobType.inputFiles      = ['CentralityTable_HFtowers200_HydjetDrum5F_v1302x04_RECODEBUG_MC2023.db']
config.JobType.inputFiles      = ['CentralityTable_HFtowers200_DataPbPb_periHYDJETshape_run3v1302x04_offline_Nominal.db']
################################

config.Data.inputDataset       = '/MinBias_PbPb_5p36TeV_Hydjet_v1/sarteaga-MinBias_PbPb_5p36TeV_Hydjet_RECODEBUG_v5-0e6c11377ba727d4466887a72ad361ed/USER'
config.Data.splitting          = 'FileBased'
config.Data.unitsPerJob        = 40
config.Data.totalUnits         = 1000
config.Data.publication        = False
config.Data.inputDBS           = 'phys03'
config.Data.outLFNDirBase      = '/store/group/phys_heavyions/rpradhan/TrackingEffTables2022PbPbRun'
#config.Data.outLFNDirBase      = '/store/user/rpradhan/Research/Tracking_Studies'
config.Data.outputDatasetTag   = 'GeneralTracks_MCRecodebug_HITrackingCorrection_Cent0_10_nhits0_noptResCut'
################################

config.Site.storageSite        = 'T2_CH_CERN'
#config.Site.storageSite        = 'T3_CH_CERNBOX'
#config.Site.storageSite        = 'T2_IN_TIFR'

