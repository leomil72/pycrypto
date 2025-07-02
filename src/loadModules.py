# This Python file uses the following encoding: utf-8

# This file is part of pyCrypto, an encryption/decryption/hashing
# app developed in Python and based on PySide6
# Written by Leonardo Miliani in 2023~2025
# Released under the terms of the GNU General Public License v3.0 or later
#
# Please read the readme file for instructions and details
#

import importlib
import subprocess
import sys

class LoadModules:
    def __init__(self):
        # list of required modules
        self.required_modules = ["cryptography"]

    # #########################################################################
    # import missing modules

    def install_and_import(self, module_name):
        try:
            # check if the module is already installed
            importlib.import_module(module_name)
        except ImportError:
            # install missing module
            print(f"\n##################################################\nInstalling missing module <{module_name}>...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", module_name])


    def run(self):
        for module in self.required_modules:
            self.install_and_import(module)
