import wx

class IntakeStatusPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.build()

    def build(self):
        self.SetBackgroundColour((0, 255, 255))

        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer)

        text = wx.StaticText(self,
            label="Intake",
            style=wx.ALIGN_CENTRE_HORIZONTAL
        )

        sizer.Add(text, 1, flag=wx.EXPAND)

