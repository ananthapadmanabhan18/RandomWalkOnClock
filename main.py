import random
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import ROOT
from ReqFunctions import *
from tqdm import trange

ROOT.gROOT.SetBatch(True)





# Generating random steps and filling histogram for checking
step_histo = ROOT.TH1F("step_histo", "Step Histogram", 4, -2, 2)

for i in range(1000):
    step = random.choice([-1, 1])  
    step_histo.Fill(step*0.5)


step_histo = set1DHist(
                    step_histo, 
                    xTitle="Generated Step",
                    yTitle="Counts",
                    lineColor=ROOT.kBlack,
                    lineWidth=2,
                    markerStyle=21,
                    markerColor=ROOT.kBlack,
                    markerSize=1.75,
                    yMaxDigits=4,
                    xTitleOffset=0.8,
                    xLabelSize=0.05,
                    yTitleOffset=0,
                    )

binLabel=[-3, -1, 1, 3]
for i in range(1, step_histo.GetNbinsX()+1):
    step_histo.GetXaxis().SetBinLabel(i, str(binLabel[i-1]))
    


oldCanvas = ROOT.gROOT.FindObject("canvas") 
if oldCanvas:
    oldCanvas.Close()
canvas = ROOT.TCanvas("canvas", "canvas", 600, 600)
canvas = set1Dcanvas(canvas,ifLogY=False,TopMargin=0.06, LeftMargin=0.15, BottomMargin=0.1)
canvas.cd()
step_histo.Draw()
canvas.SaveAs("Results/StepHistogram.png")
    
    
# Running the random walk on a clock and filling the probability histogram
clock  = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
nEvents = 100000
prob_hist = ROOT.TH1F("prob_hist", "Probability Histogram", 13, 0, 13)
for i in trange(nEvents): 
    curr_pos = 11
    covered_positions = [clock[curr_pos]]
    unique_covered = covered_positions.copy()
    while len(unique_covered) < 12:
        step = random.choice([-1, 1])
        step_histo.Fill(step)
        next_pos = (curr_pos + step) % 12
        covered_positions.append(clock[curr_pos])
        unique_covered = list(dict.fromkeys(covered_positions))
        curr_pos = next_pos
    last_pos = unique_covered[-1]
    prob_hist.Fill(last_pos)
    
    
# plotting the probability histogram
prob_hist = set1DHist(
                    prob_hist,
                    xTitle="Last Covered Position",
                    yTitle="Probability",
                    lineColor=ROOT.kBlue,
                    lineWidth=2,    
                    markerStyle=25,
                    markerColor=ROOT.kBlue,
                    markerSize=1.4,
                    yMaxDigits=1,   
                    XnDivisions=411,
                    xLabelSize=0.05,
                    xTitleOffset=0.8,
                    yTitleOffset=1.3,
                    )

for i in range(1,prob_hist.GetNbinsX()+1):
    prob_hist.GetXaxis().SetBinLabel(i, str(i-1))
prob_hist.Scale(1.0/prob_hist.Integral())
prob_hist.GetYaxis().SetRangeUser(prob_hist.GetMaximum()*0.8, prob_hist.GetMaximum()*1.2)

oldCanvas2 = ROOT.gROOT.FindObject("canvas2") 
if oldCanvas2:
    oldCanvas2.Close()
canvas2 = ROOT.TCanvas("canvas2", "canvas2", 900, 600)
canvas2 = set1Dcanvas(canvas2,ifLogY=False,TopMargin=0.06, LeftMargin=0.15, BottomMargin=0.1)
canvas2.cd()    
prob_hist.Draw()
canvas2.Draw()


for i in range(1,prob_hist.GetNbinsX()+1):
    prob_hist.GetXaxis().SetBinLabel(i, str(i-1))


oldCanvas2 = ROOT.gROOT.FindObject("canvas2") 
if oldCanvas2:
    oldCanvas2.Close()
    
canvas2 = ROOT.TCanvas("canvas2", "canvas2", 900, 600)
canvas2 = set1Dcanvas(canvas2,ifLogY=False,TopMargin=0.03, LeftMargin=0.15, BottomMargin=0.1)
canvas2.cd()    
prob_hist.Draw()
canvas2.SaveAs("Results/ProbabilityHistogram.png")
    