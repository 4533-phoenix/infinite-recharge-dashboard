import wx

class PowerCellPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.On = False

        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.On = False

    def OnSize(self, e):
        self.Refresh()

    def OnPaint(self, e):
        dc = wx.PaintDC(self)

        if self.On:
            brush = wx.Brush("yellow")
        else:
            brush = wx.Brush("red")

        dc.SetBrush(brush)

        size = self.GetSize()
        radius = min(size.width, size.height)/2
        center = wx.Point(size.width/2, size.height/2)
        dc.DrawCircle(center.x, center.y, radius * .8)

    def update(self, status):
        self.On = status
        self.Refresh()
