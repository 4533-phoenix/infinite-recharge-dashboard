#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import wx

from frame import MainFrame

def main():
    app = wx.App(False)
    frame = MainFrame(None, "Infinite Recharge Dashboard")
    frame.Show(True)
    app.MainLoop()

if __name__ == '__main__':
    main()