# This Python file uses the following encoding: utf-8

# This file is part of pyCrypto, an encryption/decryption/hashing
# app developed in Python and based on PySide6
# Written by Leonardo Miliani in 2023~2025
# Released under the terms of the GNU General Public License v3.0 or later
#
# Please read the readme file for instructions and details
#

import sys

from PySide6.QtWidgets import (
    QApplication,
)

from src.loadModules import LoadModules
from src.mainwindow import MainWindow


# #######################################################################
# # # # # # # # # # #    M A I N   P R O G R A M    # # # # # # # # # # #
# #######################################################################

# launch main program
if __name__ == "__main__":
    # check missing modules
    loadmodules = LoadModules()
    loadmodules.run()
    # show GUI
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
