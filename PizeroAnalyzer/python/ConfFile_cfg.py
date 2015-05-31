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

process.basic                = cms.EDAnalyzer('PizeroAnalyzer')
process.basic.outputFileName = cms.untracked.string('pizero.root')
process.basic.treeName       = cms.untracked.string('barrel')
process.basic.debug          = cms.untracked.int32(10)
process.basic.doEta          = cms.untracked.bool(True)
process.basic.doEnd          = cms.untracked.bool(False)
process.basic.isMC           = cms.untracked.bool(True)
process.basic.barrelClusters = cms.untracked.InputTag("hltSimple3x3Clusters","Simple3x3ClustersBarrel","TEST")
process.basic.endClusters    = cms.untracked.InputTag("hltSimple3x3Clusters","Simple3x3ClustersEndcap","TEST")

process.p = cms.Path(process.basic)
