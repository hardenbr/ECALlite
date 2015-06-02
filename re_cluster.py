# /users/hardenbr/pizero_stream/pizero_stream_lowpu_fix1/V4 (CMSSW_7_4_3)

import FWCore.ParameterSet.Config as cms
debug_level_recluster = 0
debug_level           = 0
process               = cms.Process( "TEST" )
process.load('setup_cff')

process.HLTConfigVersion = cms.PSet(
  tableName = cms.string('/users/hardenbr/pizero_stream/pizero_stream_lowpu_fix1/V4')
)

process.streams = cms.PSet(  ALCAP0 = cms.vstring( 'AlCaP0' ) )
process.datasets = cms.PSet(  AlCaP0 = cms.vstring( 'AlCa_EcalEtaEBonly_LowPU_v1',
  'AlCa_EcalEtaEEonly_LowPU_v1',
  'AlCa_EcalPi0EBonly_LowPU_v1',
  'AlCa_EcalPi0EEonly_LowPU_v1' ) )

process.hltGetConditions = cms.EDAnalyzer( "EventSetupRecordDataGetter",
    toGet = cms.VPSet( 
    ),
    verbose = cms.untracked.bool( False )
)
process.hltGetRaw = cms.EDAnalyzer( "HLTGetRaw",
    RawDataCollection = cms.InputTag( "rawDataCollector" )
)
process.hltBoolFalse = cms.EDFilter( "HLTBool",
    result = cms.bool( False )
)
process.hltTriggerType = cms.EDFilter( "HLTTriggerTypeFilter",
    SelectedTriggerType = cms.int32( 1 )
)
process.hltGtDigis = cms.EDProducer( "L1GlobalTriggerRawToDigi",
    DaqGtFedId = cms.untracked.int32( 813 ),
    Verbosity = cms.untracked.int32( 0 ),
    UnpackBxInEvent = cms.int32( 5 ),
    ActiveBoardsMask = cms.uint32( 0xffff ),
    DaqGtInputTag = cms.InputTag( "rawDataCollector" )
)
process.hltGctDigis = cms.EDProducer( "GctRawToDigi",
    checkHeaders = cms.untracked.bool( False ),
    unpackSharedRegions = cms.bool( False ),
    numberOfGctSamplesToUnpack = cms.uint32( 1 ),
    verbose = cms.untracked.bool( False ),
    numberOfRctSamplesToUnpack = cms.uint32( 1 ),
    inputLabel = cms.InputTag( "rawDataCollector" ),
    unpackerVersion = cms.uint32( 0 ),
    gctFedId = cms.untracked.int32( 745 ),
    hltMode = cms.bool( True )
)
process.hltL1GtObjectMap = cms.EDProducer( "L1GlobalTrigger",
    TechnicalTriggersUnprescaled = cms.bool( True ),
    ProduceL1GtObjectMapRecord = cms.bool( True ),
    AlgorithmTriggersUnmasked = cms.bool( False ),
    EmulateBxInEvent = cms.int32( 1 ),
    AlgorithmTriggersUnprescaled = cms.bool( True ),
    ProduceL1GtDaqRecord = cms.bool( False ),
    ReadTechnicalTriggerRecords = cms.bool( True ),
    RecordLength = cms.vint32( 3, 0 ),
    TechnicalTriggersUnmasked = cms.bool( False ),
    ProduceL1GtEvmRecord = cms.bool( False ),
    GmtInputTag = cms.InputTag( "hltGtDigis" ),
    TechnicalTriggersVetoUnmasked = cms.bool( True ),
    AlternativeNrBxBoardEvm = cms.uint32( 0 ),
    TechnicalTriggersInputTags = cms.VInputTag( 'simBscDigis' ),
    CastorInputTag = cms.InputTag( "castorL1Digis" ),
    GctInputTag = cms.InputTag( "hltGctDigis" ),
    AlternativeNrBxBoardDaq = cms.uint32( 0 ),
    WritePsbL1GtDaqRecord = cms.bool( False ),
    BstLengthBytes = cms.int32( -1 )
)
process.hltL1extraParticles = cms.EDProducer( "L1ExtraParticlesProd",
    tauJetSource = cms.InputTag( 'hltGctDigis','tauJets' ),
    etHadSource = cms.InputTag( "hltGctDigis" ),
    isoTauJetSource = cms.InputTag( 'hltGctDigis','isoTauJets' ),
    etTotalSource = cms.InputTag( "hltGctDigis" ),
    centralBxOnly = cms.bool( True ),
    centralJetSource = cms.InputTag( 'hltGctDigis','cenJets' ),
    etMissSource = cms.InputTag( "hltGctDigis" ),
    hfRingEtSumsSource = cms.InputTag( "hltGctDigis" ),
    produceMuonParticles = cms.bool( True ),
    forwardJetSource = cms.InputTag( 'hltGctDigis','forJets' ),
    ignoreHtMiss = cms.bool( False ),
    htMissSource = cms.InputTag( "hltGctDigis" ),
    produceCaloParticles = cms.bool( True ),
    muonSource = cms.InputTag( "hltGtDigis" ),
    isolatedEmSource = cms.InputTag( 'hltGctDigis','isoEm' ),
    nonIsolatedEmSource = cms.InputTag( 'hltGctDigis','nonIsoEm' ),
    hfRingBitCountsSource = cms.InputTag( "hltGctDigis" )
)
process.hltScalersRawToDigi = cms.EDProducer( "ScalersRawToDigi",
    scalersInputTag = cms.InputTag( "rawDataCollector" )
)
process.hltOnlineBeamSpot = cms.EDProducer( "BeamSpotOnlineProducer",
    maxZ = cms.double( 40.0 ),
    src = cms.InputTag( "hltScalersRawToDigi" ),
    gtEvmLabel = cms.InputTag( "" ),
    changeToCMSCoordinates = cms.bool( False ),
    setSigmaZ = cms.double( 0.0 ),
    maxRadius = cms.double( 2.0 )
)
process.hltPreAlCaEcalPi0EBonlyLowPU = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltL1sAlCaEcalPi0EtaLowPU = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleJet12_BptxAND OR L1_SingleJet16 OR L1_SingleEG5 OR L1_DoubleJet20 OR L1_SingleJet20 OR L1_SingleJet36" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltEcalDigis = cms.EDProducer( "EcalRawToDigi",
    orderedDCCIdList = cms.vint32( 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54 ),
    FedLabel = cms.InputTag( "listfeds" ),
    eventPut = cms.bool( True ),
    srpUnpacking = cms.bool( True ),
    syncCheck = cms.bool( True ),
    headerUnpacking = cms.bool( True ),
    feUnpacking = cms.bool( True ),
    orderedFedList = cms.vint32( 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654 ),
    tccUnpacking = cms.bool( True ),
    numbTriggerTSamples = cms.int32( 1 ),
    InputLabel = cms.InputTag( "rawDataCollector" ),
    numbXtalTSamples = cms.int32( 10 ),
    feIdCheck = cms.bool( True ),
    FEDs = cms.vint32( 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654 ),
    silentMode = cms.untracked.bool( True ),
    DoRegional = cms.bool( False ),
    forceToKeepFRData = cms.bool( False ),
    memUnpacking = cms.bool( True )
)
process.hltEcalPreshowerDigis = cms.EDProducer( "ESRawToDigi",
    sourceTag = cms.InputTag( "rawDataCollector" ),
    debugMode = cms.untracked.bool( False ),
    InstanceES = cms.string( "" ),
    ESdigiCollection = cms.string( "" ),
    LookupTable = cms.FileInPath( "EventFilter/ESDigiToRaw/data/ES_lookup_table.dat" )
)
process.hltEcalUncalibRecHit = cms.EDProducer( "EcalUncalibRecHitProducer",
    EEdigiCollection = cms.InputTag( 'hltEcalDigis','eeDigis' ),
    EBdigiCollection = cms.InputTag( 'hltEcalDigis','ebDigis' ),
    EEhitCollection = cms.string( "EcalUncalibRecHitsEE" ),
    EBhitCollection = cms.string( "EcalUncalibRecHitsEB" ),
    algo = cms.string( "EcalUncalibRecHitWorkerWeights" ),
    algoPSet = cms.PSet(  )
)
process.hltEcalDetIdToBeRecovered = cms.EDProducer( "EcalDetIdToBeRecoveredProducer",
    ebIntegrityChIdErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityChIdErrors' ),
    ebDetIdToBeRecovered = cms.string( "ebDetId" ),
    integrityTTIdErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityTTIdErrors' ),
    eeIntegrityGainErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityGainErrors' ),
    ebFEToBeRecovered = cms.string( "ebFE" ),
    ebIntegrityGainErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityGainErrors' ),
    eeDetIdToBeRecovered = cms.string( "eeDetId" ),
    eeIntegrityGainSwitchErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityGainSwitchErrors' ),
    eeIntegrityChIdErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityChIdErrors' ),
    ebIntegrityGainSwitchErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityGainSwitchErrors' ),
    ebSrFlagCollection = cms.InputTag( "hltEcalDigis" ),
    eeSrFlagCollection = cms.InputTag( "hltEcalDigis" ),
    integrityBlockSizeErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityBlockSizeErrors' ),
    eeFEToBeRecovered = cms.string( "eeFE" )
)
process.hltEcalRecHit = cms.EDProducer( "EcalRecHitProducer",
    recoverEEVFE = cms.bool( False ),
    EErechitCollection = cms.string( "EcalRecHitsEE" ),
    recoverEBIsolatedChannels = cms.bool( False ),
    recoverEBVFE = cms.bool( False ),
    laserCorrection = cms.bool( True ),
    EBLaserMIN = cms.double( 0.5 ),
    killDeadChannels = cms.bool( True ),
    dbStatusToBeExcludedEB = cms.vint32( 14, 78, 142 ),
    EEuncalibRecHitCollection = cms.InputTag( 'hltEcalUncalibRecHit','EcalUncalibRecHitsEE' ),
    EBLaserMAX = cms.double( 3.0 ),
    EELaserMIN = cms.double( 0.5 ),
    ebFEToBeRecovered = cms.InputTag( 'hltEcalDetIdToBeRecovered','ebFE' ),
    EELaserMAX = cms.double( 8.0 ),
    recoverEEIsolatedChannels = cms.bool( False ),
    eeDetIdToBeRecovered = cms.InputTag( 'hltEcalDetIdToBeRecovered','eeDetId' ),
    recoverEBFE = cms.bool( True ),
    algo = cms.string( "EcalRecHitWorkerSimple" ),
    ebDetIdToBeRecovered = cms.InputTag( 'hltEcalDetIdToBeRecovered','ebDetId' ),
    singleChannelRecoveryThreshold = cms.double( 8.0 ),
    ChannelStatusToBeExcluded = cms.vstring(  ),
    EBrechitCollection = cms.string( "EcalRecHitsEB" ),
    singleChannelRecoveryMethod = cms.string( "NeuralNetworks" ),
    recoverEEFE = cms.bool( True ),
    triggerPrimitiveDigiCollection = cms.InputTag( 'hltEcalDigis','EcalTriggerPrimitives' ),
    dbStatusToBeExcludedEE = cms.vint32( 14, 78, 142 ),
    flagsMapDBReco = cms.PSet( 
      kGood = cms.vstring( 'kOk',
        'kDAC',
        'kNoLaser',
        'kNoisy' ),
      kNeighboursRecovered = cms.vstring( 'kFixedG0',
        'kNonRespondingIsolated',
        'kDeadVFE' ),
      kDead = cms.vstring( 'kNoDataNoTP' ),
      kNoisy = cms.vstring( 'kNNoisy',
        'kFixedG6',
        'kFixedG1' ),
      kTowerRecovered = cms.vstring( 'kDeadFE' )
    ),
    EBuncalibRecHitCollection = cms.InputTag( 'hltEcalUncalibRecHit','EcalUncalibRecHitsEB' ),
    algoRecover = cms.string( "EcalRecHitWorkerRecover" ),
    eeFEToBeRecovered = cms.InputTag( 'hltEcalDetIdToBeRecovered','eeFE' ),
    cleaningConfig = cms.PSet( 
      e6e2thresh = cms.double( 0.04 ),
      tightenCrack_e6e2_double = cms.double( 3.0 ),
      e4e1Threshold_endcap = cms.double( 0.3 ),
      tightenCrack_e4e1_single = cms.double( 3.0 ),
      tightenCrack_e1_double = cms.double( 2.0 ),
      cThreshold_barrel = cms.double( 4.0 ),
      e4e1Threshold_barrel = cms.double( 0.08 ),
      tightenCrack_e1_single = cms.double( 2.0 ),
      e4e1_b_barrel = cms.double( -0.024 ),
      e4e1_a_barrel = cms.double( 0.04 ),
      ignoreOutOfTimeThresh = cms.double( 1.0E9 ),
      cThreshold_endcap = cms.double( 15.0 ),
      e4e1_b_endcap = cms.double( -0.0125 ),
      e4e1_a_endcap = cms.double( 0.02 ),
      cThreshold_double = cms.double( 10.0 )
    ),
    logWarningEtThreshold_EB_FE = cms.double( 50.0 ),
    logWarningEtThreshold_EE_FE = cms.double( 50.0 )
)
process.hltEcalPreshowerRecHit = cms.EDProducer( "ESRecHitProducer",
    ESRecoAlgo = cms.int32( 0 ),
    ESrechitCollection = cms.string( "EcalRecHitsES" ),
    algo = cms.string( "ESRecHitWorker" ),
    ESdigiCollection = cms.InputTag( "hltEcalPreshowerDigis" )
)

