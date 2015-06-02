# # /users/hardenbr/pizero_stream/pizero_stream_lowpu_fix1/V4 (CMSSW_7_4_3)
# EBDigiCollection                      "hltAlCaEtaEBRechitsToDigis"   "etaEBDigis"      "HLT"     
# EBDigiCollection                      "hltAlCaPi0EBRechitsToDigis"   "pi0EBDigis"      "HLT"     
# EEDigiCollection                      "hltAlCaEtaEERechitsToDigis"   "etaEEDigis"      "HLT"     
# EEDigiCollection                      "hltAlCaPi0EERechitsToDigis"   "pi0EEDigis"      "HLT"     
# L1GlobalTriggerReadoutRecord          "hltGtDigis"                ""                "HLT"     
# edm::SortedCollection<EcalRecHit,edm::StrictWeakOrdering<EcalRecHit> >    "hltAlCaEtaRecHitsFilterEEonlyRegional"   "etaEcalRecHitsES"   "HLT"     
# edm::SortedCollection<EcalRecHit,edm::StrictWeakOrdering<EcalRecHit> >    "hltAlCaPi0RecHitsFilterEEonlyRegional"   "pi0EcalRecHitsES"   "HLT"     
# edm::TriggerResults                   "TriggerResults"            ""                "HLT"  

import FWCore.ParameterSet.Config as cms
debug_level_recluster = 0
debug_level           = 0
pname = "TEST"
process               = cms.Process( pname )
#process.load("setup_cff")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("Configuration.Geometry.GeometryIdeal_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")

process.dummyHitsPi0 = cms.EDProducer("DummyRechitDigis",
                                      doDigi = cms.untracked.bool(True),
                                      # rechits
                                      barrelHitProducer      = cms.InputTag('hltAlCaPi0EBUncalibrator','pi0EcalRecHitsEB' ,"HLT"),
                                      endcapHitProducer      = cms.InputTag('hltAlCaPi0EEUncalibrator','pi0EcalRecHitsEE' ,"HLT"),
                                      barrelRecHitCollection = cms.untracked.string("dummyBarrelRechitsPi0"),
                                      endcapRecHitCollection = cms.untracked.string("dummyEndcapRechitsPi0"),
                                      # digis
                                      barrelDigis            = cms.InputTag(  'hltAlCaPi0EBRechitsToDigis','pi0EBDigis' ,"HLT"),
                                      endcapDigis            = cms.InputTag(  'hltAlCaPi0EERechitsToDigis','pi0EEDigis' ,"HLT"),
                                      barrelDigiCollection   = cms.untracked.string("dummyBarrelDigisPi0"),
                                      endcapDigiCollection   = cms.untracked.string("dummyEndcapDigisPi0"))

process.dummyHitsEta = cms.EDProducer("DummyRechitDigis",
                                      doDigi = cms.untracked.bool(True),
                                      # rechits
                                      barrelHitProducer      = cms.InputTag('hltAlCaEtaEBUncalibrator','etaEcalRecHitsEB' ,"HLT"),
                                      endcapHitProducer      = cms.InputTag('hltAlCaEtaEEUncalibrator','etaEcalRecHitsEE' ,"HLT"),
                                      barrelRecHitCollection = cms.untracked.string("dummyBarrelRechitsEta"),
                                      endcapRecHitCollection = cms.untracked.string("dummyEndcapRechitsEta"),
                                      # digis
                                      barrelDigis            = cms.InputTag('hltAlCaEtaEBRechitsToDigis','etaEBDigis' ,"HLT"),
                                      endcapDigis            = cms.InputTag('hltAlCaEtaEERechitsToDigis','etaEEDigis' ,"HLT"),
                                      barrelDigiCollection   = cms.untracked.string("dummyBarrelDigisEta"),
                                      endcapDigiCollection   = cms.untracked.string("dummyEndcapDigisEta"))

