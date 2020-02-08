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

        sizer.Add(
            PowerCellPanel(self),
            1,
            flag=wx.EXPAND
        )

        sizer.Add(
            PowerCellPanel(self),
            1,
            flag=wx.EXPAND
        )        

        sizer.Add(
            PowerCellPanel(self),
            1,
            flag=wx.EXPAND
        )

        sizer.Add(
            PowerCellPanel(self),
            1,
            flag=wx.EXPAND
        )        

        sizer.Add(
            PowerCellPanel(self),
            1,
            flag=wx.EXPAND
        )