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

        self.dropDown = wx.ComboBox(panel, choices=auto_groups, value=auto_selection['name'], style=wx.CB_READONLY)
        self.dropDown.Bind(wx.EVT_COMBOBOX, self.on_group_selected)
        sizer.Add(self.dropDown, 0, border=5, flag=wx.ALL | wx.EXPAND)

        auto_modes = self.config.get_auto_modes_by_group(self.dropDown.GetStringSelection())

        self.modesList = wx.ListBox(panel, choices=auto_modes, style=wx.LB_SINGLE)
        self.modesList.SetStringSelection(auto_selection['mode'])
        sizer.Add(self.modesList, 1, border=5, flag=wx.ALL | wx.EXPAND)

        self.setAutoButton = wx.Button(panel, label="Select Autonomous")
        self.setAutoButton.Bind(wx.EVT_BUTTON, self.on_set_auto)

        sizer.Add(self.setAutoButton, 0, flag=wx.CENTER | wx.EXPAND)        

        return panel

    def on_set_auto(self, event):
        self.config.set_selected_auto_group(self.dropDown.GetValue())
        self.config.set_selected_auto_mode(self.modesList.GetStringSelection())
        self.config.save()

    def on_group_selected(self, event):
        self.modesList.Clear()
        auto_modes = self.config.get_auto_modes_by_group(self.dropDown.GetStringSelection())
        self.modesList.Append(auto_modes)
        self.Refresh()