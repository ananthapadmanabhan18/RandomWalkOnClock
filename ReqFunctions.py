import ROOT

def set1DHist( 
                hist,
                xTitle: str, yTitle:str,
                xTitleOffset=1.05,  yTitleOffset=1.05,
                xLabelSize=0.05, yLabelSize=0.05,
                xTitleSize=0.05, yTitleSize=0.05,
                xMaxDigits=3, yMaxDigits=3,
                lineColor=ROOT.kBlack, lineWidth=1, lineStyle=1,
                markerColor=ROOT.kBlack, markerSize=0.7, markerStyle=21,
                ifCenterTitle: bool=True,
                title="",
                ifStats: bool=False,
                XnDivisions=1410,
                YnDivisions=1410,
            ):
    # Title Setup
    hist.SetTitle(title)
    hist.SetStats(ifStats)
    
    # Marker Setup
    hist.SetMarkerStyle(markerStyle)
    hist.SetMarkerSize(markerSize)
    hist.SetMarkerColor(markerColor)
    
    # Line Setup
    hist.SetLineColor(lineColor)
    hist.SetLineStyle(lineStyle)
    hist.SetLineWidth(lineWidth)
    
    # Axis Setup
    hist.GetXaxis().SetTitle(xTitle)
    hist.GetYaxis().SetTitle(yTitle)
    hist.GetXaxis().SetTitleFont(42)
    hist.GetYaxis().SetTitleFont(42)
    hist.GetXaxis().SetLabelFont(42)
    hist.GetYaxis().SetLabelFont(42)
    hist.GetYaxis().SetTitleOffset(yTitleOffset)
    hist.GetXaxis().SetTitleOffset(xTitleOffset)
    hist.GetXaxis().SetTitleSize(xTitleSize)
    hist.GetYaxis().SetTitleSize(yTitleSize)
    hist.GetXaxis().SetLabelSize(xLabelSize)
    hist.GetYaxis().SetLabelSize(yLabelSize)
    hist.GetXaxis().SetTickLength(0.015)
    hist.GetYaxis().SetTickLength(0.015)
    if ifCenterTitle:
        hist.GetXaxis().CenterTitle()
        hist.GetYaxis().CenterTitle()
    hist.GetXaxis().SetMaxDigits(xMaxDigits) 
    hist.GetYaxis().SetMaxDigits(yMaxDigits)   
    hist.GetXaxis().SetNdivisions(XnDivisions)
    hist.GetYaxis().SetNdivisions(YnDivisions)  
    return hist


def set1Dcanvas(canvas,
                TopMargin : float=0.025, BottomMargin : float=0.12, 
                LeftMargin : float=0.11, RightMargin : float=0.0175,
                ifLogY : bool=False,ifLogX : bool=False,
                ifGrid : bool=False,                
):
    canvas.SetLeftMargin(LeftMargin)
    canvas.SetBottomMargin(BottomMargin)
    canvas.SetRightMargin(RightMargin)
    canvas.SetTopMargin(TopMargin)  
    canvas.SetTickx(1)
    canvas.SetTicky(1)
    if ifGrid:
        canvas.SetGrid()
    if ifLogX:
        canvas.SetLogx()        
    if ifLogY:
        canvas.SetLogy()

    return canvas

