process.hltSimple3x3Clusters = cms.EDProducer( "EgammaHLTNxNClusterProducer",
    statusLevelRecHitsToUse = cms.int32( 1 ),
    barrelClusterCollection = cms.string( "Simple3x3ClustersBarrel" ),
    flagLevelRecHitsToUse = cms.int32( 1 ),
    maxNumberofClusters = cms.int32( 99999 ),
    clusPhiSize = cms.int32( 3 ),
    posCalcParameters = cms.PSet( 
      T0_barl = cms.double( 7.4 ),
      LogWeighted = cms.bool( True ),
      T0_endc = cms.double( 3.1 ),
      T0_endcPresh = cms.double( 1.2 ),
      W0 = cms.double( 4.2 ),
      X0 = cms.double( 0.89 )
    ),
    clusEtaSize = cms.int32( 3 ),
    useRecoFlag = cms.bool( False ),
    endcapHitProducer = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEE' ),
    maxNumberofSeeds = cms.int32( 99999 ),
    useDBStatus = cms.bool( True ),
    debugLevel = cms.int32( debug_level ),
    barrelHitProducer = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEB' ),
    clusSeedThrEndCap = cms.double( 1.0 ),
    clusSeedThr = cms.double( 0.5 ),
    doEndcaps = cms.bool( True ),
    endcapClusterCollection = cms.string( "Simple3x3ClustersEndcap" ),
    doBarrel = cms.bool( True )
)

