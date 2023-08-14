# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTabWidget, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(674, 345)
        MainWindow.setMinimumSize(QSize(572, 310))
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        icon = QIcon()
        icon.addFile(u"assets/icons/system-shutdown.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionQuit.setIcon(icon)
        self.actionRun = QAction(MainWindow)
        self.actionRun.setObjectName(u"actionRun")
        icon1 = QIcon()
        icon1.addFile(u"assets/icons/media-playback-start.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionRun.setIcon(icon1)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        icon2 = QIcon()
        icon2.addFile(u"assets/icons/help-about.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAbout.setIcon(icon2)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        icon3 = QIcon()
        icon3.addFile(u"assets/icons/folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionOpen.setIcon(icon3)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 10, 651, 281))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.layoutWidget = QWidget(self.tab)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 631, 231))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSpacing(8)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(8, 8, 8, 8)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_6 = QSpacerItem(45, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_6)

        self.filenameField = QLineEdit(self.layoutWidget)
        self.filenameField.setObjectName(u"filenameField")
        self.filenameField.setReadOnly(True)

        self.horizontalLayout.addWidget(self.filenameField)

        self.horizontalSpacer_7 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_7)

        self.btnChooseFile = QPushButton(self.layoutWidget)
        self.btnChooseFile.setObjectName(u"btnChooseFile")
        self.btnChooseFile.setIcon(icon3)

        self.horizontalLayout.addWidget(self.btnChooseFile)

        self.horizontalSpacer_9 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_9)

        self.btnClearFile = QPushButton(self.layoutWidget)
        self.btnClearFile.setObjectName(u"btnClearFile")
        icon4 = QIcon()
        icon4.addFile(u"assets/icons/edit-clear.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnClearFile.setIcon(icon4)

        self.horizontalLayout.addWidget(self.btnClearFile)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.horizontalSpacer_4 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.cmbAlgorithm = QComboBox(self.layoutWidget)
        self.cmbAlgorithm.addItem("")
        self.cmbAlgorithm.addItem("")
        self.cmbAlgorithm.addItem("")
        self.cmbAlgorithm.addItem("")
        self.cmbAlgorithm.setObjectName(u"cmbAlgorithm")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbAlgorithm.sizePolicy().hasHeightForWidth())
        self.cmbAlgorithm.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.cmbAlgorithm)

        self.horizontalSpacer_16 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_16)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.cmbKeysize = QComboBox(self.layoutWidget)
        self.cmbKeysize.addItem("")
        self.cmbKeysize.addItem("")
        self.cmbKeysize.addItem("")
        self.cmbKeysize.setObjectName(u"cmbKeysize")
        sizePolicy.setHeightForWidth(self.cmbKeysize.sizePolicy().hasHeightForWidth())
        self.cmbKeysize.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.cmbKeysize)

        self.horizontalSpacer_19 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_19)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.cmbMode = QComboBox(self.layoutWidget)
        self.cmbMode.addItem("")
        self.cmbMode.addItem("")
        self.cmbMode.setObjectName(u"cmbMode")
        sizePolicy.setHeightForWidth(self.cmbMode.sizePolicy().hasHeightForWidth())
        self.cmbMode.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.cmbMode)

        self.horizontalSpacer_15 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_15)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_11.addWidget(self.label_7)

        self.horizontalSpacer_22 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_22)

        self.rdbEncrypt = QRadioButton(self.layoutWidget)
        self.rdbEncrypt.setObjectName(u"rdbEncrypt")
        self.rdbEncrypt.setChecked(True)

        self.horizontalLayout_11.addWidget(self.rdbEncrypt)

        self.horizontalSpacer_10 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_10)

        self.rdbDecrypt = QRadioButton(self.layoutWidget)
        self.rdbDecrypt.setObjectName(u"rdbDecrypt")

        self.horizontalLayout_11.addWidget(self.rdbDecrypt)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_5.addWidget(self.label_2)

        self.horizontalSpacer_5 = QSpacerItem(12, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.passwordField = QLineEdit(self.layoutWidget)
        self.passwordField.setObjectName(u"passwordField")
        self.passwordField.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.horizontalLayout_5.addWidget(self.passwordField)

        self.horizontalSpacer_8 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_8)

        self.btnClearPassword = QPushButton(self.layoutWidget)
        self.btnClearPassword.setObjectName(u"btnClearPassword")
        self.btnClearPassword.setIcon(icon4)

        self.horizontalLayout_5.addWidget(self.btnClearPassword)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.btnRun = QPushButton(self.layoutWidget)
        self.btnRun.setObjectName(u"btnRun")

        self.horizontalLayout_3.addWidget(self.btnRun)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.layoutWidget_2 = QWidget(self.tab_2)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 10, 631, 234))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setSpacing(8)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(8, 8, 8, 8)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_5 = QLabel(self.layoutWidget_2)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_6.addWidget(self.label_5)

        self.horizontalSpacer_13 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_13)

        self.cmbHashAlgorithm = QComboBox(self.layoutWidget_2)
        self.cmbHashAlgorithm.addItem("")
        self.cmbHashAlgorithm.addItem("")
        self.cmbHashAlgorithm.addItem("")
        self.cmbHashAlgorithm.addItem("")
        self.cmbHashAlgorithm.addItem("")
        self.cmbHashAlgorithm.setObjectName(u"cmbHashAlgorithm")

        self.horizontalLayout_6.addWidget(self.cmbHashAlgorithm)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_14)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 4, -1, 4)
        self.rdbFileHash = QRadioButton(self.layoutWidget_2)
        self.rdbFileHash.setObjectName(u"rdbFileHash")
        self.rdbFileHash.setChecked(True)

        self.horizontalLayout_4.addWidget(self.rdbFileHash)

        self.horizontalSpacer_20 = QSpacerItem(22, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_20)

        self.txtHashFile = QLineEdit(self.layoutWidget_2)
        self.txtHashFile.setObjectName(u"txtHashFile")
        self.txtHashFile.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.txtHashFile)

        self.horizontalSpacer_11 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_11)

        self.btnChooseHash = QPushButton(self.layoutWidget_2)
        self.btnChooseHash.setObjectName(u"btnChooseHash")
        self.btnChooseHash.setIcon(icon3)

        self.horizontalLayout_4.addWidget(self.btnChooseHash)

        self.horizontalSpacer_12 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_12)

        self.btnClearHashFile = QPushButton(self.layoutWidget_2)
        self.btnClearHashFile.setObjectName(u"btnClearHashFile")
        self.btnClearHashFile.setIcon(icon4)

        self.horizontalLayout_4.addWidget(self.btnClearHashFile)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, -1, -1, -1)
        self.rdbText = QRadioButton(self.layoutWidget_2)
        self.rdbText.setObjectName(u"rdbText")

        self.horizontalLayout_9.addWidget(self.rdbText)

        self.horizontalSpacer_23 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_23)

        self.txtHashField = QTextEdit(self.layoutWidget_2)
        self.txtHashField.setObjectName(u"txtHashField")
        self.txtHashField.setEnabled(False)

        self.horizontalLayout_9.addWidget(self.txtHashField)

        self.horizontalSpacer_21 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_21)

        self.btnClearHashField = QPushButton(self.layoutWidget_2)
        self.btnClearHashField.setObjectName(u"btnClearHashField")
        self.btnClearHashField.setEnabled(False)
        self.btnClearHashField.setIcon(icon4)

        self.horizontalLayout_9.addWidget(self.btnClearHashField)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_17)

        self.btnHashRun = QPushButton(self.layoutWidget_2)
        self.btnHashRun.setObjectName(u"btnHashRun")

        self.horizontalLayout_8.addWidget(self.btnHashRun)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_18)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, -1, -1, -1)
        self.label_8 = QLabel(self.layoutWidget_2)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_10.addWidget(self.label_8)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_26)

        self.txtHash = QLineEdit(self.layoutWidget_2)
        self.txtHash.setObjectName(u"txtHash")
        self.txtHash.setReadOnly(True)

        self.horizontalLayout_10.addWidget(self.txtHash)

        self.horizontalSpacer_25 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_25)

        self.btnCopyHash = QPushButton(self.layoutWidget_2)
        self.btnCopyHash.setObjectName(u"btnCopyHash")
        icon5 = QIcon()
        icon5.addFile(u"assets/icons/edit-copy.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnCopyHash.setIcon(icon5)

        self.horizontalLayout_10.addWidget(self.btnCopyHash)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 674, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuRun = QMenu(self.menubar)
        self.menuRun.setObjectName(u"menuRun")
        self.menuInfo = QMenu(self.menubar)
        self.menuInfo.setObjectName(u"menuInfo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuRun.menuAction())
        self.menubar.addAction(self.menuInfo.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuRun.addAction(self.actionRun)
        self.menuInfo.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionRun.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"File:", None))
#if QT_CONFIG(tooltip)
        self.filenameField.setToolTip(QCoreApplication.translate("MainWindow", u"File to be encrypted/decrypted", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.btnChooseFile.setToolTip(QCoreApplication.translate("MainWindow", u"Choose the file to encrypt/decrypt", None))
#endif // QT_CONFIG(tooltip)
        self.btnChooseFile.setText("")
#if QT_CONFIG(tooltip)
        self.btnClearFile.setToolTip(QCoreApplication.translate("MainWindow", u"Clear the filename", None))
#endif // QT_CONFIG(tooltip)
        self.btnClearFile.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Algorithm:", None))
        self.cmbAlgorithm.setItemText(0, QCoreApplication.translate("MainWindow", u"AES", None))
        self.cmbAlgorithm.setItemText(1, QCoreApplication.translate("MainWindow", u"CAST5", None))
        self.cmbAlgorithm.setItemText(2, QCoreApplication.translate("MainWindow", u"Camellia", None))
        self.cmbAlgorithm.setItemText(3, QCoreApplication.translate("MainWindow", u"ChaCha20", None))

#if QT_CONFIG(tooltip)
        self.cmbAlgorithm.setToolTip(QCoreApplication.translate("MainWindow", u"Select an algorithm", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Keysize:", None))
        self.cmbKeysize.setItemText(0, QCoreApplication.translate("MainWindow", u"128 bits", None))
        self.cmbKeysize.setItemText(1, QCoreApplication.translate("MainWindow", u"192 bits", None))
        self.cmbKeysize.setItemText(2, QCoreApplication.translate("MainWindow", u"256 bits", None))

#if QT_CONFIG(tooltip)
        self.cmbKeysize.setToolTip(QCoreApplication.translate("MainWindow", u"Select keysize", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Mode:", None))
        self.cmbMode.setItemText(0, QCoreApplication.translate("MainWindow", u"OFB", None))
        self.cmbMode.setItemText(1, QCoreApplication.translate("MainWindow", u"CBC", None))

#if QT_CONFIG(tooltip)
        self.cmbMode.setToolTip(QCoreApplication.translate("MainWindow", u"Select mode of operation", None))
#endif // QT_CONFIG(tooltip)
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Operation:", None))
        self.rdbEncrypt.setText(QCoreApplication.translate("MainWindow", u"Encryption", None))
        self.rdbDecrypt.setText(QCoreApplication.translate("MainWindow", u"Decryption", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
#if QT_CONFIG(tooltip)
        self.passwordField.setToolTip(QCoreApplication.translate("MainWindow", u"Enter a password", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.passwordField.setStatusTip(QCoreApplication.translate("MainWindow", u"AES cipher with 128/256 (16/32 chars) password", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(tooltip)
        self.btnClearPassword.setToolTip(QCoreApplication.translate("MainWindow", u"Clear the password field", None))
#endif // QT_CONFIG(tooltip)
        self.btnClearPassword.setText("")
        self.btnRun.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Encrypt/Decrypt", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Algorithm:", None))
        self.cmbHashAlgorithm.setItemText(0, QCoreApplication.translate("MainWindow", u"BLAKE2", None))
        self.cmbHashAlgorithm.setItemText(1, QCoreApplication.translate("MainWindow", u"MD5", None))
        self.cmbHashAlgorithm.setItemText(2, QCoreApplication.translate("MainWindow", u"SHA256", None))
        self.cmbHashAlgorithm.setItemText(3, QCoreApplication.translate("MainWindow", u"SHA384", None))
        self.cmbHashAlgorithm.setItemText(4, QCoreApplication.translate("MainWindow", u"SHA512", None))

#if QT_CONFIG(tooltip)
        self.cmbHashAlgorithm.setToolTip(QCoreApplication.translate("MainWindow", u"Choose an Hash algorithm", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.rdbFileHash.setToolTip(QCoreApplication.translate("MainWindow", u"Work with a file", None))
#endif // QT_CONFIG(tooltip)
        self.rdbFileHash.setText(QCoreApplication.translate("MainWindow", u"File ", None))
#if QT_CONFIG(tooltip)
        self.txtHashFile.setToolTip(QCoreApplication.translate("MainWindow", u"File for which to calculate the hash", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.btnChooseHash.setToolTip(QCoreApplication.translate("MainWindow", u"Choose file", None))
#endif // QT_CONFIG(tooltip)
        self.btnChooseHash.setText("")
#if QT_CONFIG(tooltip)
        self.btnClearHashFile.setToolTip(QCoreApplication.translate("MainWindow", u"Clear filename field", None))
#endif // QT_CONFIG(tooltip)
        self.btnClearHashFile.setText("")
#if QT_CONFIG(tooltip)
        self.rdbText.setToolTip(QCoreApplication.translate("MainWindow", u"Manually insert a text", None))
#endif // QT_CONFIG(tooltip)
        self.rdbText.setText(QCoreApplication.translate("MainWindow", u"Text", None))
#if QT_CONFIG(tooltip)
        self.txtHashField.setToolTip(QCoreApplication.translate("MainWindow", u"Insert a text for which to computer the has", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.btnClearHashField.setToolTip(QCoreApplication.translate("MainWindow", u"Clear the text field", None))
#endif // QT_CONFIG(tooltip)
        self.btnClearHashField.setText("")
#if QT_CONFIG(tooltip)
        self.btnHashRun.setToolTip(QCoreApplication.translate("MainWindow", u"Compute the hash", None))
#endif // QT_CONFIG(tooltip)
        self.btnHashRun.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Hash", None))
#if QT_CONFIG(tooltip)
        self.txtHash.setToolTip(QCoreApplication.translate("MainWindow", u"Computed hash", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.btnCopyHash.setToolTip(QCoreApplication.translate("MainWindow", u"Copy to clipboard", None))
#endif // QT_CONFIG(tooltip)
        self.btnCopyHash.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Hash", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuRun.setTitle(QCoreApplication.translate("MainWindow", u"Run", None))
        self.menuInfo.setTitle(QCoreApplication.translate("MainWindow", u"Info", None))
    # retranslateUi

