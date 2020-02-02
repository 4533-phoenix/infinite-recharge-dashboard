import wx
import wx.gizmos as gizmos

MATCH_START = 60
TELEOP_START =  45
END_GAME_START = 30

YELLOW = (255, 255, 77)
GREEN = (77, 255, 77)
ORANGE = (255, 175, 25)
RED = (255, 25, 25)

class GameTimerPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.buildPanel()

    def buildPanel(self):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.SetSizer(sizer)

        self.text = wx.StaticText(self,
            label="0:00",
            style=wx.ALIGN_CENTRE_HORIZONTAL | wx.ST_NO_AUTORESIZE
        )
        font = wx.Font(48, wx.MODERN, wx.NORMAL, wx.BOLD)
        self.text.SetForegroundColour(wx.BLACK)
        self.text.SetFont(font)

        sizer.Add(self.text, 1, flag=wx.EXPAND)

        self.matchTime = MATCH_START
        self.currentTime = self.matchTime

        self.OnTimer(None)

        self.timer = wx.Timer(self, -1)
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)
        self.timer.Start(1000)

    def OnTimer(self, event):
        self.currentTime -= 1

        minutes = self.currentTime // 60
        seconds = self.currentTime % 60

        if (self.currentTime > TELEOP_START):
            self.SetBackgroundColour(YELLOW)
        elif (self.currentTime > END_GAME_START):
            self.SetBackgroundColour(GREEN)
        elif (self.currentTime > 0):
            self.SetBackgroundColour(ORANGE)
        else:
            self.SetBackgroundColour(RED)
            self.timer.Stop()

        self.text.SetLabel("{}:{:02}".format(minutes, seconds))
