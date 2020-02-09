import wx

from app import DashboardApp
from dialogs import SystemDialog

class ControlButtonsPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.build()

    def build(self):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.SetSizer(sizer)

        self.autoButton = wx.Button(self, label="Autonomous")
        self.systemButton = wx.Button(self, label="System")
        self.systemButton.Bind(wx.EVT_BUTTON, self.on_system)

        self.miscButton = wx.Button(self, label="Miscellaneous")

        sizer.Add(self.autoButton, 1, flag=wx.CENTER)
        sizer.Add(self.systemButton, 1, flag=wx.CENTER)
        sizer.Add(self.miscButton, 1, flag=wx.CENTER)

    def on_system(self, event):
        config = DashboardApp.Get().config
        dlg = SystemDialog(self, config)
        dlg.ShowModal()
        dlg.Destroy()


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
