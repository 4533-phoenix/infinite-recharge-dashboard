import wx

from panels import GameTimerPanel
from panels import DriverAssistPanel
from panels import IntakeStatusPanel
from panels import ControlButtonsPanel
from panels import CameraButtonsPanel
from panels import PowerCellPanel
from panels import AutoChooserPanel

from app import DashboardApp

class MainFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title)

        screenSize = wx.DisplaySize()
        initialSize = (screenSize[0] * 0.60, screenSize[1] * 0.60)

        self.statusBar = self.CreateStatusBar(2)
        self.set_telemetry_status(False)
        self.set_camera_status(False)

        self.SetInitialSize(initialSize)
        self.config = DashboardApp.Get().config
        self.build()
        self.Center()

    def build(self):

        # The main panel of the frame is laid out and sized by a Gridbag Sizer.
        # Below is the mapping of each component within that sizer.
        #
        # |   | 0 | 1 | 2 |
        # |---|---|---|---|
        # | 0 | T | T | T |
        # | 1 | A | D | I |
        # | 2 | A | D | I |
        # | 3 | A | C | I |
        # |---|---|---|---|
        #
        # T = Game Timer
        # A = Auto Chooser
        # D = Driver Assist
        # C = Driver Assist Camera Buttons
        # I = Intake Status
        gbs = wx.GridBagSizer(5, 4)

        mainPanel = wx.Panel(self)
        mainPanel.SetSizer(gbs)

        self.intakeStatus = IntakeStatusPanel(mainPanel)
        self.intakeStatus.update([True, True, False, False, True])

        # Get the configuration from the global 'Application'.
        config = DashboardApp.Get().config

        # Build and add the Game Timer Panel.
        gbs.Add(
            GameTimerPanel(mainPanel),
            wx.GBPosition(0,0),
            wx.GBSpan(1, 4),
            flag=wx.EXPAND
        )

        # Build and add the Auto Chooser Panel.
        gbs.Add(
            AutoChooserPanel(mainPanel, config),
            wx.GBPosition(1,0),
            wx.GBSpan(4,1),
            flag=wx.EXPAND
        )

        # Build and add the Driver Assist Panel.
        gbs.Add(
            DriverAssistPanel(mainPanel),
            wx.GBPosition(1,1),
            wx.GBSpan(3, 2),
            flag=wx.EXPAND
        )

        # Build and add the Intake Status Panel.
        gbs.Add(
            self.intakeStatus,
            wx.GBPosition(1, 3),
            wx.GBSpan(4, 1),
            flag=wx.EXPAND
        )

        # Build and add the Intake Status Panel.
        #
        # Note: this should more than likely be absorbed into the driver assist
        # panel since that is more relevant to it's context and purpose.
        gbs.Add(
            CameraButtonsPanel(mainPanel),
            wx.GBPosition(4, 1),
            wx.GBSpan(1, 2),
            flag=wx.EXPAND
        )

        # Define which columns of the sizer are growable.
        gbs.AddGrowableCol(0, 1)
        gbs.AddGrowableCol(1, 3)
        gbs.AddGrowableCol(2, 1)
        gbs.AddGrowableCol(3, 1)

        # Define which rows of the sizer are growable.
        gbs.AddGrowableRow(1, 1)
        gbs.AddGrowableRow(2, 1)

        gbs.Fit(self)

    def set_telemetry_status(self, status):
        if status:
            status = "connected"
        else:
            status = "disconnected"

        self.SetStatusText("Telemetry: {}".format(status), 0)

    def set_camera_status(self, status):
        if status:
            status = "connected"
        else:
            status = "disconnected"

        self.SetStatusText("Camera: {}".format(status), 1)
