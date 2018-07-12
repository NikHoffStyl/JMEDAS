from ROOT import *

gROOT.Macro("rootlogon.C")

f = TFile("ttbar.root")

h_areaAK4 = f.Get("h_areaAK4")
h_areaAK8 = f.Get("h_areaAK8")
h_areaAK8.SetLineStyle(4)
h_areaAK8.SetLineColor(4)

h_areaAK4.Scale( 1.0 / h_areaAK4.Integral() )
h_areaAK8.Scale( 1.0 / h_areaAK8.Integral() )

c = TCanvas('c', 'c')
h_areaAK4.Draw('hist')
h_areaAK8.Draw("hist same")

leg = gPad.BuildLegend(0.6, 0.5, 0.9, 0.7, "", "L")
leg.Draw()


c.Print('plots3.png', 'png')
c.Print('plots3.pdf', 'pdf')