process.hltAlCaPi0RecHitsFilterEBonlyRegional = cms.EDFilter( "HLTRegionalEcalResonanceFilter",
    barrelSelection = cms.PSet( 
      seleS4S9GammaBarrel_region1 = cms.double( 0.88 ),
      massLowPi0Cand = cms.double( 0.104 ),
      seleIsoBarrel_region2 = cms.double( 0.5 ),
      seleMinvMaxBarrel = cms.double( 0.22 ),
      seleIsoBarrel_region1 = cms.double( 0.5 ),
      seleMinvMinBarrel = cms.double( 0.06 ),
      selePtPairBarrel_region2 = cms.double( 1.75 ),
      seleS9S25Gamma = cms.double( 0.0 ),
      selePtPairBarrel_region1 = cms.double( 2.0 ),
      region1_Barrel = cms.double( 1.0 ),
      seleS4S9GammaBarrel_region2 = cms.double( 0.9 ),
      massHighPi0Cand = cms.double( 0.163 ),
      ptMinForIsolation = cms.double( 1.0 ),
      store5x5RecHitEB = cms.bool( False ),
      selePtGammaBarrel_region1 = cms.double( 0.65 ),
      seleBeltDeta = cms.double( 0.05 ),
      removePi0CandidatesForEta = cms.bool( False ),
      barrelHitCollection = cms.string( "pi0EcalRecHitsEB" ),
      selePtGammaBarrel_region2 = cms.double( 0.65 ),
      seleBeltDR = cms.double( 0.2 )
    ),
    statusLevelRecHitsToUse = cms.int32( 1 ),
    endcapHits = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEE' ),
    doSelBarrel = cms.bool( True ),
    flagLevelRecHitsToUse = cms.int32( 1 ),
    preshRecHitProducer = cms.InputTag( 'hltEcalPreshowerRecHit','EcalRecHitsES' ),
    doSelEndcap = cms.bool( False ),
    storeRecHitES = cms.bool( False ),
    endcapClusters = cms.InputTag( 'hltSimple3x3Clusters','Simple3x3ClustersEndcap' ),
    barrelHits = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEB' ),
    useRecoFlag = cms.bool( False ),
    barrelClusters = cms.InputTag( 'hltSimple3x3Clusters','Simple3x3ClustersBarrel' ),
    debugLevel = cms.int32( debug_level ),
    endcapSelection = cms.PSet( 
      seleS9S25GammaEndCap = cms.double( 0.0 ),
      seleBeltDREndCap = cms.double( 0.2 ),
      region1_EndCap = cms.double( 1.8 ),
      seleMinvMinEndCap = cms.double( 0.05 ),
      store5x5RecHitEE = cms.bool( False ),
      seleMinvMaxEndCap = cms.double( 0.3 ),
      selePtPairEndCap_region1 = cms.double( 1.5 ),
      selePtPairEndCap_region3 = cms.double( 99.0 ),
      selePtPairEndCap_region2 = cms.double( 1.5 ),
      selePtGammaEndCap_region3 = cms.double( 0.5 ),
      seleBeltDetaEndCap = cms.double( 0.05 ),
      seleIsoEndCap_region1 = cms.double( 0.5 ),
      region2_EndCap = cms.double( 2.0 ),
      seleS4S9GammaEndCap_region1 = cms.double( 0.65 ),
      seleS4S9GammaEndCap_region2 = cms.double( 0.65 ),
      seleS4S9GammaEndCap_region3 = cms.double( 0.65 ),
      selePtPairMaxEndCap_region3 = cms.double( 2.5 ),
      seleIsoEndCap_region2 = cms.double( 0.5 ),
      ptMinForIsolationEndCap = cms.double( 0.5 ),
      selePtGammaEndCap_region1 = cms.double( 0.5 ),
      seleIsoEndCap_region3 = cms.double( 0.5 ),
      selePtGammaEndCap_region2 = cms.double( 0.5 ),
      endcapHitCollection = cms.string( "pi0EcalRecHitsEE" )
    ),
    preshowerSelection = cms.PSet( 
      preshCalibGamma = cms.double( 0.024 ),
      preshStripEnergyCut = cms.double( 0.0 ),
      debugLevelES = cms.string( "" ),
      preshCalibPlaneY = cms.double( 0.7 ),
      preshCalibPlaneX = cms.double( 1.0 ),
      preshCalibMIP = cms.double( 9.0E-5 ),
      preshNclust = cms.int32( 4 ),
      ESCollection = cms.string( "pi0EcalRecHitsES" ),
      preshClusterEnergyCut = cms.double( 0.0 ),
      preshSeededNstrip = cms.int32( 15 )
    ),
    useDBStatus = cms.bool( True )
)
process.hltAlCaPi0EBUncalibrator = cms.EDProducer( "EcalRecalibRecHitProducer",
    doEnergyScale = cms.bool( False ),
    doLaserCorrectionsInverse = cms.bool( False ),
    EERecHitCollection = cms.InputTag( 'hltAlCaPi0RecHitsFilterEBonlyRegional','pi0EcalRecHitsEB' ),
    doEnergyScaleInverse = cms.bool( False ),
    EBRecHitCollection = cms.InputTag( 'hltAlCaPi0RecHitsFilterEBonlyRegional','pi0EcalRecHitsEB' ),
    doIntercalibInverse = cms.bool( False ),
    doLaserCorrections = cms.bool( False ),
    EBRecalibRecHitCollection = cms.string( "pi0EcalRecHitsEB" ),
    doIntercalib = cms.bool( False ),
    EERecalibRecHitCollection = cms.string( "pi0EcalRecHitsEE" )
)
process.hltAlCaPi0EBRechitsToDigis = cms.EDProducer( "HLTRechitsToDigis",
    digisIn = cms.InputTag( 'hltEcalDigis','ebDigis' ),
    recHits = cms.InputTag( 'hltAlCaPi0EBUncalibrator','pi0EcalRecHitsEB' ),
    digisOut = cms.string( "pi0EBDigis" ),
    region = cms.string( "barrel" )
)
process.hltBoolEnd = cms.EDFilter( "HLTBool",
    result = cms.bool( True )
)
process.hltPreAlCaEcalPi0EEonlyLowPU = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltAlCaPi0RecHitsFilterEEonlyRegional = cms.EDFilter( "HLTRegionalEcalResonanceFilter",
    barrelSelection = cms.PSet( 
      seleS4S9GammaBarrel_region1 = cms.double( 0.65 ),
      massLowPi0Cand = cms.double( 0.104 ),
      seleIsoBarrel_region2 = cms.double( 0.5 ),
      seleMinvMaxBarrel = cms.double( 0.22 ),
      seleIsoBarrel_region1 = cms.double( 0.5 ),
      seleMinvMinBarrel = cms.double( 0.06 ),
      selePtPairBarrel_region2 = cms.double( 1.5 ),
      seleS9S25Gamma = cms.double( 0.0 ),
      selePtPairBarrel_region1 = cms.double( 1.5 ),
      region1_Barrel = cms.double( 1.0 ),
      seleS4S9GammaBarrel_region2 = cms.double( 0.65 ),
      massHighPi0Cand = cms.double( 0.163 ),
      ptMinForIsolation = cms.double( 1.0 ),
      store5x5RecHitEB = cms.bool( False ),
      selePtGammaBarrel_region1 = cms.double( 0.5 ),
      seleBeltDeta = cms.double( 0.05 ),
      removePi0CandidatesForEta = cms.bool( False ),
      barrelHitCollection = cms.string( "pi0EcalRecHitsEB" ),
      selePtGammaBarrel_region2 = cms.double( 0.5 ),
      seleBeltDR = cms.double( 0.2 )
    ),
    statusLevelRecHitsToUse = cms.int32( 1 ),
    endcapHits = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEE' ),
    doSelBarrel = cms.bool( False ),
    flagLevelRecHitsToUse = cms.int32( 1 ),
    preshRecHitProducer = cms.InputTag( 'hltEcalPreshowerRecHit','EcalRecHitsES' ),
    doSelEndcap = cms.bool( True ),
    storeRecHitES = cms.bool( True ),
    endcapClusters = cms.InputTag( 'hltSimple3x3Clusters','Simple3x3ClustersEndcap' ),
    barrelHits = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEB' ),
    useRecoFlag = cms.bool( False ),
    barrelClusters = cms.InputTag( 'hltSimple3x3Clusters','Simple3x3ClustersBarrel' ),
    debugLevel = cms.int32( debug_level ),
    endcapSelection = cms.PSet( 
      seleS9S25GammaEndCap = cms.double( 0.0 ),
      seleBeltDREndCap = cms.double( 0.2 ),
      region1_EndCap = cms.double( 1.8 ),
      seleMinvMinEndCap = cms.double( 0.05 ),
      store5x5RecHitEE = cms.bool( False ),
      seleMinvMaxEndCap = cms.double( 0.3 ),
      selePtPairEndCap_region1 = cms.double( 2.5 ),
      selePtPairEndCap_region3 = cms.double( 2.0 ),
      selePtPairEndCap_region2 = cms.double( 2.0 ),
      selePtGammaEndCap_region3 = cms.double( 0.95 ),
      seleBeltDetaEndCap = cms.double( 0.05 ),
      seleIsoEndCap_region1 = cms.double( 0.5 ),
      region2_EndCap = cms.double( 2.0 ),
      seleS4S9GammaEndCap_region1 = cms.double( 0.85 ),
      seleS4S9GammaEndCap_region2 = cms.double( 0.92 ),
      seleS4S9GammaEndCap_region3 = cms.double( 0.92 ),
      selePtPairMaxEndCap_region3 = cms.double( 999.0 ),
      seleIsoEndCap_region2 = cms.double( 0.5 ),
      ptMinForIsolationEndCap = cms.double( 0.5 ),
      selePtGammaEndCap_region1 = cms.double( 0.8 ),
      seleIsoEndCap_region3 = cms.double( 0.5 ),
      selePtGammaEndCap_region2 = cms.double( 0.95 ),
      endcapHitCollection = cms.string( "pi0EcalRecHitsEE" )
    ),
    preshowerSelection = cms.PSet( 
      preshCalibGamma = cms.double( 0.024 ),
      preshStripEnergyCut = cms.double( 0.0 ),
      debugLevelES = cms.string( "" ),
      preshCalibPlaneY = cms.double( 0.7 ),
      preshCalibPlaneX = cms.double( 1.0 ),
      preshCalibMIP = cms.double( 9.0E-5 ),
      preshNclust = cms.int32( 4 ),
      ESCollection = cms.string( "pi0EcalRecHitsES" ),
      preshClusterEnergyCut = cms.double( 0.0 ),
      preshSeededNstrip = cms.int32( 15 )
    ),
    useDBStatus = cms.bool( True )
)
process.hltAlCaPi0EEUncalibrator = cms.EDProducer( "EcalRecalibRecHitProducer",
    doEnergyScale = cms.bool( False ),
    doLaserCorrectionsInverse = cms.bool( False ),
    EERecHitCollection = cms.InputTag( 'hltAlCaPi0RecHitsFilterEEonlyRegional','pi0EcalRecHitsEE' ),
    doEnergyScaleInverse = cms.bool( False ),
    EBRecHitCollection = cms.InputTag( 'hltAlCaPi0RecHitsFilterEEonlyRegional','pi0EcalRecHitsEE' ),
    doIntercalibInverse = cms.bool( False ),
    doLaserCorrections = cms.bool( False ),
    EBRecalibRecHitCollection = cms.string( "pi0EcalRecHitsEB" ),
    doIntercalib = cms.bool( False ),
    EERecalibRecHitCollection = cms.string( "pi0EcalRecHitsEE" )
)
process.hltAlCaPi0EERechitsToDigis = cms.EDProducer( "HLTRechitsToDigis",
    digisIn = cms.InputTag( 'hltEcalDigis','eeDigis' ),
    recHits = cms.InputTag( 'hltAlCaPi0EEUncalibrator','pi0EcalRecHitsEE' ),
    digisOut = cms.string( "pi0EEDigis" ),
    region = cms.string( "endcap" )
)
process.hltPreAlCaEcalEtaEBonlyLowPU = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltAlCaEtaRecHitsFilterEBonlyRegional = cms.EDFilter( "HLTRegionalEcalResonanceFilter",
    barrelSelection = cms.PSet( 
      seleS4S9GammaBarrel_region1 = cms.double( 0.65 ),
      massLowPi0Cand = cms.double( 0.084 ),
      seleIsoBarrel_region2 = cms.double( 0.5 ),
      seleMinvMaxBarrel = cms.double( 0.8 ),
      seleIsoBarrel_region1 = cms.double( 0.5 ),
      seleMinvMinBarrel = cms.double( 0.3 ),
      selePtPairBarrel_region2 = cms.double( 2.5 ),
      seleS9S25Gamma = cms.double( 0.8 ),
      selePtPairBarrel_region1 = cms.double( 2.5 ),
      region1_Barrel = cms.double( 1.0 ),
      seleS4S9GammaBarrel_region2 = cms.double( 0.87 ),
      massHighPi0Cand = cms.double( 0.156 ),
      ptMinForIsolation = cms.double( 1.0 ),
      store5x5RecHitEB = cms.bool( True ),
      selePtGammaBarrel_region1 = cms.double( 0.8 ),
      seleBeltDeta = cms.double( 0.1 ),
      removePi0CandidatesForEta = cms.bool( True ),
      barrelHitCollection = cms.string( "etaEcalRecHitsEB" ),
      selePtGammaBarrel_region2 = cms.double( 0.8 ),
      seleBeltDR = cms.double( 0.3 )
    ),
    statusLevelRecHitsToUse = cms.int32( 1 ),
    endcapHits = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEE' ),
    doSelBarrel = cms.bool( True ),
    flagLevelRecHitsToUse = cms.int32( 1 ),
    preshRecHitProducer = cms.InputTag( 'hltEcalPreshowerRecHit','EcalRecHitsES' ),
    doSelEndcap = cms.bool( False ),
    storeRecHitES = cms.bool( False ),
    endcapClusters = cms.InputTag( 'hltSimple3x3Clusters','Simple3x3ClustersEndcap' ),
    barrelHits = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEB' ),
    useRecoFlag = cms.bool( False ),
    barrelClusters = cms.InputTag( 'hltSimple3x3Clusters','Simple3x3ClustersBarrel' ),
    debugLevel = cms.int32( debug_level ),
    endcapSelection = cms.PSet( 
      seleS9S25GammaEndCap = cms.double( 0.0 ),
      seleBeltDREndCap = cms.double( 0.2 ),
      region1_EndCap = cms.double( 1.8 ),
      seleMinvMinEndCap = cms.double( 0.05 ),
      store5x5RecHitEE = cms.bool( False ),
      seleMinvMaxEndCap = cms.double( 0.3 ),
      selePtPairEndCap_region1 = cms.double( 1.5 ),
      selePtPairEndCap_region3 = cms.double( 99.0 ),
      selePtPairEndCap_region2 = cms.double( 1.5 ),
      selePtGammaEndCap_region3 = cms.double( 0.5 ),
      seleBeltDetaEndCap = cms.double( 0.05 ),
      seleIsoEndCap_region1 = cms.double( 0.5 ),
      region2_EndCap = cms.double( 2.0 ),
      seleS4S9GammaEndCap_region1 = cms.double( 0.65 ),
      seleS4S9GammaEndCap_region2 = cms.double( 0.65 ),
      seleS4S9GammaEndCap_region3 = cms.double( 0.65 ),
      selePtPairMaxEndCap_region3 = cms.double( 2.5 ),
      seleIsoEndCap_region2 = cms.double( 0.5 ),
      ptMinForIsolationEndCap = cms.double( 0.5 ),
      selePtGammaEndCap_region1 = cms.double( 0.5 ),
      seleIsoEndCap_region3 = cms.double( 0.5 ),
      selePtGammaEndCap_region2 = cms.double( 0.5 ),
      endcapHitCollection = cms.string( "etaEcalRecHitsEE" )
    ),
    preshowerSelection = cms.PSet( 
      preshCalibGamma = cms.double( 0.024 ),
      preshStripEnergyCut = cms.double( 0.0 ),
      debugLevelES = cms.string( "" ),
      preshCalibPlaneY = cms.double( 0.7 ),
      preshCalibPlaneX = cms.double( 1.0 ),
      preshCalibMIP = cms.double( 9.0E-5 ),
      preshNclust = cms.int32( 4 ),
      ESCollection = cms.string( "etaEcalRecHitsES" ),
      preshClusterEnergyCut = cms.double( 0.0 ),
      preshSeededNstrip = cms.int32( 15 )
    ),
    useDBStatus = cms.bool( True )
)
process.hltAlCaEtaEBUncalibrator = cms.EDProducer( "EcalRecalibRecHitProducer",
    doEnergyScale = cms.bool( False ),
    doLaserCorrectionsInverse = cms.bool( False ),
    EERecHitCollection = cms.InputTag( 'hltAlCaEtaRecHitsFilterEBonlyRegional','etaEcalRecHitsEB' ),
    doEnergyScaleInverse = cms.bool( False ),
    EBRecHitCollection = cms.InputTag( 'hltAlCaEtaRecHitsFilterEBonlyRegional','etaEcalRecHitsEB' ),
    doIntercalibInverse = cms.bool( False ),
    doLaserCorrections = cms.bool( False ),
    EBRecalibRecHitCollection = cms.string( "etaEcalRecHitsEB" ),
    doIntercalib = cms.bool( False ),
    EERecalibRecHitCollection = cms.string( "etaEcalRecHitsEE" )
)
process.hltAlCaEtaEBRechitsToDigis = cms.EDProducer( "HLTRechitsToDigis",
    digisIn = cms.InputTag( 'hltEcalDigis','ebDigis' ),
    recHits = cms.InputTag( 'hltAlCaEtaEBUncalibrator','etaEcalRecHitsEB' ),
    digisOut = cms.string( "etaEBDigis" ),
    region = cms.string( "barrel" )
)
process.hltPreAlCaEcalEtaEEonlyLowPU = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltAlCaEtaRecHitsFilterEEonlyRegional = cms.EDFilter( "HLTRegionalEcalResonanceFilter",
    barrelSelection = cms.PSet( 
      seleS4S9GammaBarrel_region1 = cms.double( 0.65 ),
      massLowPi0Cand = cms.double( 0.104 ),
      seleIsoBarrel_region2 = cms.double( 0.5 ),
      seleMinvMaxBarrel = cms.double( 0.8 ),
      seleIsoBarrel_region1 = cms.double( 0.5 ),
      seleMinvMinBarrel = cms.double( 0.3 ),
      selePtPairBarrel_region2 = cms.double( 1.5 ),
      seleS9S25Gamma = cms.double( 0.0 ),
      selePtPairBarrel_region1 = cms.double( 1.5 ),
      region1_Barrel = cms.double( 1.0 ),
      seleS4S9GammaBarrel_region2 = cms.double( 0.65 ),
      massHighPi0Cand = cms.double( 0.163 ),
      ptMinForIsolation = cms.double( 1.0 ),
      store5x5RecHitEB = cms.bool( False ),
      selePtGammaBarrel_region1 = cms.double( 1.0 ),
      seleBeltDeta = cms.double( 0.05 ),
      removePi0CandidatesForEta = cms.bool( False ),
      barrelHitCollection = cms.string( "etaEcalRecHitsEB" ),
      selePtGammaBarrel_region2 = cms.double( 0.5 ),
      seleBeltDR = cms.double( 0.2 )
    ),
    statusLevelRecHitsToUse = cms.int32( 1 ),
    endcapHits = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEE' ),
    doSelBarrel = cms.bool( False ),
    flagLevelRecHitsToUse = cms.int32( 1 ),
    preshRecHitProducer = cms.InputTag( 'hltEcalPreshowerRecHit','EcalRecHitsES' ),
    doSelEndcap = cms.bool( True ),
    storeRecHitES = cms.bool( True ),
    endcapClusters = cms.InputTag( 'hltSimple3x3Clusters','Simple3x3ClustersEndcap' ),
    barrelHits = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEB' ),
    useRecoFlag = cms.bool( False ),
    barrelClusters = cms.InputTag( 'hltSimple3x3Clusters','Simple3x3ClustersBarrel' ),
    debugLevel = cms.int32( debug_level ),
    endcapSelection = cms.PSet( 
      seleS9S25GammaEndCap = cms.double( 0.85 ),
      seleBeltDREndCap = cms.double( 0.3 ),
      region1_EndCap = cms.double( 1.8 ),
      seleMinvMinEndCap = cms.double( 0.3 ),
      store5x5RecHitEE = cms.bool( True ),
      seleMinvMaxEndCap = cms.double( 0.8 ),
      selePtPairEndCap_region1 = cms.double( 2.7 ),
      selePtPairEndCap_region3 = cms.double( 2.7 ),
      selePtPairEndCap_region2 = cms.double( 2.7 ),
      selePtGammaEndCap_region3 = cms.double( 1.0 ),
      seleBeltDetaEndCap = cms.double( 0.1 ),
      seleIsoEndCap_region1 = cms.double( 0.5 ),
      region2_EndCap = cms.double( 2.0 ),
      seleS4S9GammaEndCap_region1 = cms.double( 0.9 ),
      seleS4S9GammaEndCap_region2 = cms.double( 0.9 ),
      seleS4S9GammaEndCap_region3 = cms.double( 0.9 ),
      selePtPairMaxEndCap_region3 = cms.double( 999.0 ),
      seleIsoEndCap_region2 = cms.double( 0.5 ),
      ptMinForIsolationEndCap = cms.double( 0.5 ),
      selePtGammaEndCap_region1 = cms.double( 0.8 ),
      seleIsoEndCap_region3 = cms.double( 0.5 ),
      selePtGammaEndCap_region2 = cms.double( 0.8 ),
      endcapHitCollection = cms.string( "etaEcalRecHitsEE" )
    ),
    preshowerSelection = cms.PSet( 
      preshCalibGamma = cms.double( 0.024 ),
      preshStripEnergyCut = cms.double( 0.0 ),
      debugLevelES = cms.string( "" ),
      preshCalibPlaneY = cms.double( 0.7 ),
      preshCalibPlaneX = cms.double( 1.0 ),
      preshCalibMIP = cms.double( 9.0E-5 ),
      preshNclust = cms.int32( 4 ),
      ESCollection = cms.string( "etaEcalRecHitsES" ),
      preshClusterEnergyCut = cms.double( 0.0 ),
      preshSeededNstrip = cms.int32( 15 )
    ),
    useDBStatus = cms.bool( True )
)
process.hltAlCaEtaEEUncalibrator = cms.EDProducer( "EcalRecalibRecHitProducer",
    doEnergyScale = cms.bool( False ),
    doLaserCorrectionsInverse = cms.bool( False ),
    EERecHitCollection = cms.InputTag( 'hltAlCaEtaRecHitsFilterEEonlyRegional','etaEcalRecHitsEE' ),
    doEnergyScaleInverse = cms.bool( False ),
    EBRecHitCollection = cms.InputTag( 'hltAlCaEtaRecHitsFilterEEonlyRegional','etaEcalRecHitsEE' ),
    doIntercalibInverse = cms.bool( False ),
    doLaserCorrections = cms.bool( False ),
    EBRecalibRecHitCollection = cms.string( "etaEcalRecHitsEB" ),
    doIntercalib = cms.bool( False ),
    EERecalibRecHitCollection = cms.string( "etaEcalRecHitsEE" )
)
process.hltAlCaEtaEERechitsToDigis = cms.EDProducer( "HLTRechitsToDigis",
    digisIn = cms.InputTag( 'hltEcalDigis','eeDigis' ),
    recHits = cms.InputTag( 'hltAlCaEtaEEUncalibrator','etaEcalRecHitsEE' ),
    digisOut = cms.string( "etaEEDigis" ),
    region = cms.string( "endcap" )
)
process.hltFEDSelector = cms.EDProducer( "EvFFEDSelector",
    inputTag = cms.InputTag( "rawDataCollector" ),
    fedList = cms.vuint32( 1023, 1024 )
)
process.hltTriggerSummaryAOD = cms.EDProducer( "TriggerSummaryProducerAOD",
    processName = cms.string( "@" )
)
process.hltTriggerSummaryRAW = cms.EDProducer( "TriggerSummaryProducerRAW",
    processName = cms.string( "@" )
)
process.hltPreALCAP0Output = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)

