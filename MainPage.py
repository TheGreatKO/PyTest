#!/usr/bin/env python3.4

# Author - KO . All rights reserved.
import  sys
from PyQt5 import QtWidgets

# Stab at showing GUI QT Window
def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    w.setWindowTitle("GitHub Window")
    w.show()
    sys.exit(app.exec_())

window()