# This Python file uses the following encoding: utf-8

# This file is part of pyCrypto, an encryption/decryption/hashing
# app developed in Python and based on PySide6
# Written by Leonardo Miliani in 2023
# Released under the terms of the GNU General Public License v3.0 or later
#
# Please read the readme file for instructions and details
#

# # # # # # #   L I B R A R I E S / M O D U L E S   I M P O R T   # # # # # # #

import os.path, time

from PySide6.QtWidgets import (
    QApplication, QMainWindow,
    QFileDialog, QMessageBox
)

from PySide6.QtCore import (
    QThreadPool
)

# custom libraries
from my_crypto import MyCrypto
from thread import MySignal, Worker
from info import Info

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow


# # # # # # # # # # # # # #   M A I N   C O D E   # # # # # # # # # # # # # # #

closing_app = False
APP_VERSION = "0.9"
BUILD = 11

# # # # #   M A I N   W I N D O W   U I   M A N A G E M E N T   # # # # #
class MainWindow(QMainWindow):
    """Main window: show the UI and manage the user interaction"""
    def __init__(self, parent=None):
        # initialize window
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("pyCrypto")

        # create menu links
        menu_exit = self.ui.actionQuit
        menu_exit.triggered.connect(self.menu_quit_pressed)
        menu_info = self.ui.actionAbout
        menu_info.triggered.connect(self.menu_info_pressed)
        menu_run = self.ui.actionRun
        menu_run.triggered.connect(self.menu_run_pressed)
        menu_open = self.ui.actionOpen
        menu_open.triggered.connect(self.btn_file_pressed)

        # connect signal/slot for widgets related to Encryption/Decryption
        run_btn = self.ui.btnRun
        run_btn.clicked.connect(self.btn_run_pressed)
        file_btn = self.ui.btnChooseFile
        file_btn.clicked.connect(self.btn_file_pressed)
        clearfile_btn = self.ui.btnClearFile
        clearfile_btn.clicked.connect(self.btn_clearfile_pressed)
        clearpassword_btn = self.ui.btnClearPassword
        clearpassword_btn.clicked.connect(self.btn_clearpassword_pressed)
        rdbText_radio = self.ui.rdbText
        rdbText_radio.clicked.connect(self.rdbText_radio_pressed)
        cmb_algorithm = self.ui.cmbAlgorithm
        cmb_algorithm.currentIndexChanged[int].connect(self.set_crypto_algorithm_params)

        # connect signal/slot for widgets related to Hashing
        run_hash_btn = self.ui.btnHashRun
        run_hash_btn.clicked.connect(self.btn_run_pressed)
        hashfile_btn = self.ui.btnChooseHash
        hashfile_btn.clicked.connect(self.btn_file_pressed)
        clearHashField_btn = self.ui.btnClearHashField
        clearHashField_btn.clicked.connect(self.btn_clearHashfield_pressed)
        clearHashFile_btn = self.ui.btnClearHashFile
        clearHashFile_btn.clicked.connect(self.btn_chearHashfile_pressed)
        rdbFile_radio = self.ui.rdbFileHash
        rdbFile_radio.clicked.connect(self.rdbFile_radio_pressed)
        copy_digest = self.ui.btnCopyHash
        copy_digest.clicked.connect(self.copy_to_clipboard)

        # create thread pool
        self.threadpool = QThreadPool()

    def closeEvent(self, event):
        # let the window close
        global closing_app
        closing_app = True
        event.accept()