# process.hltOutputALCAP0 = cms.OutputModule( "PoolOutputModule",
#     fileName = cms.untracked.string( "outputALCAP0.root" ),
#     fastCloning = cms.untracked.bool( False ),
#     dataset = cms.untracked.PSet(
#         filterName = cms.untracked.string( "" ),
#         dataTier = cms.untracked.string( "RAW" )
#     ),
#     SelectEvents = cms.untracked.PSet(  SelectEvents = cms.vstring( 'AlCa_EcalEtaEBonly_LowPU_v1',
#   'AlCa_EcalEtaEEonly_LowPU_v1',
#   'AlCa_EcalPi0EBonly_LowPU_v1',
#   'AlCa_EcalPi0EEonly_LowPU_v1' ) ),
#     outputCommands = cms.untracked.vstring( 'keep *',
#       'keep *_hltAlCaEtaEBRechitsToDigis_*_*',
#       'keep *_hltAlCaEtaEBUncalibrator_*_*',
#       'keep *_hltAlCaEtaEERechitsToDigis_*_*',
#       'keep *_hltAlCaEtaEEUncalibrator_*_*',
#       'keep *_hltAlCaEtaRecHitsFilterEEonlyRegional_etaEcalRecHitsES_*',
#       'keep *_hltAlCaPi0EBRechitsToDigis_*_*',
#       'keep *_hltAlCaPi0EBUncalibrator_*_*',
#       'keep *_hltAlCaPi0EERechitsToDigis_*_*',
#       'keep *_hltAlCaPi0EEUncalibrator_*_*',
#       'keep *_hltAlCaPi0RecHitsFilterEEonlyRegional_pi0EcalRecHitsES_*',
# #      'keep *_hltSimple3x3Clusters_*',                                      
#       'keep L1GlobalTriggerReadoutRecord_hltGtDigis_*_*',                                            
#       'keep edmTriggerResults_*_*_*' )
# )

