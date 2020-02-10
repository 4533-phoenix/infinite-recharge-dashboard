import wx
from app import DashboardApp

class AutoDialog(wx.Dialog):
    def __init__(self, parent, config):
        super().__init__(parent, title="Autonomous Select")
        self.config = config
        self.build()
    
    def build(self):
        sizer = wx.BoxSizer(wx.VERTICAL)
        dropDownPanel = self.createAutoPanel(self)
        sizer.Add(dropDownPanel, 1, border=5, flag=wx.ALL | wx.EXPAND)

        buttonSizer = self.CreateButtonSizer(wx.OK | wx.CANCEL)
        sizer.Add(buttonSizer, 0, border=5, flag=wx.ALL | wx.EXPAND)

        self.SetSizer(sizer)
        self.Fit()
    
    def createAutoPanel(self, parent):
        panel = wx.Panel(parent)
        sizer = wx.BoxSizer(wx.VERTICAL)
        panel.SetSizer(sizer)

        auto_modes = [mode['name'] for mode in self.config.auto_modes]

        dropDown = wx.ComboBox(panel, choices=auto_modes, style=wx.CB_READONLY)
        sizer.Add(dropDown, 0, border=5, flag=wx.ALL | wx.EXPAND)
        
        modes = list(self.config.auto_modes)[0]['modes']
        print(modes)
        rBox = wx.ListBox(panel, choices=[mode['display_name'] for mode in modes], style=wx.LB_SINGLE)
        sizer.Add(rBox, 1, border=5, flag=wx.ALL | wx.EXPAND)

        return panel