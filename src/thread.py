# This Python file uses the following encoding: utf-8

# This file is part of pyCrypto, an encryption/decryption/hashing
# app developed in Python and based on PySide6
# Written by Leonardo Miliani in 2023~2025
# Released under the terms of the GNU General Public License v3.0 or later
#
# Please read the readme file for instructions and details
#

from PySide6.QtCore import (
    QObject, Signal,
    QRunnable, Slot
)

# used to send signals to custom slots
class MySignal(QObject):
    """Send signals to custom slots"""
    finalize = Signal(str)
    finalize_error = Signal(str)

# threads manager
class Worker(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    @Slot()
    def run(self):
        self.fn(*self.args, **self.kwargs)