process.HLTL1UnpackerSequence = cms.Sequence( process.hltGtDigis + process.hltGctDigis + process.hltL1GtObjectMap + process.hltL1extraParticles )
process.HLTBeamSpot = cms.Sequence( process.hltScalersRawToDigi + process.hltOnlineBeamSpot )
process.HLTBeginSequence = cms.Sequence( process.hltTriggerType + process.HLTL1UnpackerSequence + process.HLTBeamSpot )
process.HLTDoFullUnpackingEgammaEcalSequence = cms.Sequence( process.hltEcalDigis + process.hltEcalPreshowerDigis + process.hltEcalUncalibRecHit + process.hltEcalDetIdToBeRecovered + process.hltEcalRecHit + process.hltEcalPreshowerRecHit )
process.HLTEndSequence = cms.Sequence( process.hltBoolEnd )

process.HLTriggerFirstPath = cms.Path( process.hltGetConditions + process.hltGetRaw + process.hltBoolFalse )
#process.HLTriggerFirstPath = cms.Path( process.hltGetConditions)# + process.hltGetRaw + process.hltBoolFalse )
process.AlCa_EcalPi0EBonly_LowPU_v1 = cms.Path( process.HLTBeginSequence + process.hltPreAlCaEcalPi0EBonlyLowPU + process.HLTDoFullUnpackingEgammaEcalSequence + process.hltSimple3x3Clusters + process.hltAlCaPi0RecHitsFilterEBonlyRegional + process.hltAlCaPi0EBUncalibrator + process.hltAlCaPi0EBRechitsToDigis + process.HLTEndSequence )