# # # # # # # # #   H A S H    S L O T S / F U N C T I O N S   # # # # # # # # #

    # thread that executes the hash algorithms
    # without blocking the GUI thread
    def start_hash(self):
        global closing_app
        # clear current digest
        self.ui.txtHash.setText("")
        # get a reference to button
        btn_run = self.ui.btnHashRun
        status_bar = self.ui.statusbar
        # create a signal/slot interface to show a message after operation is finished
        self.signal = MySignal()
        self.signal.finalize.connect(self.showDiag)
        self.signal.finalize_error.connect(self.showDiagErr)

        # begin
        inputFile = self.ui.txtHashFile.text()
        # hash of a file
        if self.ui.rdbFileHash.isChecked():
            if (not os.path.isfile(inputFile)):
                self.signal.finalize_error.emit("{} isn't a valid file.".format(inputFile))
            hash_algorithm = self.ui.cmbHashAlgorithm.currentText()
            hashing = MyCrypto(hash_algorithm)
            status_bar.showMessage("Hashing...")
            digest = hashing.hash_file(inputFile)
            self.ui.txtHash.setText(''.join(format(x, '02x') for x in digest))
        # hash of a text
        else:
            hash_algorithm = self.ui.cmbHashAlgorithm.currentText()
            hashing = MyCrypto(hash_algorithm)
            status_bar.showMessage("Hashing...")
            #time1 = time.time()
            text = bytearray(self.ui.txtHashField.toPlainText().encode('utf8'))
            digest = hashing.hash_text(text)
            #time2 = time.time()
            self.ui.txtHash.setText(''.join(format(x, '02x') for x in digest))
        # finish
        btn_run.setEnabled(True)
        status_bar.showMessage("Done")


    # enable/disable hash file radio options
    def rdbText_radio_pressed(self):
        self.ui.txtHashField.setEnabled(True)
        self.ui.btnClearHashField.setEnabled(True)
        self.ui.txtHashFile.setEnabled(False)
        self.ui.btnChooseHash.setEnabled(False)
        self.ui.btnClearHashFile.setEnabled(False)

    # enable/disable hash field radio options
    def rdbFile_radio_pressed(self):
        self.ui.txtHashField.setEnabled(False)
        self.ui.btnClearHashField.setEnabled(False)
        self.ui.txtHashFile.setEnabled(True)
        self.ui.btnChooseHash.setEnabled(True)
        self.ui.btnClearHashFile.setEnabled(True)

    # clear hasfile
    def btn_chearHashfile_pressed(self):
        self.ui.txtHashFile.setText("")

    # clear hashfield
    def btn_clearHashfield_pressed(self):
        self.ui.txtHashField.setText("")

