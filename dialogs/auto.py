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

        auto_selection = self.config.get_auto_selection()
        auto_groups = self.config.get_auto_mode_groups()

        dropDown = wx.ComboBox(panel, choices=auto_groups, value=auto_selection['name'], style=wx.CB_READONLY)
        sizer.Add(dropDown, 0, border=5, flag=wx.ALL | wx.EXPAND)

        auto_modes = self.config.get_auto_modes_by_group(dropDown.GetStringSelection())

        modesList = wx.ListBox(panel, choices=auto_modes, style=wx.LB_SINGLE)
        modesList.SetStringSelection(auto_selection['mode'])
        sizer.Add(modesList, 1, border=5, flag=wx.ALL | wx.EXPAND)

        return panel