#pi0 uncalibrated rechits from multifit
process.load('Configuration.StandardSequences.Reconstruction_cff')
import RecoLocalCalo.EcalRecProducers.ecalMultiFitUncalibRecHit_cfi
process.ecalMultiFitUncalibRecHitPi0                               = RecoLocalCalo.EcalRecProducers.ecalMultiFitUncalibRecHit_cfi.ecalMultiFitUncalibRecHit.clone()
process.ecalMultiFitUncalibRecHitPi0.algoPSet.useLumiInfoRunHeader = cms.bool( False ) # To read the conditions from the header 
process.ecalMultiFitUncalibRecHitPi0.algoPSet.activeBXs            = cms.vint32(-4,-2,0,2,4) #Are 10 (-5-5). For 50ns is (-4,-2,0,2,4) 
#process.ecalMultiFitUncalibRecHit.algoPSet.activeBXs              = cms.vint32(-5,-4,-3,-2,-1,0,1,2,3,4) #Are 10 (-5-5). For 50ns is (-4,-2,0,2,4) 
process.ecalMultiFitUncalibRecHitPi0.EBdigiCollection              = cms.InputTag('dummyHitsPi0', 'dummyBarrelDigisPi0', pname)
process.ecalMultiFitUncalibRecHitPi0.EEdigiCollection              = cms.InputTag('dummyHitsPi0', 'dummyEndcapDigisPi0', pname)

#eta ucalbirated rechits from multifit
import RecoLocalCalo.EcalRecProducers.ecalMultiFitUncalibRecHit_cfi
process.ecalMultiFitUncalibRecHitEta                               = RecoLocalCalo.EcalRecProducers.ecalMultiFitUncalibRecHit_cfi.ecalMultiFitUncalibRecHit.clone()
process.ecalMultiFitUncalibRecHitEta.algoPSet.useLumiInfoRunHeader = cms.bool( False ) # To read the conditions from the header 
process.ecalMultiFitUncalibRecHitEta.algoPSet.activeBXs            = cms.vint32(-4,-2,0,2,4) #Are 10 (-5-5). For 50ns is (-4,-2,0,2,4) #No .algoPSet. in old releases
#    process.ecalMultiFitUncalibRecHit.algoPSet.activeBXs          = cms.vint32(-5,-4,-3,-2,-1,0,1,2,3,4) #Are 10 (-5-5). For 50ns is (-4,-2,0,2,4) #No .algoPSet. in old releases
process.ecalMultiFitUncalibRecHitEta.EBdigiCollection              = cms.InputTag('dummyHitsEta', 'dummyBarrelDigisEta', pname)
process.ecalMultiFitUncalibRecHitEta.EEdigiCollection              = cms.InputTag('dummyHitsEta', 'dummyEndcapDigisEta', pname)

# pi0 ecal rechits from uncalib
from RecoLocalCalo.EcalRecProducers.ecalRecHit_cfi import *
process.ecalDetIdToBeRecovered                  = RecoLocalCalo.EcalRecProducers.ecalDetIdToBeRecovered_cfi.ecalDetIdToBeRecovered.clone()
process.ecalRecHitPi0                           = RecoLocalCalo.EcalRecProducers.ecalRecHit_cfi.ecalRecHit.clone()
process.ecalRecHitPi0.killDeadChannels          = cms.bool( False )
process.ecalRecHitPi0.recoverEBVFE              = cms.bool( False )
process.ecalRecHitPi0.recoverEEVFE              = cms.bool( False )
process.ecalRecHitPi0.recoverEBFE               = cms.bool( False )
process.ecalRecHitPi0.recoverEEFE               = cms.bool( False )
process.ecalRecHitPi0.recoverEEIsolatedChannels = cms.bool( False )
process.ecalRecHitPi0.recoverEBIsolatedChannels = cms.bool( False )
process.ecalRecHitPi0.EEuncalibRecHitCollection = cms.InputTag("ecalMultiFitUncalibRecHitPi0","EcalUncalibRecHitsEE")
process.ecalRecHitPi0.EBuncalibRecHitCollection = cms.InputTag("ecalMultiFitUncalibRecHitPi0","EcalUncalibRecHitsEB")

