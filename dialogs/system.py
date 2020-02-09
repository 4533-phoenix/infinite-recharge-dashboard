import wx

from app import DashboardApp

class SystemDialog(wx.Dialog):
    def __init__(self, parent, config):
        super().__init__(parent, title="System")
        self.config = config
        self.build()

    def build(self):
        sizer = wx.BoxSizer(wx.VERTICAL)
        telemetryPanel = self.createTelemetryPanel(self)
        buttonSizer = self.CreateButtonSizer(wx.APPLY | wx.CLOSE)

        sizer.Add(telemetryPanel, 1, border=5, flag=wx.ALL | wx.EXPAND)
        sizer.Add(buttonSizer, 0, border=5, flag=wx.ALL | wx.EXPAND)


        self.Bind(wx.EVT_BUTTON, self.on_apply, id=wx.ID_APPLY)

        self.SetSizer(sizer)
        self.Fit()

    def on_apply(self, e):
        self.config.telemetry['host'] = self.hostField.GetValue()
        self.config.telemetry['port'] = int(self.portField.GetValue())
        self.config.telemetry['database'] = self.dbField.GetValue()
        self.config.save()

    def createTelemetryPanel(self, parent):
        panel = wx.Panel(parent)
        sizer = wx.BoxSizer(wx.VERTICAL)
        panel.SetSizer(sizer)

        box = wx.StaticBox(panel, label="Telemetry Server")
        boxSizer = wx.StaticBoxSizer(box, wx.VERTICAL)

        gbs = wx.GridBagSizer(3, 3)

        hostLabel = wx.StaticText(panel, label="Host:")
        self.hostField = wx.TextCtrl(panel, value=self.config.telemetry['host'])

        gbs.Add(hostLabel, pos=(0, 0), span=(1, 1), border=5, flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL)
        gbs.Add(self.hostField, pos=(0, 1), span=(1, 1), border=5, flag=wx.ALL | wx.EXPAND)

        portLabel = wx.StaticText(panel, label="Port:")
        self.portField = wx.TextCtrl(panel, value=str(self.config.telemetry['port']))

        gbs.Add(portLabel, pos=(1, 0), span=(1, 1), border=5, flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL)
        gbs.Add(self.portField, pos=(1, 1), span=(1, 1), border=5, flag=wx.ALL | wx.EXPAND)

        dbLabel = wx.StaticText(panel, label="Database:")
        self.dbField = wx.TextCtrl(panel, value=self.config.telemetry['database'])

        gbs.Add(dbLabel, pos=(2, 0), span=(1, 1), border=5, flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL)
        gbs.Add(self.dbField, pos=(2, 1), span=(1, 1), border=5, flag=wx.ALL | wx.EXPAND)

        gbs.Add(wx.Button(panel, label="Connect"), pos=(0, 2), border=5, flag=wx.ALL | wx.EXPAND)

        gbs.AddGrowableCol(1, 1)

        boxSizer.Add(gbs, flag=wx.EXPAND)

        sizer.Add(boxSizer, flag=wx.EXPAND)

        return panel

