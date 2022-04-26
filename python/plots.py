import sys, os, glob, shutil, json, math, re, random, time
import ROOT
import functions

ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetOptTitle(0)


def drawAux(c, left = "#bf{FCCee} Delphes Simulation", right="#sqrt{s} = 240 GeV"):
    
    textLeft = ROOT.TLatex()
    textLeft.SetTextFont(42)
    textLeft.SetTextSize(0.04)
    textLeft.SetNDC()
    textLeft.DrawLatex(c.GetLeftMargin(), 0.96, left)
        
    textRight = ROOT.TLatex()
    textRight.SetNDC()
    textRight.SetTextFont(42)
    textRight.SetTextSize(0.04)
    textRight.SetTextAlign(31)
    textRight.DrawLatex(1.0-c.GetRightMargin(), 0.96, right)

if __name__ == "__main__":

    outDir = "/eos/user/j/jaeyserm/www/FCCee/ZH_Zinv/"

    outFiles = ["output/vvbb_Base.root", "output/vvbb_CaloCMS.root", "output/vvbb_TrkCLD.root"]
    labels = ["IDEA baseline", "IDEA + CMS calo", "IDEA + CLD Tracker"]
    colors = [ROOT.kBlack, ROOT.kRed, ROOT.kBlue]
    
    fIns = [ROOT.TFile(x) for x in outFiles]

    

    c = ROOT.TCanvas("c", "", 800, 800)
    c.SetLeftMargin(0.12)
    c.SetRightMargin(0.05)
    c.SetTopMargin(0.05)
    c.SetBottomMargin(0.1)

    # plot invariant mass of PF candidates
    c.cd()
    c.Clear()

    leg = ROOT.TLegend(.15, 0.75, .4, .93)
    leg.SetBorderSize(0)
    leg.SetTextSize(0.03)
    leg.SetFillStyle(0)
        
    for i in range(0, len(fIns)):

        h = fIns[i].Get("pf_m")
        h.SetLineColor(colors[i])
        h.SetLineWidth(2)
        h.GetYaxis().SetRangeUser(0, 1.2*h.GetMaximum())
        
        leg.AddEntry(h, labels[i], "L")
        
        if i == 0:
        
            h.GetXaxis().SetRangeUser(0, 200)
            h.GetXaxis().SetTitle("Mass PF candidates (GeV)")
            h.GetXaxis().SetTitleOffset(1.2)
            h.GetXaxis().SetLabelOffset(0.005)
            h.GetYaxis().SetTitle("Events")   
            h.GetYaxis().SetTitleOffset(1.8)
            h.GetYaxis().SetLabelOffset(0.005)
            h.Draw("HIST")
        
        else: h.Draw("HIST SAME")
        
    leg.Draw()
    drawAux(c)
   
    c.SaveAs("%s/pf_m.png" % outDir) 
    c.SaveAs("%s/pf_m.pdf" % outDir) 
 
 
    # plot recoil
    c.cd()
    c.Clear()

    leg = ROOT.TLegend(.15, 0.75, .4, .93)
    leg.SetBorderSize(0)
    leg.SetTextSize(0.03)
    leg.SetFillStyle(0)
        
    for i in range(0, len(fIns)):

        h = fIns[i].Get("recoil")
        h.SetLineColor(colors[i])
        h.SetLineWidth(2)
        h.GetYaxis().SetRangeUser(0, 1.2*h.GetMaximum())
        
        leg.AddEntry(h, labels[i], "L")
        
        if i == 0:
        
            h.GetXaxis().SetRangeUser(0, 200)
            h.GetXaxis().SetTitle("Recoil (GeV)")
            h.GetXaxis().SetTitleOffset(1.2)
            h.GetXaxis().SetLabelOffset(0.005)
            h.GetYaxis().SetTitle("Events")   
            h.GetYaxis().SetTitleOffset(1.8)
            h.GetYaxis().SetLabelOffset(0.005)
            h.Draw("HIST")
        
        else: h.Draw("HIST SAME")
        
    leg.Draw()
    drawAux(c)
   
    c.SaveAs("%s/recoil.png" % outDir) 
    c.SaveAs("%s/recoil.pdf" % outDir) 
    
    
    # visible energy
    c.cd()
    c.Clear()

    leg = ROOT.TLegend(.15, 0.75, .4, .93)
    leg.SetBorderSize(0)
    leg.SetTextSize(0.03)
    leg.SetFillStyle(0)
        
    for i in range(0, len(fIns)):

        h = fIns[i].Get("energy_vis")
        h.SetLineColor(colors[i])
        h.SetLineWidth(2)
        h.GetYaxis().SetRangeUser(0, 1.2*h.GetMaximum())
        
        leg.AddEntry(h, labels[i], "L")
        
        if i == 0:
        
            h.GetXaxis().SetRangeUser(0, 200)
            h.GetXaxis().SetTitle("Visible energy (GeV)")
            h.GetXaxis().SetTitleOffset(1.2)
            h.GetXaxis().SetLabelOffset(0.005)
            h.GetYaxis().SetTitle("Events")   
            h.GetYaxis().SetTitleOffset(1.8)
            h.GetYaxis().SetLabelOffset(0.005)
            h.Draw("HIST")
        
        else: h.Draw("HIST SAME")
        
    leg.Draw()
    drawAux(c)
   
    c.SaveAs("%s/energy_vis.png" % outDir) 
    c.SaveAs("%s/energy_vis.pdf" % outDir) 