# eta ecal rechits from uncalib
from RecoLocalCalo.EcalRecProducers.ecalRecHit_cfi import *
#process.ecalDetIdToBeRecovered                  = RecoLocalCalo.EcalRecProducers.ecalDetIdToBeRecovered_cfi.ecalDetIdToBeRecovered.clone()
process.ecalRecHitEta                           = RecoLocalCalo.EcalRecProducers.ecalRecHit_cfi.ecalRecHit.clone()
process.ecalRecHitEta.killDeadChannels          = cms.bool( False )
process.ecalRecHitEta.recoverEBVFE              = cms.bool( False )
process.ecalRecHitEta.recoverEEVFE              = cms.bool( False )
process.ecalRecHitEta.recoverEBFE               = cms.bool( False )
process.ecalRecHitEta.recoverEEFE               = cms.bool( False )
process.ecalRecHitEta.recoverEEIsolatedChannels = cms.bool( False )
process.ecalRecHitEta.recoverEBIsolatedChannels = cms.bool( False )
process.ecalRecHitEta.EEuncalibRecHitCollection = cms.InputTag("ecalMultiFitUncalibRecHitEta","EcalUncalibRecHitsEE")
process.ecalRecHitEta.EBuncalibRecHitCollection = cms.InputTag("ecalMultiFitUncalibRecHitEta","EcalUncalibRecHitsEB")

process.pizeroClusters = cms.EDProducer( "EgammaHLTNxNClusterProducer",
    statusLevelRecHitsToUse = cms.int32( 1 ),
    barrelClusterCollection = cms.string( "Simple3x3ClustersBarrel" ),
    flagLevelRecHitsToUse   = cms.int32( 1 ),
    maxNumberofClusters     = cms.int32( 99999 ),
    clusPhiSize             = cms.int32( 3 ),
    posCalcParameters       = cms.PSet(
      T0_barl               = cms.double( 7.4 ),
      LogWeighted           = cms.bool( True ),
      T0_endc               = cms.double( 3.1 ),
      T0_endcPresh          = cms.double( 1.2 ),
      W0                    = cms.double( 4.2 ),
      X0                    = cms.double( 0.89 )
    ),
    clusEtaSize             = cms.int32( 3 ),
    useRecoFlag             = cms.bool( False ),
    endcapHitProducer       = cms.InputTag('ecalRecHitPi0', 'EcalRecHitsEE', pname),
    maxNumberofSeeds        = cms.int32( 99999 ),
    useDBStatus             = cms.bool( True ),
    debugLevel              = cms.int32( debug_level ),
    barrelHitProducer       = cms.InputTag('ecalRecHitPi0', 'EcalRecHitsEB', pname),
    clusSeedThrEndCap       = cms.double( 1.0 ),
    clusSeedThr             = cms.double( 0.5 ),
    doEndcaps               = cms.bool( True ),
    endcapClusterCollection = cms.string( "Simple3x3ClustersEndcap" ),
    doBarrel                = cms.bool( True )
)

