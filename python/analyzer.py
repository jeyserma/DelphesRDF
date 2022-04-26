import sys, os, glob, shutil, json, math, re, random, time, pathlib
import ROOT
import functions

ROOT.gSystem.Load("libDelphes")

ROOT.gInterpreter.AddIncludePath(os.path.dirname(__file__) + "/cc/")
ROOT.gInterpreter.Declare('#include "functions.h"')
ROOT.gInterpreter.Declare('#include "classes/DelphesClasses.h"')


def analyze(files, fOut):

    rdf = ROOT.RDataFrame("Delphes", files)
    

    rdf = rdf.Define("njets", "Jet_size")
    rdf = rdf.Filter("njets >= 2")
    
    ## reco
    rdf = rdf.Define("jet_pt", "Jet.PT")
    rdf = rdf.Define("jet_eta", "Jet.Eta")
    rdf = rdf.Define("jet_phi", "Jet.Phi")
    rdf = rdf.Define("jet_mass", "Jet.Mass")
    
    rdf = rdf.Define("jet1_mom4", "ROOT::Math::PtEtaPhiMVector(jet_pt[0], jet_eta[0], jet_phi[0], jet_mass[0])")
    rdf = rdf.Define("jet2_mom4", "ROOT::Math::PtEtaPhiMVector(jet_pt[1], jet_eta[1], jet_phi[1], jet_mass[1])")
    rdf = rdf.Define("dijet", "jet1_mom4 + jet2_mom4")
    rdf = rdf.Define("dijet_m", "dijet.M()")
    
    rdf = rdf.Define("jets_mom4", "sumP4(jet_pt, jet_eta, jet_phi, jet_mass)")
    rdf = rdf.Define("jets_m", "jets_mom4.M()")
    
    rdf = rdf.Define("ht", "sumScalar(jet_pt)")
    
    
    
    # PF candidates
    rdf = rdf.Define("pf_pt", "ParticleFlowCandidate.PT")
    rdf = rdf.Define("pf_eta", "ParticleFlowCandidate.Eta")
    rdf = rdf.Define("pf_phi", "ParticleFlowCandidate.Phi")
    rdf = rdf.Define("pf_mass", "ParticleFlowCandidate.Mass")
    rdf = rdf.Define("pf_energy", "computeEnergy(pf_pt, pf_eta, pf_phi, pf_mass)")
    rdf = rdf.Define("pfcand_mom4", "sumP4(pf_pt, pf_eta, pf_phi, pf_mass)")
    rdf = rdf.Define("pf_m", "pfcand_mom4.M()")
    
    rdf = rdf.Define("recoil", "recoil(240, pfcand_mom4)")
    rdf = rdf.Define("energy_vis", "sumScalar(pf_energy)")
    
    
    ## gen
    rdf = rdf.Define("genjet_pt", "GenJet.PT")
    rdf = rdf.Define("genjet_eta", "GenJet.Eta")
    rdf = rdf.Define("genjet_phi", "GenJet.Phi")
    rdf = rdf.Define("genjet_mass", "GenJet.Mass")
    
    rdf = rdf.Define("genjet1_mom4", "ROOT::Math::PtEtaPhiMVector(genjet_pt[0], genjet_eta[0], genjet_phi[0], genjet_mass[0])")
    rdf = rdf.Define("genjet2_mom4", "ROOT::Math::PtEtaPhiMVector(genjet_pt[1], genjet_eta[1], genjet_phi[1], genjet_mass[1])")
    rdf = rdf.Define("gendijet", "genjet1_mom4 + genjet2_mom4")
    rdf = rdf.Define("gendijet_m", "gendijet.M()")
    
    
    
    # make graphs and store
    graphs = []
    
    h_jet_pt = rdf.Histo1D(("jet_pt", "", 100, 0, 100), "jet_pt")
    h_dijet_m = rdf.Histo1D(("dijet_m", "", 200, 0, 200), "dijet_m")
    h_recoil = rdf.Histo1D(("recoil", "", 200, 0, 200), "recoil")
    h_ht = rdf.Histo1D(("ht", "", 300, 0, 300), "ht")
    h_njets = rdf.Histo1D(("njets", "", 10, 0, 10), "njets")
    h_pf_m = rdf.Histo1D(("pf_m", "", 200, 0, 200), "pf_m")
    h_jets_m = rdf.Histo1D(("jets_m", "", 200, 0, 200), "jets_m")
    h_energy_vis = rdf.Histo1D(("energy_vis", "", 300, 0, 300), "energy_vis")
    
    h_genjet_pt = rdf.Histo1D(("genjet_pt", "", 100, 0, 100), "genjet_pt")
    h_gendijet_m = rdf.Histo1D(("gendijet_m", "", 200, 0, 200), "gendijet_m")


    graphs.append(h_jet_pt)
    graphs.append(h_dijet_m)
    graphs.append(h_recoil)
    graphs.append(h_ht)
    graphs.append(h_njets)
    graphs.append(h_pf_m)
    graphs.append(h_jets_m)
    graphs.append(h_energy_vis)
    
    graphs.append(h_genjet_pt)
    graphs.append(h_gendijet_m)
    
    
  
    # execute the RDFs
    start_time = time.time()
    print("Executing the RDF")
    ROOT.RDF.RunGraphs(graphs)
    end_time = time.time()
    print("Finished in %d seconds" % (end_time-start_time))
    
    
    # save histograms
    fOut = ROOT.TFile(fOut, "RECREATE")
    for g in graphs: g.Write()
    fOut.Close()
    
    
    
    


if __name__ == "__main__":

    ## vvbb, IDEA base
    #files = functions.findFiles("/eos/experiment/fcc/ee/generation/DelphesStandalone/DetectorVariation_v0/vvbb_Base/vvbb_Base_0.root") # test 1 file
    files = functions.findFiles("/eos/experiment/fcc/ee/generation/DelphesStandalone/DetectorVariation_v0/vvbb_Base/")
    analyze(files, "output/vvbb_Base.root")
 
 
    ## vvbb, IDEA + CMS calorimeter
    files = functions.findFiles("/eos/experiment/fcc/ee/generation/DelphesStandalone/DetectorVariation_v0/vvbb_CaloCMS/")
    analyze(files, "output/vvbb_CaloCMS.root")
    
    ## vvbb, IDEA + Tracker CLD
    files = functions.findFiles("/eos/experiment/fcc/ee/generation/DelphesStandalone/DetectorVariation_v0/vvbb_TrkCLD/")
    analyze(files, "output/vvbb_TrkCLD.root")