process.AlCa_EcalPi0EEonly_LowPU_v1 = cms.Path( process.HLTBeginSequence + process.hltPreAlCaEcalPi0EEonlyLowPU + process.HLTDoFullUnpackingEgammaEcalSequence + process.hltSimple3x3Clusters + process.hltAlCaPi0RecHitsFilterEEonlyRegional + process.hltAlCaPi0EEUncalibrator + process.hltAlCaPi0EERechitsToDigis + process.HLTEndSequence )

process.AlCa_EcalEtaEBonly_LowPU_v1 = cms.Path( process.HLTBeginSequence + process.hltPreAlCaEcalEtaEBonlyLowPU  + process.HLTDoFullUnpackingEgammaEcalSequence + process.hltSimple3x3Clusters + process.hltAlCaEtaRecHitsFilterEBonlyRegional + process.hltAlCaEtaEBUncalibrator + process.hltAlCaEtaEBRechitsToDigis + process.HLTEndSequence )

process.AlCa_EcalEtaEEonly_LowPU_v1 = cms.Path( process.HLTBeginSequence + process.hltPreAlCaEcalEtaEEonlyLowPU  + process.HLTDoFullUnpackingEgammaEcalSequence + process.hltSimple3x3Clusters + process.hltAlCaEtaRecHitsFilterEEonlyRegional + process.hltAlCaEtaEEUncalibrator + process.hltAlCaEtaEERechitsToDigis + process.HLTEndSequence )

process.HLTriggerFinalPath = cms.Path( process.hltGtDigis + process.hltScalersRawToDigi + process.hltFEDSelector + process.hltTriggerSummaryAOD + process.hltTriggerSummaryRAW + process.hltBoolFalse )

# # basic cluster reco
# process.basic                = cms.EDAnalyzer('PizeroAnalyzer')
# process.basic.outputFileName = cms.untracked.string('pizero.root')
# process.basic.treeName       = cms.untracked.string('barrel')
# process.basic.debug          = cms.untracked.int32(0)
# process.basic.doEta          = cms.untracked.bool(False)
# process.basic.doEnd          = cms.untracked.bool(False)
# process.basic.isMC           = cms.untracked.bool(True)
# process.basic.barrelClusters = cms.untracked.InputTag("hltSimple3x3Clusters","Simple3x3ClustersBarrel","TEST")
# process.basic.endClusters    = cms.untracked.InputTag("hltSimple3x3Clusters","Simple3x3ClustersEndcap","TEST")

process.dummyHitsPi0 = cms.EDProducer("DummyRechitDigis",
                                      doDigi = cms.untracked.bool(False),
                                      # rechits
                                      barrelHitProducer      = cms.InputTag('hltAlCaPi0EBUncalibrator','pi0EcalRecHitsEB' ,"TEST"),
                                      endcapHitProducer      = cms.InputTag('hltAlCaPi0EEUncalibrator','pi0EcalRecHitsEE' ,"TEST"),
                                      barrelRecHitCollection = cms.untracked.string("dummyBarrelRechitsPi0"),
                                      endcapRecHitCollection = cms.untracked.string("dummyEndcapRechitsPi0"),
                                      # digis
                                      barrelDigis            = cms.InputTag(  'hltAlCaPi0EBRechitsToDigis','pi0EBDigis' ,"TEST"),
                                      endcapDigis            = cms.InputTag(  'hltAlCaPi0EERechitsToDigis','pi0EEDigis' ,"TEST"),
                                      barrelDigiCollection   = cms.untracked.string("dummyBarrelDigisPi0"),
                                      endcapDigiCollection   = cms.untracked.string("dummyEndcapDigisPi0"))

process.dummyHitsEta = cms.EDProducer("DummyRechitDigis",
                                      doDigi = cms.untracked.bool(False),
                                      # rechits
                                      barrelHitProducer      = cms.InputTag('hltAlCaEtaEBUncalibrator','etaEcalRecHitsEB' ,"TEST"),
                                      endcapHitProducer      = cms.InputTag('hltAlCaEtaEEUncalibrator','etaEcalRecHitsEE' ,"TEST"),
                                      barrelRecHitCollection = cms.untracked.string("dummyBarrelRechitsEta"),
                                      endcapRecHitCollection = cms.untracked.string("dummyEndcapRechitsEta"),
                                      # digis
                                      barrelDigis            = cms.InputTag(  'hltAlCaEtaEBRechitsToDigis','etaEBDigis' ,"TEST"),
                                      endcapDigis            = cms.InputTag(  'hltAlCaEtaEERechitsToDigis','etaEEDigis' ,"TEST"),
                                      barrelDigiCollection   = cms.untracked.string("dummyBarrelDigisEta"),
                                      endcapDigiCollection   = cms.untracked.string("dummyEndcapDigisEta"))

process.pizeroClusters = cms.EDProducer( "EgammaHLTNxNClusterProducer",
    statusLevelRecHitsToUse = cms.int32( 1 ),
    barrelClusterCollection = cms.string( "Simple3x3ClustersBarrel" ),
    flagLevelRecHitsToUse = cms.int32( 1 ),
    maxNumberofClusters = cms.int32( 99999 ),
    clusPhiSize = cms.int32( 3 ),
    posCalcParameters = cms.PSet(
      T0_barl = cms.double( 7.4 ),
      LogWeighted = cms.bool( True ),
      T0_endc = cms.double( 3.1 ),
      T0_endcPresh = cms.double( 1.2 ),
      W0 = cms.double( 4.2 ),
      X0 = cms.double( 0.89 )
    ),
    clusEtaSize = cms.int32( 3 ),
    useRecoFlag = cms.bool( False ),
    endcapHitProducer = cms.InputTag('dummyHitsPi0', 'dummyEndcapRechitsPi0' ,"TEST"),
    maxNumberofSeeds = cms.int32( 99999 ),
    useDBStatus = cms.bool( True ),
    debugLevel = cms.int32( debug_level ),
    barrelHitProducer = cms.InputTag('dummyHitsPi0', 'dummyBarrelRechitsPi0' ,"TEST"),
    clusSeedThrEndCap = cms.double( 1.0 ),
    clusSeedThr = cms.double( 0.5 ),
    doEndcaps = cms.bool( True ),
    endcapClusterCollection = cms.string( "Simple3x3ClustersEndcap" ),
    doBarrel = cms.bool( True )
)

