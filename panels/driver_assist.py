import wx

class DriverAssistPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.buildPanel()

    def buildPanel(self):
        self.SetBackgroundColour((0, 0, 255))
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        text = wx.StaticText(self, label="Driver Assist Panel", style=wx.ALIGN_CENTRE_HORIZONTAL | wx.ALIGN_CENTRE_VERTICAL)
        sizer.Add(text, 1, flag=wx.EXPAND)

        self.SetSizer(sizer)