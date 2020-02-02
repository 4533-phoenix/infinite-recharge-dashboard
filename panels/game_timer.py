import wx

MATCH_START = 150
TELEOP_START =  135
END_GAME_START = 30

YELLOW = (255, 255, 77)
GREEN = (77, 255, 77)
ORANGE = (255, 175, 25)
RED = (255, 25, 25)

class GameTimerPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.matchTime = MATCH_START
        self.currentTime = self.matchTime
        self.SetBackgroundColour(YELLOW)

        self.timer = wx.Timer(self, -1)
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)

        self.buildPanel()

    def buildPanel(self):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.SetSizer(sizer)

        self.text = wx.StaticText(self,
            label=self.GetFormattedTime(),
            style=wx.ALIGN_CENTRE_HORIZONTAL | wx.ST_NO_AUTORESIZE
        )

        self.text.SetForegroundColour(wx.BLACK)
        self.text.SetFont(wx.Font(48, wx.MODERN, wx.NORMAL, wx.BOLD))

        sizer.Add(self.text, 1, flag=wx.EXPAND)

    def Start(self):
        self.timer.Start()

    def Stop(self):
        self.time.Stop()

    def GetFormattedTime(self):
        minutes = self.currentTime // 60
        seconds = self.currentTime % 60
        return "{}:{:02}".format(minutes, seconds)

    def OnTimer(self, event):
        self.currentTime -= 1

        if (self.currentTime > TELEOP_START):
            self.SetBackgroundColour(YELLOW)
        elif (self.currentTime > END_GAME_START):
            self.SetBackgroundColour(GREEN)
        elif (self.currentTime > 0):
            self.SetBackgroundColour(ORANGE)
        else:
            self.SetBackgroundColour(RED)
            self.timer.Stop()

        self.text.SetLabel(self.GetFormattedTime())