process.etaClusters = cms.EDProducer( "EgammaHLTNxNClusterProducer",
    statusLevelRecHitsToUse = cms.int32( 1 ),
    barrelClusterCollection = cms.string( "Simple3x3ClustersBarrel" ),
    flagLevelRecHitsToUse = cms.int32( 1 ),
    maxNumberofClusters = cms.int32( 99999 ),
    clusPhiSize = cms.int32( 3 ),
    posCalcParameters = cms.PSet(
      T0_barl = cms.double( 7.4 ),
      LogWeighted = cms.bool( True ),
      T0_endc = cms.double( 3.1 ),
      T0_endcPresh = cms.double( 1.2 ),
      W0 = cms.double( 4.2 ),
      X0 = cms.double( 0.89 )
    ),
    clusEtaSize = cms.int32( 3 ),
    useRecoFlag = cms.bool( False ),
    endcapHitProducer = cms.InputTag('dummyHitsEta', 'dummyEndcapRechitsEta' ,"TEST"),
    maxNumberofSeeds = cms.int32( 99999 ),
    useDBStatus = cms.bool( True ),
    debugLevel = cms.int32( debug_level ),
    barrelHitProducer = cms.InputTag('dummyHitsEta', 'dummyBarrelRechitsEta' ,"TEST"),
    clusSeedThrEndCap = cms.double( 1.0 ),
    clusSeedThr = cms.double( 0.5 ),
    doEndcaps = cms.bool( True ),
    endcapClusterCollection = cms.string( "Simple3x3ClustersEndcap" ),
    doBarrel = cms.bool( True )
)

# pi0 EB
process.reclusterpi0eb                = cms.EDAnalyzer('PizeroAnalyzer')
process.reclusterpi0eb.outputFileName = cms.untracked.string('pi0_recluster_eb.root')
process.reclusterpi0eb.treeName       = cms.untracked.string('barrel')
process.reclusterpi0eb.debug          = cms.untracked.int32(debug_level_recluster)
process.reclusterpi0eb.doEta          = cms.untracked.bool(False)
process.reclusterpi0eb.doEnd          = cms.untracked.bool(False)
process.reclusterpi0eb.isMC           = cms.untracked.bool(False)
process.reclusterpi0eb.barrelClusters = cms.untracked.InputTag("pizeroClusters","Simple3x3ClustersBarrel")
process.reclusterpi0eb.endClusters    = cms.untracked.InputTag("pizeroClusters","Simple3x3ClustersEndcap")

# eta EB
process.reclusteretaeb                = cms.EDAnalyzer('PizeroAnalyzer')
process.reclusteretaeb.outputFileName = cms.untracked.string('eta_recluster_eb.root')
process.reclusteretaeb.treeName       = cms.untracked.string('barrel')
process.reclusteretaeb.debug          = cms.untracked.int32(debug_level_recluster)
process.reclusteretaeb.doEta          = cms.untracked.bool(True)
process.reclusteretaeb.doEnd          = cms.untracked.bool(False)
process.reclusteretaeb.isMC           = cms.untracked.bool(False)
process.reclusteretaeb.barrelClusters = cms.untracked.InputTag("etaClusters","Simple3x3ClustersBarrel")
process.reclusteretaeb.endClusters    = cms.untracked.InputTag("etaClusters","Simple3x3ClustersEndcap")

# pizero EE
process.reclusterpi0ee                = cms.EDAnalyzer('PizeroAnalyzer')
process.reclusterpi0ee.outputFileName = cms.untracked.string('pi0_recluster_ee.root')
process.reclusterpi0ee.treeName       = cms.untracked.string('endcap')
process.reclusterpi0ee.debug          = cms.untracked.int32(debug_level_recluster)
process.reclusterpi0ee.doEta          = cms.untracked.bool(False)
process.reclusterpi0ee.doEnd          = cms.untracked.bool(True)
process.reclusterpi0ee.isMC           = cms.untracked.bool(False)
process.reclusterpi0ee.barrelClusters = cms.untracked.InputTag("pizeroClusters","Simple3x3ClustersBarrel")
process.reclusterpi0ee.endClusters    = cms.untracked.InputTag("pizeroClusters","Simple3x3ClustersEndcap")

# eta EE
process.reclusteretaee                = cms.EDAnalyzer('PizeroAnalyzer')
process.reclusteretaee.outputFileName = cms.untracked.string('eta_recluster_ee.root')
process.reclusteretaee.treeName       = cms.untracked.string('endcap')
process.reclusteretaee.debug          = cms.untracked.int32(debug_level_recluster)
process.reclusteretaee.doEta          = cms.untracked.bool(True)
process.reclusteretaee.doEnd          = cms.untracked.bool(True)
process.reclusteretaee.isMC           = cms.untracked.bool(False)
process.reclusteretaee.barrelClusters = cms.untracked.InputTag("etaClusters","Simple3x3ClustersBarrel")
process.reclusteretaee.endClusters    = cms.untracked.InputTag("etaClusters","Simple3x3ClustersEndcap")

process.ALCAP0Output = cms.EndPath(process.dummyHitsPi0 +  process.dummyHitsEta + process.pizeroClusters +  process.etaClusters + process.reclusterpi0eb  + process.reclusteretaeb + process.reclusterpi0ee + process.reclusteretaee ) 
#process.ALCAP0Output = cms.EndPath(process.dummyHitsPi0 + process.pizeroClusters + process.reclusterpi0ee) 
#process.ALCAP0Output = cms.EndPath(process.pizeroEBClusters + process.etaEBClusters + process.reclusteretaeb + process.reclusterpi0eb) #process.hltOutputALCAP0
#process.ALCAP0Output = cms.EndPath(process.dummyHitsEB + process.etaEBClusters + process.reclusteretaeb) #process.hltOutputALCAP0

process.HLTSchedule = cms.Schedule( *(process.HLTriggerFirstPath, process.AlCa_EcalPi0EBonly_LowPU_v1, process.AlCa_EcalPi0EEonly_LowPU_v1, process.AlCa_EcalEtaEBonly_LowPU_v1, process.AlCa_EcalEtaEEonly_LowPU_v1, process.HLTriggerFinalPath, process.ALCAP0Output ))

#process.HLTSchedule = cms.Schedule( *(process.HLTriggerFirstPath, process.ALCAP0Output ))

input_file_list = None
input_file_list = '/afs/cern.ch/user/h/hardenbr/2013/PIZERO/HLT_PATH/CMSSW_7_4_3/src/minbias_small.txt'
# parse the input files to the file list                                                                                                                                                            
myfilelist = cms.untracked.vstring()
if input_file_list != None:
   list_from_input_list = open(input_file_list, "r")
   lines = list_from_input_list.readlines()
   stripped_lines = map(lambda x: x.rstrip("\n"), lines)
   for line in stripped_lines:
      myfilelist.extend([line])
else:
   myfilelist.extend(["file:/afs/cern.ch/work/h/hardenbr/pizero_minbasi_nofail.root"])

