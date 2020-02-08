import wx
from .power_cell import PowerCellPanel

class IntakeStatusPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.build()

    def build(self):
        self.SetBackgroundColour((0, 255, 255))

        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer)

        self.powercells = [
            PowerCellPanel(self),
            PowerCellPanel(self),
            PowerCellPanel(self),
            PowerCellPanel(self),
            PowerCellPanel(self)
        ]
        for pcp in self.powercells:
            sizer.Add(pcp, 1, flag=wx.EXPAND)
    
    def update(self, status):
        for i in range(len(status)):
            self.powercells[i].update(status[i])
    