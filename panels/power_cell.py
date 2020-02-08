import wx

class PowerCellPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def OnPaint(self, e):
        dc = wx.PaintDC(self)
        brush = wx.Brush("red")
        dc.Clear()

        dc.SetBrush(brush)
        size = self.GetSize()
        size = min(size.width, size.height)
        dc.DrawCircle(size/2, size/2, size/2)
        