process.etaClusters         = cms.EDProducer( "EgammaHLTNxNClusterProducer",
    statusLevelRecHitsToUse = cms.int32( 1 ),
    barrelClusterCollection = cms.string( "Simple3x3ClustersBarrel" ),
    flagLevelRecHitsToUse   = cms.int32( 1 ),
    maxNumberofClusters     = cms.int32( 99999 ),
    clusPhiSize             = cms.int32( 3 ),
    posCalcParameters       = cms.PSet(
      T0_barl               = cms.double( 7.4 ),
      LogWeighted           = cms.bool( True ),
      T0_endc               = cms.double( 3.1 ),
      T0_endcPresh          = cms.double( 1.2 ),
      W0                    = cms.double( 4.2 ),
      X0                    = cms.double( 0.89 )
    ),
    clusEtaSize             = cms.int32( 3 ),
    useRecoFlag             = cms.bool( False ),
    endcapHitProducer       = cms.InputTag('ecalRecHitEta', 'EcalRecHitsEE' ,pname),
    maxNumberofSeeds        = cms.int32( 99999 ),
    useDBStatus             = cms.bool( True ),
    debugLevel              = cms.int32( debug_level ),
    barrelHitProducer       = cms.InputTag('ecalRecHitEta', 'EcalRecHitsEB' ,pname),
    clusSeedThrEndCap       = cms.double( 1.0 ),
    clusSeedThr             = cms.double( 0.5 ),
    doEndcaps               = cms.bool( True ),
    endcapClusterCollection = cms.string( "Simple3x3ClustersEndcap" ),
    doBarrel                = cms.bool( True )
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

process.reco_ecal = cms.Path( process.dummyHitsPi0 + process.ecalMultiFitUncalibRecHitPi0 + process.ecalRecHitPi0 +  process.dummyHitsEta + process.ecalMultiFitUncalibRecHitEta + process.ecalRecHitEta)
process.ALCAP0Output = cms.EndPath(process.dummyHitsEta + process.pizeroClusters +  process.etaClusters + process.reclusterpi0eb  + process.reclusteretaeb + process.reclusterpi0ee + process.reclusteretaee ) 
#process.ALCAP0Output = cms.EndPath(process.pizeroClusters + process.reclusterpi0eb) 

process.HLTSchedule = cms.Schedule( *( process.reco_ecal, process.ALCAP0Output ))

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

process.source = cms.Source( "PoolSource", fileNames  = cms.untracked.vstring(
'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/AlCaP0/RAW/v1/000/246/081/00000/0E4B40DE-5505-E511-8FC7-02163E013518.root',
'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/AlCaP0/RAW/v1/000/246/084/00000/3EDDF9A5-5805-E511-813C-02163E01470E.root',
'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/AlCaP0/RAW/v1/000/246/086/00000/B87D70C4-5D05-E511-8336-02163E013979.root',
'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/AlCaP0/RAW/v1/000/246/090/00000/466ED84A-6405-E511-9557-02163E0135BE.root',
'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/AlCaP0/RAW/v1/000/246/091/00000/52D98E4E-6505-E511-94D8-02163E0133E8.root',
'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/AlCaP0/RAW/v1/000/246/092/00000/34470235-7005-E511-8D40-02163E0142DF.root',
'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/AlCaP0/RAW/v1/000/246/286/00000/AC9A286C-B406-E511-9D72-02163E0142EA.root',
'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/AlCaP0/RAW/v1/000/246/305/00000/C838E9C6-B606-E511-9F3F-02163E01427A.root',
'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/AlCaP0/RAW/v1/000/246/310/00000/0EF1A960-C206-E511-9743-02163E011D7B.root',
'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/AlCaP0/RAW/v1/000/246/310/00000/76BABB09-C206-E511-8434-02163E014384.root',
'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/AlCaP0/RAW/v1/000/246/310/00000/92E8DBB2-C206-E511-B8EA-02163E01185C.root',
'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/AlCaP0/RAW/v1/000/246/310/00000/BE05C959-C206-E511-AAA0-02163E012434.root',
'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/AlCaP0/RAW/v1/000/246/316/00000/B0C3F426-C906-E511-B34F-02163E011DC2.root',
'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/AlCaP0/RAW/v1/000/246/316/00000/C26E0C2F-C906-E511-AAA8-02163E0141F7.root',
'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/AlCaP0/RAW/v1/000/246/317/00000/DED001C4-C506-E511-A15C-02163E0118C6.root',
'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/AlCaP0/RAW/v1/000/246/318/00000/40808F46-CC06-E511-B962-02163E013788.root',
'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/AlCaP0/RAW/v1/000/246/318/00000/9E8D0212-CD06-E511-8BB3-02163E014609.root',
'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/AlCaP0/RAW/v1/000/246/319/00000/780DBD42-C906-E511-970C-02163E0146ED.root',
'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/AlCaP0/RAW/v1/000/246/320/00000/9E1867AA-CC06-E511-A5FD-02163E013596.root',
'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/AlCaP0/RAW/v1/000/246/321/00000/BA92C573-CD06-E511-A5A2-02163E012820.root',
'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/AlCaP0/RAW/v1/000/246/341/00000/0A5E1ABC-F106-E511-BC62-02163E01187D.root',
'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/AlCaP0/RAW/v1/000/246/341/00000/149E29ED-F306-E511-B741-02163E011DC2.root',
'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/AlCaP0/RAW/v1/000/246/341/00000/5A3CCCB8-F106-E511-8065-02163E01186F.root',
'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/AlCaP0/RAW/v1/000/246/341/00000/C6A76CBC-F306-E511-9958-02163E014610.root',
'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/AlCaP0/RAW/v1/000/246/342/00000/048ECF48-F906-E511-95AC-02163E011909.root',
'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/AlCaP0/RAW/v1/000/246/342/00000/0E0E617F-0107-E511-AC4E-02163E012A0D.root',
'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/AlCaP0/RAW/v1/000/246/342/00000/105C0E1E-F706-E511-928C-02163E012A86.root',
'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/AlCaP0/RAW/v1/000/246/342/00000/42872653-FC06-E511-8734-02163E0139C7.root',
'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/AlCaP0/RAW/v1/000/246/342/00000/48868576-0107-E511-8D31-02163E01452F.root',
'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/AlCaP0/RAW/v1/000/246/342/00000/78146169-FC06-E511-9FA0-02163E013490.root',
'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/AlCaP0/RAW/v1/000/246/342/00000/8293E528-F806-E511-B4C1-02163E01219E.root',
'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/AlCaP0/RAW/v1/000/246/342/00000/9EE2B590-FF06-E511-81D2-02163E0135ED.root',
'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/AlCaP0/RAW/v1/000/246/342/00000/A45865EB-F606-E511-9A4F-02163E0138F2.root',
'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/AlCaP0/RAW/v1/000/246/342/00000/B03B354D-FE06-E511-BC5E-02163E014212.root',
'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/AlCaP0/RAW/v1/000/246/342/00000/B27603F4-F606-E511-B204-02163E013678.root',
'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/AlCaP0/RAW/v1/000/246/342/00000/D022DDA0-0007-E511-BC49-02163E014185.root',
'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/AlCaP0/RAW/v1/000/246/342/00000/DE41D00D-FB06-E511-A6F1-02163E0138F2.root',
'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/AlCaP0/RAW/v1/000/246/342/00000/F001B78A-0107-E511-B0B7-02163E0127A2.root',
'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/AlCaP0/RAW/v1/000/246/342/00000/FA28465E-F506-E511-BF44-02163E011D36.root',
'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/AlCaP0/RAW/v1/000/246/345/00000/1CEF73A3-0807-E511-8E48-02163E0142EA.root',
'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/AlCaP0/RAW/v1/000/246/345/00000/58B5D16B-0807-E511-BF0D-02163E013653.root',
'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/AlCaP0/RAW/v1/000/246/345/00000/7C976761-0807-E511-8890-02163E011A81.root',
'file:/afs/cern.ch/user/h/hardenbr/eos/cms/store/data/Commissioning2015/AlCaP0/RAW/v1/000/246/345/00000/CA51F769-0807-E511-B4E7-02163E0134CC.root'
      ))

# limit the number of events to be processed
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32( -1 )
)

# enable the TrigReport and TimeReport
process.options = cms.untracked.PSet(
#    SkipEvent = cms.untracked.vstring('ProductNotFound'),
    wantSummary = cms.untracked.bool( True )
)

# override the GlobalTag, connection string and pfnPrefix
if 'GlobalTag' in process.__dict__:
    from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag as customiseGlobalTag
    process.GlobalTag = customiseGlobalTag(process.GlobalTag, globaltag = 'GR_P_V54')
    process.GlobalTag.connect   = 'frontier://FrontierProd/CMS_CONDITIONS'
    process.GlobalTag.pfnPrefix = cms.untracked.string('frontier://FrontierProd/')
    for pset in process.GlobalTag.toGet.value():
        pset.connect = pset.connect.value().replace('frontier://FrontierProd/', 'frontier://FrontierProd/')
    # fix for multi-run processing
    process.GlobalTag.RefreshEachRun = cms.untracked.bool( False )
    process.GlobalTag.ReconnectEachRun = cms.untracked.bool( False )