process.source = cms.Source( "PoolSource", #fileNames = myfilelist )
                             fileNames  = cms.untracked.vstring(
#                                    'file:/afs/cern.ch/user/h/hardenbr/2013/PIZERO/HLT_PATH/CMSSW_7_4_3/src/outputALCAP0.root'
                                     'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/MinimumBias/RAW/v1/000/246/081/00000/0A92FEF3-7005-E511-978C-02163E012A88.root',
                                     'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/MinimumBias/RAW/v1/000/246/081/00000/14829B20-8505-E511-937E-02163E0126FB.root',
                                     'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/MinimumBias/RAW/v1/000/246/081/00000/14AFB466-8505-E511-BFEE-02163E0144EE.root',
                                     'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/MinimumBias/RAW/v1/000/246/081/00000/269703F1-7005-E511-B19C-02163E0142B3.root',
                                     'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/MinimumBias/RAW/v1/000/246/081/00000/2E9BA321-8505-E511-84E5-02163E0146A9.root',
                                     'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/MinimumBias/RAW/v1/000/246/081/00000/306C155A-8505-E511-9CD1-02163E011C07.root',
                                     'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/MinimumBias/RAW/v1/000/246/081/00000/38B2F427-8505-E511-8CAB-02163E011816.root',
                                     'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/MinimumBias/RAW/v1/000/246/081/00000/44095E24-8505-E511-A475-02163E014100.root',
                                     'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/MinimumBias/RAW/v1/000/246/081/00000/54D94F11-7105-E511-B184-02163E012BD8.root',
                                     'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/MinimumBias/RAW/v1/000/246/081/00000/5A227803-7105-E511-BC05-02163E0123D0.root',
                                     'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/MinimumBias/RAW/v1/000/246/081/00000/6631DF17-8505-E511-9EC8-02163E013511.root',
                                     'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/MinimumBias/RAW/v1/000/246/081/00000/6A995B2F-8505-E511-8581-02163E0143FB.root',
                                     'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/MinimumBias/RAW/v1/000/246/081/00000/74B0D7EC-7005-E511-8794-02163E0138BC.root',
                                     'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/MinimumBias/RAW/v1/000/246/081/00000/A2C4A2F3-7005-E511-B0E7-02163E01365F.root',
                                     'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/MinimumBias/RAW/v1/000/246/081/00000/A8EFFE24-8505-E511-8B81-02163E01395B.root',
                                     'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/MinimumBias/RAW/v1/000/246/081/00000/AA801422-7105-E511-838B-02163E011CFB.root',
                                     'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/MinimumBias/RAW/v1/000/246/081/00000/B23A0A1A-8505-E511-AC62-02163E0136D7.root',
                                     'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/MinimumBias/RAW/v1/000/246/081/00000/B62869F1-7005-E511-AB74-02163E012BE0.root',
                                     'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/MinimumBias/RAW/v1/000/246/081/00000/CEF0C103-7105-E511-8483-02163E01469F.root',
                                     'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/MinimumBias/RAW/v1/000/246/081/00000/E09DAEDB-5B05-E511-82C7-02163E014249.root',
                                     'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/MinimumBias/RAW/v1/000/246/081/00000/E283770B-7105-E511-91DD-02163E01268A.root',
                                     'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/MinimumBias/RAW/v1/000/246/081/00000/F8677617-8505-E511-9AD3-02163E014323.root',
                                     'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/MinimumBias/RAW/v1/000/246/081/00000/FE980A1F-8505-E511-9F2D-02163E013502.root'))
#                                            'root://xrootd-cms.infn.it//store/data/Commissioning2015/MinimumBias/RAW/v1/000/232/881/00000/E63DF8F8-3FAB-E411-A41A-02163E011DD5.root'


# load 2015 Run-2 L1 Menu for 25ns (default for GRun, PIon)
from L1Trigger.Configuration.customise_overwriteL1Menu import L1Menu_Collisions2015_25ns_v2 as loadL1menu
process = loadL1menu(process)

# adapt HLT modules to the correct process name
if 'hltTrigReport' in process.__dict__:
    process.hltTrigReport.HLTriggerResults                    = cms.InputTag( 'TriggerResults', '', 'TEST' )

if 'hltPreExpressCosmicsOutputSmart' in process.__dict__:
    process.hltPreExpressCosmicsOutputSmart.hltResults = cms.InputTag( 'TriggerResults', '', 'TEST' )

if 'hltPreExpressOutputSmart' in process.__dict__:
    process.hltPreExpressOutputSmart.hltResults        = cms.InputTag( 'TriggerResults', '', 'TEST' )

if 'hltPreDQMForHIOutputSmart' in process.__dict__:
    process.hltPreDQMForHIOutputSmart.hltResults       = cms.InputTag( 'TriggerResults', '', 'TEST' )

if 'hltPreDQMForPPOutputSmart' in process.__dict__:
    process.hltPreDQMForPPOutputSmart.hltResults       = cms.InputTag( 'TriggerResults', '', 'TEST' )

if 'hltPreHLTDQMResultsOutputSmart' in process.__dict__:
    process.hltPreHLTDQMResultsOutputSmart.hltResults  = cms.InputTag( 'TriggerResults', '', 'TEST' )

if 'hltPreHLTDQMOutputSmart' in process.__dict__:
    process.hltPreHLTDQMOutputSmart.hltResults         = cms.InputTag( 'TriggerResults', '', 'TEST' )

if 'hltPreHLTMONOutputSmart' in process.__dict__:
    process.hltPreHLTMONOutputSmart.hltResults         = cms.InputTag( 'TriggerResults', '', 'TEST' )

if 'hltDQMHLTScalers' in process.__dict__:
    process.hltDQMHLTScalers.triggerResults                   = cms.InputTag( 'TriggerResults', '', 'TEST' )
    process.hltDQMHLTScalers.processname                      = 'TEST'

if 'hltDQML1SeedLogicScalers' in process.__dict__:
    process.hltDQML1SeedLogicScalers.processname              = 'TEST'

# limit the number of events to be processed
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32( 100 )
)

# enable the TrigReport and TimeReport
process.options = cms.untracked.PSet(
#    SkipEvent = cms.untracked.vstring('ProductNotFound'),
    wantSummary = cms.untracked.bool( True )
)

# override the GlobalTag, connection string and pfnPrefix
if 'GlobalTag' in process.__dict__:
    from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag as customiseGlobalTag
    process.GlobalTag = customiseGlobalTag(process.GlobalTag, globaltag = 'GR_H_V58')
    process.GlobalTag.connect   = 'frontier://FrontierProd/CMS_CONDITIONS'
    process.GlobalTag.pfnPrefix = cms.untracked.string('frontier://FrontierProd/')
    for pset in process.GlobalTag.toGet.value():
        pset.connect = pset.connect.value().replace('frontier://FrontierProd/', 'frontier://FrontierProd/')
    # fix for multi-run processing
    process.GlobalTag.RefreshEachRun = cms.untracked.bool( False )
    process.GlobalTag.ReconnectEachRun = cms.untracked.bool( False )

# override the L1 menu from an Xml file
process.l1GtTriggerMenuXml = cms.ESProducer("L1GtTriggerMenuXmlProducer",
  TriggerMenuLuminosity = cms.string('startup'),
  DefXmlFile = cms.string('L1Menu_Collisions2015_lowPU_v2_L1T_Scales_20141121.xml'),
  VmeXmlFile = cms.string('')
)
process.L1GtTriggerMenuRcdSource = cms.ESSource("EmptyESSource",
  recordName = cms.string('L1GtTriggerMenuRcd'),
  iovIsRunNotTime = cms.bool(True),
  firstValid = cms.vuint32(1)
)
process.es_prefer_l1GtParameters = cms.ESPrefer('L1GtTriggerMenuXmlProducer','l1GtTriggerMenuXml')

if 'MessageLogger' in process.__dict__:
    process.MessageLogger.categories.append('TriggerSummaryProducerAOD')
    process.MessageLogger.categories.append('L1GtTrigReport')
    process.MessageLogger.categories.append('HLTrigReport')
    process.MessageLogger.categories.append('FastReport')


# load the DQMStore and DQMRootOutputModule
#process.load( "DQMServices.Core.DQMStore_cfi" )
#3process.DQMStore.enableMultiThread = True

# process.dqmOutput = cms.OutputModule("DQMRootOutputModule",
#     fileName = cms.untracked.string("DQMIO.root")
# )

# process.DQMOutput = cms.EndPath( process.dqmOutput )

# # Add specific customizations
# _customInfo = {}
# _customInfo['menuType'  ]= "GRun"
# _customInfo['globalTags']= {}
# _customInfo['globalTags'][True ] = "auto:run2_hlt_GRun"
# _customInfo['globalTags'][False] = "auto:run2_mc_GRun"
# _customInfo['inputFiles']={}
# _customInfo['inputFiles'][True]  = "file:RelVal_Raw_GRun_DATA.root"
# _customInfo['inputFiles'][False] = "file:RelVal_Raw_GRun_MC.root"
# _customInfo['maxEvents' ]=  100
# _customInfo['globalTag' ]= "GR_H_V58"
# _customInfo['inputFile' ]=  ['root://xrootd-cms.infn.it//store/data/Commissioning2015/MinimumBias/RAW/v1/000/232/881/00000/E63DF8F8-3FAB-E411-A41A-02163E011DD5.root']
# _customInfo['realData'  ]=  True
# from HLTrigger.Configuration.customizeHLTforALL import customizeHLTforAll
# process = customizeHLTforAll(process,_customInfo)

