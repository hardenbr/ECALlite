import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")
process.load("FWCore.MessageService.MessageLogger_cfi")
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
                            # replace 'myfile.root' with the source file you want to use
                            fileNames = cms.untracked.vstring(
        ' file:/afs/cern.ch/user/h/hardenbr/2013/PIZERO/HLT_PATH/CMSSW_7_4_3/src/outputALCAP0.root'
        )
                            )

process.pizeroEBClusters = cms.EDProducer( "EgammaHLTNxNClusterProducer",
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
    endcapHitProducer = cms.InputTag( 'hltAlCaPi0EBUncalibrator','pi0EcalRecHitsEE' ),
    maxNumberofSeeds = cms.int32( 99999 ),
    useDBStatus = cms.bool( True ),
    debugLevel = cms.int32( 10 ),
    barrelHitProducer = cms.InputTag(  'hltAlCaPi0EBUncalibrator','pi0EcalRecHitsEB' ),
    clusSeedThrEndCap = cms.double( 1.0 ),
    clusSeedThr = cms.double( 0.5 ),
    doEndcaps = cms.bool( True ),
    endcapClusterCollection = cms.string( "Simple3x3ClustersEndcap" ),
    doBarrel = cms.bool( True )
)

process.basic                = cms.EDAnalyzer('PizeroAnalyzer')
process.basic.outputFileName = cms.untracked.string('pizero.root')
process.basic.treeName       = cms.untracked.string('barrel')
process.basic.debug          = cms.untracked.int32(10)
process.basic.doEta          = cms.untracked.bool(True)
process.basic.doEnd          = cms.untracked.bool(False)
process.basic.isMC           = cms.untracked.bool(True)
process.basic.barrelClusters = cms.untracked.InputTag("pizeroEBClusters","Simple3x3ClustersBarrel","TEST")
process.basic.endClusters    = cms.untracked.InputTag("pizeroEEClusters","Simple3x3ClustersEndcap","TEST")

process.p = cms.Path(process.pizeroEBClusters + process.basic)
