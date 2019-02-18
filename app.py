#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import QApplication

from CryptoDiary import gui

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = gui.CryptoDiary()

    sys.exit(app.exec_())
