import wx

from panels import GameTimerPanel
from panels import DriverAssistPanel
from panels import IntakeStatusPanel
from panels import ButtonsPanel

class MainFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=wx.Size(400,500))
        self.build()
        self.Center()

    def build(self):
        self.SetInitialSize(size=wx.Size(500,400))

        gbs = wx.GridBagSizer(4, 2)

        mainPanel = wx.Panel(self)
        mainPanel.SetSizer(gbs)

        gbs.Add(
            GameTimerPanel(mainPanel),
            wx.GBPosition(0,0),
            wx.GBSpan(1, 3),
            flag=wx.EXPAND
        )

        gbs.Add(
            DriverAssistPanel(mainPanel),
            wx.GBPosition(1,0),
            wx.GBSpan(2, 2),
            flag=wx.EXPAND
        )

        gbs.Add(
            IntakeStatusPanel(mainPanel),
            wx.GBPosition(1, 2),
            wx.GBSpan(2, 1),
            flag=wx.EXPAND
        )

        gbs.Add(
            ButtonsPanel(mainPanel),
            wx.GBPosition(3, 0),
            wx.GBSpan(1, 3),
            flag=wx.EXPAND
        )

        gbs.AddGrowableCol(0, 1)
        gbs.AddGrowableCol(1, 3)
        gbs.AddGrowableCol(2, 1)
        gbs.AddGrowableRow(1, 1)

        gbs.Fit(self)