import wx
import os

from config import Config

class DashboardApp(wx.App):
    def __init__(self, config="./config.yaml"):
        self.config = Config.load(os.path.abspath(config))
        super().__init__(redirect=False)

    def OnInit(self):
        return True