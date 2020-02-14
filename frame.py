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

        self.SetInitialSize(initialSize)
        self.config = DashboardApp.Get().config
        self.build()
        self.Center()

    def build(self):
        gbs = wx.GridBagSizer(5, 4)

        mainPanel = wx.Panel(self)
        mainPanel.SetSizer(gbs)

        self.intakeStatus = IntakeStatusPanel(mainPanel)
        self.intakeStatus.update([True, True, False, False, True])

        config = DashboardApp.Get().config

        gbs.Add(
            GameTimerPanel(mainPanel),
            wx.GBPosition(0,0),
            wx.GBSpan(1, 4),
            flag=wx.EXPAND
        )

        gbs.Add(
            AutoChooserPanel(mainPanel, config),
            wx.GBPosition(1,0),
            wx.GBSpan(4,1),
            flag=wx.EXPAND
        )

        gbs.Add(
            DriverAssistPanel(mainPanel),
            wx.GBPosition(1,1),
            wx.GBSpan(3, 2),
            flag=wx.EXPAND
        )

        gbs.Add(
            self.intakeStatus,
            wx.GBPosition(1, 3),
            wx.GBSpan(4, 1),
            flag=wx.EXPAND
        )

        gbs.Add(
            CameraButtonsPanel(mainPanel),
            wx.GBPosition(4, 1),
            wx.GBSpan(1, 2),
            flag=wx.EXPAND
        )

        gbs.AddGrowableCol(0, 1)
        gbs.AddGrowableCol(1, 3)
        gbs.AddGrowableCol(2, 1)
        gbs.AddGrowableCol(3, 1)
        gbs.AddGrowableRow(1, 1)

        gbs.AddGrowableRow(2, 1)

        gbs.Fit(self)
