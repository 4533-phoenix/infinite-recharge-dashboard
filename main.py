#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import wx
import yaml

from frame import MainFrame
from config import Config
from app import DashboardApp

def main():
    app = DashboardApp()
    app.SetAppName("FOO BAR")
    frame = MainFrame(None, "Infinite Recharge Dashboard")
    frame.Show(True)
    app.MainLoop()

if __name__ == '__main__':
    main()