import wx

class ButtonsPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.build()

    def build(self):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.SetSizer(sizer)

        self.autoButton = wx.Button(self, label="Autonomous")
        self.systemButton = wx.Button(self, label="System")
        self.miscButton = wx.Button(self, label="Miscellaneous")

        sizer.Add(self.autoButton, 1, flag=wx.CENTER)
        sizer.Add(self.systemButton, 1, flag=wx.CENTER)
        sizer.Add(self.miscButton, 1, flag=wx.CENTER)