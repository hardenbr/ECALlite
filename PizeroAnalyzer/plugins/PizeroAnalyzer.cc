// -*- C++ -*-
//
// Package:    ECALlite/PizeroAnalyzer
// Class:      PizeroAnalyzer
// 
/**\class PizeroAnalyzer PizeroAnalyzer.cc ECALlite/PizeroAnalyzer/plugins/PizeroAnalyzer.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Joshua Robert Hardenbrook
//         Created:  Fri, 29 May 2015 07:44:29 GMT
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

// root includes
#include "TFile.h"
#include "TH2F.h"
#include "TH1F.h"
#include "TTree.h"
#include "TMath.h"
#include "TVector3.h" 
#include "TLorentzVector.h" 

#include "DataFormats/CaloRecHit/interface/CaloCluster.h"
#include "DataFormats/CaloRecHit/interface/CaloClusterFwd.h"
#include "DataFormats/Math/interface/LorentzVector.h"

//
// class declaration
//

class PizeroAnalyzer : public edm::EDAnalyzer {
public:
  explicit	PizeroAnalyzer(const edm::ParameterSet&);
  ~PizeroAnalyzer();
  
  static void   fillDescriptions(edm::ConfigurationDescriptions& descriptions);
  void fillHandles(const edm::Event &);

private:
  virtual void beginJob() override;
  virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
  virtual void endJob() override;
  
  static const int MAX_PIZ = 2000;

  int nPi0;
  int isBar;

  // momentum
  float mPi0[MAX_PIZ];
  float ptPi0[MAX_PIZ];
  float ptG1[MAX_PIZ];
  float ptG2[MAX_PIZ];
  // energies
  float eG1[MAX_PIZ];
  float eG2[MAX_PIZ];

  // cartesian position
  float xG1[MAX_PIZ];
  float xG2[MAX_PIZ];
  float yG1[MAX_PIZ];
  float yG2[MAX_PIZ];
  float zG1[MAX_PIZ];
  float zG2[MAX_PIZ];

  // eta phi positioning
  float etaPi0[MAX_PIZ];
  float phiPi0[MAX_PIZ];
  float etaG1[MAX_PIZ];
  float phiG1[MAX_PIZ];
  float etaG2[MAX_PIZ];
  float phiG2[MAX_PIZ];

  TTree* pizTree_;
  TTree* eventTree_;

  edm::InputTag tag_barClusters_, tag_endClusters_;

  edm::Handle<reco::CaloClusterCollection> barClusters;
  edm::Handle<reco::CaloClusterCollection> endClusters;

  TFile * outputFile_;
  std::string outputFileName_;
  std::string pizTreeName_;

  float run, lumi, event;

  int debug_;
  bool doEta_, doEnd_, isMC_;
};

PizeroAnalyzer::PizeroAnalyzer(const edm::ParameterSet& iConfig)
{
   // output information
   outputFileName_  = iConfig.getUntrackedParameter<std::string>("outputFileName");
   pizTreeName_	    = iConfig.getUntrackedParameter<std::string>("treeName");
   debug_	    = iConfig.getUntrackedParameter<int>("debug");   
   // sample flags
   isMC_	    = iConfig.getUntrackedParameter<bool>("isMC"); 
   // split by regions
   doEta_	    = iConfig.getUntrackedParameter<bool>("doEta"); 
   doEnd_	    = iConfig.getUntrackedParameter<bool>("doEnd");
   // barrel and endcap cluster tags 
   tag_barClusters_ = iConfig.getUntrackedParameter<edm::InputTag>("barrelClusters");
   tag_endClusters_ = iConfig.getUntrackedParameter<edm::InputTag>("endClusters");   
}

PizeroAnalyzer::~PizeroAnalyzer()
{
 
}

//
// member functions
//

// ------------ method called for each event  ------------
void PizeroAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;
  fillHandles(iEvent);

  reco::CaloClusterCollection clusters = *(barClusters.product());
  if(doEnd_) clusters = *(endClusters.product());

  const float minMass = doEta_ ? 0.20 : 0.05;
  const float maxMass = doEta_ ? 0.50 : 0.15;      

  nPi0	= 0;
  isBar = doEnd_ ? 0 : 1;

  std::vector<reco::CaloCluster>::const_iterator candIter1 = clusters.begin();
  std::vector<reco::CaloCluster>::const_iterator candIter2 = clusters.begin();


  run   = iEvent.id().run();
  lumi  = iEvent.id().luminosityBlock();
  event = iEvent.id().event();

  for(; candIter1 != clusters.end(); ++candIter1) {
    for(; candIter2 != clusters.end(); ++candIter2) {
      if (candIter1 == candIter2) continue;
	 
      // calculate the pt for 1
      float eG1_temp   = candIter1->energy();	 
      float etaG1_temp = candIter1->position().eta();
      float phiG1_temp = candIter1->position().phi();
      float theta1     = 2.*atan(exp(-etaG1_temp));
      float ptG1_temp  = eG1_temp*sin(theta1);

      // calculate the pt for 2
      float eG2_temp   = candIter2->energy();	 
      float etaG2_temp = candIter2->position().eta();
      float phiG2_temp = candIter2->position().phi();
      float theta2     = 2.*atan(exp(-etaG2_temp));
      float ptG2_temp  = eG2_temp*sin(theta2);

      TLorentzVector g1, g2;
      g1.SetPtEtaPhiM(ptG1_temp, etaG1_temp, phiG1_temp, 0);
      g2.SetPtEtaPhiM(ptG2_temp, etaG2_temp, phiG2_temp, 0);


      if(debug_ > 1) std::cout << "e1: "<< eG1_temp << " e2: " << eG2_temp << std::endl;

      if(debug_ > 1) std::cout << "pt1: "<< ptG1_temp << 
		       " pt2: " << ptG2_temp << " etaG1 " << etaG1_temp << " etaG2 " << etaG2_temp 
			       << " phiG1 " << phiG1_temp << " phi G2 " << phiG2_temp << std::endl;


      TLorentzVector pi0 = g1 + g2;

      if(debug_ > 1) std::cout << "mass: " << pi0.M() << std::endl;

      // apply a mass window cut
      if (pi0.M() > maxMass || pi0.M() < minMass) continue;

      if(debug_ > 1) std::cout << "pt1: "<< ptG1_temp << 
		       " pt2: " << ptG2_temp << " ptPi0 " << pi0.Pt()
			      << " mPi0 " << pi0.M() << std::endl;


      // kinematics
      mPi0[nPi0]   = pi0.M();
      ptPi0[nPi0]  = pi0.Pt();
      etaPi0[nPi0] = pi0.Eta();
      phiPi0[nPi0] = pi0.Phi();
      // candidates
      eG1[nPi0]    = eG1_temp;
      eG2[nPi0]    = eG2_temp;
      ptG1[nPi0]   = ptG1_temp;
      ptG2[nPi0]   = ptG2_temp;
      // eta phi position
      etaG1[nPi0]  = etaG1_temp;
      etaG2[nPi0]  = etaG2_temp;
      phiG1[nPi0]  = phiG1_temp;
      phiG2[nPi0]  = phiG2_temp;	 
      // absolute position
      // g1
      xG1[nPi0]    = candIter1->x();
      yG1[nPi0]    = candIter1->y();
      zG1[nPi0]    = candIter1->z();
      // g2
      xG2[nPi0]    = candIter2->x();
      yG2[nPi0]    = candIter2->y();
      zG2[nPi0]    = candIter2->z();
	 
      nPi0++;	 	 
    }
  }

  if(nPi0 > 0) {
    if(debug_ > 1) std::cout << " Filling Tree " << nPi0 << std::endl;
    pizTree_->Fill();
  }
  else {
    if(debug_ > 1) std::cout << "Not Filing Tree nPi0: " << nPi0 << std::endl;
  }
}

void PizeroAnalyzer::beginJob()
{
  outputFile_ = new TFile(outputFileName_.c_str(), "RECREATE");
  pizTree_    = new TTree(pizTreeName_.c_str(), "pizero tree");
  eventTree_    = new TTree("eventInfo", "event info tree");

  eventTree_->Branch("run", &run, "run/I");
  eventTree_->Branch("lumi", &lumi, "lumi/I");
  eventTree_->Branch("event", &event, "event/I");
  eventTree_->Branch("nPi0", &nPi0, "nPi0/I");
  // index 
  pizTree_->Branch("run", &run, "run/I");
  pizTree_->Branch("lumi", &lumi, "lumi/I");
  pizTree_->Branch("event", &event, "event/I");

  pizTree_->Branch("nPi0", &nPi0, "nPi0/I");

  // kinematics
  pizTree_->Branch("mPi0", &mPi0, "mPi0[nPi0]/F");
  pizTree_->Branch("ptPi0",&ptPi0, "ptPi0[nPi0]/F");
  pizTree_->Branch("ptG1", &ptG1, "ptG1[nPi0]/F");
  pizTree_->Branch("ptG2", &ptG2, "ptG2[nPi0]/F");
  pizTree_->Branch("eG1",  &eG1, "eG1[nPi0]/F");
  pizTree_->Branch("eG2",  &eG2, "eG2[nPi0]/F");

  // position
  pizTree_->Branch("xG1", &xG1, "xG1[nPi0]/F");
  pizTree_->Branch("xG2", &xG2, "xG2[nPi0]/F");
  pizTree_->Branch("yG1", &yG1, "yG1[nPi0]/F");
  pizTree_->Branch("yG2", &yG2, "yG2[nPi0]/F");
  pizTree_->Branch("zG1", &zG1, "zG1[nPi0]/F");
  pizTree_->Branch("zG2", &zG2, "zG2[nPi0]/F");

  // eta phi position
  pizTree_->Branch("etaPi0", &etaPi0, "etaPi0[nPi0]/F");
  pizTree_->Branch("phiPi0", &etaPi0, "phiPi0[nPi0]/F");
  pizTree_->Branch("etaG1", &etaG1, "etaG1[nPi0]/F");
  pizTree_->Branch("phiG1", &etaG1, "phiG1[nPi0]/F");
  pizTree_->Branch("etaG2", &etaG2, "etaG2[nPi0]/F");
  pizTree_->Branch("phiG2", &etaG2, "phiG2[nPi0]/F");
}


void PizeroAnalyzer::endJob() 
{
  pizTree_->Write();
  eventTree_->Write();
  outputFile_->Close();
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void PizeroAnalyzer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}


void PizeroAnalyzer::fillHandles(const edm::Event & iEvent ) {
  if(!doEnd_)iEvent.getByLabel(tag_barClusters_, barClusters); 
  if(doEnd_) iEvent.getByLabel(tag_endClusters_, endClusters);
}

//define this as a plug-in
DEFINE_FWK_MODULE(PizeroAnalyzer);
