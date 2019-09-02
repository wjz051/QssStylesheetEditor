﻿#!/usr/bin/python
# -*- coding: utf-8 -*-
"""QssStylesheetEditor app start module

Create QApplication and show splash. Include minimal module to accelerate spalsh load.

Copyright (c) 2019 lileilei <hustlei@sina.cn>
"""

from PyQt5.QtWidgets import QApplication
import sys
import os
os.chdir(os.path.dirname(__file__))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


def main():
    # sys.setrecursionlimit(1500)
    app = QApplication(sys.argv)
    print("starting...")
    from ui.splash import SplashScreen
    splash = SplashScreen("img/splash.png")
    splash.loadProgress()
    from ui.mainwin import MainWin
    win = MainWin()
    win.show()
    splash.finish(win)
    sys.exit(app.exec_())


main()