# # # # # # #   E N C / D E C    S L O T S / F U N C T I O N S   # # # # # # #

    # clear filename field
    def btn_clearfile_pressed(self):
        self.ui.filenameField.setText("")

    # clear password field
    def btn_clearpassword_pressed(self):
        self.ui.passwordField.setText("")


    # set UI and params according to algorithms
    def set_crypto_algorithm_params(self, index):
        if index == 0:
            # AES
            self.ui.cmbKeysize.setEnabled(True)
            self.ui.cmbMode.setEnabled(True)
            self.ui.passwordField.setStatusTip("AES cipher with 128/192/256 bits (16/24/32 chars) password")
        elif index == 1:
            # CAST5: set keysize to 128
            self.ui.cmbKeysize.setCurrentIndex(0)
            self.ui.cmbKeysize.setEnabled(False)
            self.ui.cmbMode.setEnabled(True)
            self.ui.passwordField.setStatusTip("CAST5 cipher with 128 bits (16 chars) password")
        elif index == 2:
            # Camellia
            self.ui.cmbKeysize.setEnabled(True)
            self.ui.cmbMode.setEnabled(True)
            self.ui.passwordField.setStatusTip("Camellia cipher with 128/192/256 bits (16/24/32 chars) password")
        else:
            # Chacha20: set keysize to 256 and disable mode
            self.ui.cmbKeysize.setCurrentIndex(2)
            self.ui.cmbKeysize.setEnabled(False)
            self.ui.cmbMode.setEnabled(False)
            self.ui.passwordField.setStatusTip("ChaCha20 cipher with 256 bits (32 chars) password")



    # thread that executes the cipher algorithms
    # without blocking the GUI thread
    def start_program(self):
        global closing_app
        # get a reference to button
        btn_run = self.ui.btnRun
        status_bar = self.ui.statusbar
        # create a signal/slot interface to show a message after operation is finished
        self.signal = MySignal()
        self.signal.finalize.connect(self.showDiag)
        self.signal.finalize_error.connect(self.showDiagErr)

        # begin
        tempKey = self.ui.passwordField.text()
        tempKey.replace(" ", "")
        inputFile = self.ui.filenameField.text()
        if (not os.path.isfile(inputFile)):
            #self.showDialog("{} isn't a valid file.".format(inputFile), QMessageBox.Critical)
            self.signal.finalize_error.emit("{} isn't a valid file.".format(inputFile))
        else:
            cipher_algorithm = self.ui.cmbAlgorithm.currentText()
            cipher_keysize = 128 + (self.ui.cmbKeysize.currentIndex() * 64)
            cipher_mode = self.ui.cmbMode.currentText()
            if cipher_algorithm == "AES" or cipher_algorithm == "Camellia":
                iv_size = 128
                block_size = 128
            elif cipher_algorithm == "ChaCha20":
                iv_size = 128
                block_size = 128
            else: # CAST5
                iv_size = 64
                block_size = 64
            # initialize cipher primitive
            cipher = MyCrypto(cipher_algorithm, cipher_keysize, block_size, iv_size, cipher_mode)
            # key padding
            key = cipher.padding(tempKey, cipher_keysize // 8, truncate = True)
            keyList = list(key)
            keyList = [ord(x) for x in keyList]

            # encrypt or decrypt?
            if self.ui.rdbEncrypt.isChecked():
                status_bar.showMessage("Encrypting...")
                time1 = time.time()
                cipher.encryptFile(inputFile, bytearray(keyList))
                time2 = time.time()
                self.signal.finalize.emit("File encrypted as:\n{}\nTime elapsed: {}".format(inputFile + ".enc", time2 - time1))
            else:
                status_bar.showMessage("Decrypting...")
                time1 = time.time()
                cipher.decryptFile(inputFile, bytearray(keyList))
                time2 = time.time()
                self.signal.finalize.emit("File decrypted as:\n{}\nTime elapsed: {}".format(inputFile + ".dec", time2 - time1))
        # finish
        btn_run.setEnabled(True)
        # re-enable button
        btn_run.setDisabled(False)

    # button pressed signal management
    def btn_run_pressed(self):
        if self.ui.tabWidget.currentIndex() == 0:
            if self.ui.filenameField.text() == "":
                self.showDialog("You didn't choose any file", QMessageBox.Warning)
                return
            if self.ui.passwordField.text() == "":
                self.showDialog("You didn't set any password", QMessageBox.Warning)
                return
            # disable button
            self.ui.btnRun.setDisabled(True)
            # choose correct routine
            program = self.start_program
        else:
            if self.ui.rdbFileHash.isChecked():
                if self.ui.txtHashFile.text() == "":
                    self.showDialog("You didn't choose any file", QMessageBox.Warning)
                    return
            # disable button
            self.ui.btnHashRun.setDisabled(True)
            program = self.start_hash
        # add the job to the thread manager
        worker = Worker(program)
        # start the thread
        self.threadpool.start(worker)

# # # # # # #   G E N E R I C    S L O T S / F U N C T I O N S   # # # # # # #

    # show a msg to the user through a signal/slot channel
    def showDiag(self, msgTxt):
        status_bar = self.ui.statusbar
        status_bar.showMessage("Done")
        self.showDialog(msgTxt, QMessageBox.Information)

    # show an error msg to the user through a signal/slot channel
    def showDiagErr(self, msgTxt):
        status_bar = self.ui.statusbar
        status_bar.showMessage("Error")
        self.showDialog(msgTxt, QMessageBox.Critical)

    # show a dialog box
    def showDialog(self, msgTxt, msgType):
        msgbox = QMessageBox(self)
        msgbox.setWindowTitle("pyCrypto")
        msgbox.setText(msgTxt)
        msgbox.setStandardButtons(QMessageBox.Ok)
        msgbox.setIcon(msgType)
        msgbox.exec()

    # copy digest to clipboard
    def copy_to_clipboard(self):
        if self.ui.txtHash.text() != "":
            clipboard = QApplication.clipboard()
            clipboard.setText(self.ui.txtHash.text())
            self.showDialog("Digest copied to clipboard", QMessageBox.Information)


# # # # # # # # #   M E N U    S L O T S / F U N C T I O N S   # # # # # # # # #

    # menu file dialog
    def btn_file_pressed(self):
        # get current tab
        tab_index = self.ui.tabWidget.currentIndex()
        # if the current tab is Hash and the input is in the text field, show a warning
        if tab_index == 1 and self.ui.rdbFileHash.isChecked() == False:
            self.showDialog('To choose a file you need to\nclick on the "File" radio button first', QMessageBox.Warning)
            return
        # open the File choose dialog
        fileName = QFileDialog.getOpenFileName(self, str("Choose File"), "", str("Any File (*.*)"))
        if fileName[0] != '':
            # set the correct field with the file name
            if tab_index == 0:
                self.ui.filenameField.setText(fileName[0])
            else:
                self.ui.txtHashFile.setText(fileName[0])

    # menu Info
    def menu_info_pressed(self):
        dlg = Info(APP_VERSION, BUILD)
        dlg.exec()

    # menu Quit
    def menu_quit_pressed(self):
        self.threadpool
        widget.close()

    # menu Run
    def menu_run_pressed(self):
        self.btn_run_pressed()

