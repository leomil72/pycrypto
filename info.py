# This Python file uses the following encoding: utf-8

# This file is part of pyCrypto, an encryption/decryption/hashing
# app developed in Python and based on PySide6
# Written by Leonardo Miliani in 2023
# Released under the terms of the GNU General Public License v3.0 or later
#
# Please read the readme file for instructions and details
#

from PySide6.QtGui import QPixmap

from PySide6.QtWidgets import (
    QDialog, QHBoxLayout,
    QDialogButtonBox, QVBoxLayout,
    QLabel
)

# show info about the app
class Info(QDialog):
    """Show info about the app"""
    def __init__(self, app_version, build):
        super().__init__()
        self.setWindowTitle("pyCrypto")
        self.app_version = app_version
        self.build = build

        QBtn = QDialogButtonBox.Ok
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout1 = QVBoxLayout()
        self.layout2 = QHBoxLayout()
        txt = "pyCrypto is a simple app written in Python/Qt that encrypts/\n"
        txt += "decrypts files with several cryptographic algorithms.\n\n"
        txt += "Written by Leonardo Miliani (2023).\n\n"
        txt += "App version {} - Build {}".format(self.app_version, self.build)
        message = QLabel(txt)
        pixmap = QPixmap("./assets/pycrypto.png")
        label = QLabel(self)
        label.setPixmap(pixmap)
        label.setFixedSize(128, 128)
        label.setScaledContents(True)
        self.layout2.addWidget(message)
        self.layout2.addWidget(label)
        self.layout1.addLayout(self.layout2)
        self.layout1.addWidget(self.buttonBox)
        self.setLayout(self.layout1)

