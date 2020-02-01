import wx

class GameTimerPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.buildPanel()

    def buildPanel(self):
        self.SetBackgroundColour((255,0,0))

        sizer = wx.BoxSizer(wx.HORIZONTAL)

        text = wx.StaticText(self, label="Game Timer", style=wx.ALIGN_CENTRE_HORIZONTAL)
        sizer.Add(text, 1, flag=wx.EXPAND)

        self.SetSizer(sizer)