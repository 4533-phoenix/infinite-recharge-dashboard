import wx

class CameraButtonsPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.build()
    def build(self):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.SetSizer(sizer)

        self.oneButton = wx.Button(self, label="Camera 1")
        self.twoButton = wx.Button(self, label="Camera 2")
        self.threeButton = wx.Button(self, label="Camera 3")

        sizer.Add(self.oneButton, 1, flag=wx.CENTER)
        sizer.Add(self.twoButton, 1, flag=wx.CENTER)
        sizer.Add(self.threeButton, 1, flag=wx.CENTER)