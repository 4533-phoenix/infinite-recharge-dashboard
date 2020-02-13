import wx
from app import DashboardApp

class AutoChooserPanel(wx.Panel):
    def __init__(self, parent, config):
        wx.Panel.__init__(self, parent)
        self.config = config
        self.build()

    def build(self):
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer)

        dropDownPanel = self.createAutoPanel(self)
        sizer.Add(dropDownPanel, 1, border=5, flag=wx.ALL | wx.EXPAND)


    def createAutoPanel(self, parent):
        panel = wx.Panel(parent)
        sizer = wx.BoxSizer(wx.VERTICAL)
        panel.SetSizer(sizer)

        auto_selection = self.config.get_auto_selection()
        auto_groups = self.config.get_auto_mode_groups()

        dropDown = wx.ComboBox(panel, choices=auto_groups, value=auto_selection['name'], style=wx.CB_READONLY)
        sizer.Add(dropDown, 0, border=5, flag=wx.ALL | wx.EXPAND)

        auto_modes = self.config.get_auto_modes_by_group(dropDown.GetStringSelection())

        modesList = wx.ListBox(panel, choices=auto_modes, style=wx.LB_SINGLE)
        modesList.SetStringSelection(auto_selection['mode'])
        sizer.Add(modesList, 1, border=5, flag=wx.ALL | wx.EXPAND)

        self.setAutoButton = wx.Button(panel, label="Select Autonomous")

        sizer.Add(self.setAutoButton, 0, flag=wx.CENTER | wx.EXPAND)        

        return panel