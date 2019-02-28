# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'deneme.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 200)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.infobutton = QtWidgets.QPushButton(self.centralwidget)
        self.infobutton.setGeometry(QtCore.QRect(60, 110, 101, 31))
        self.infobutton.setStyleSheet("")
        self.infobutton.setObjectName("infobutton")
        self.maintext = QtWidgets.QLabel(self.centralwidget)
        self.maintext.setGeometry(QtCore.QRect(130, 0, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.maintext.setFont(font)
        self.maintext.setScaledContents(False)
        self.maintext.setAlignment(QtCore.Qt.AlignCenter)
        self.maintext.setWordWrap(False)
        self.maintext.setObjectName("maintext")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 60, 111, 21))
        self.label.setObjectName("label")
        self.inputcoininfo = QtWidgets.QLineEdit(self.centralwidget)
        self.inputcoininfo.setGeometry(QtCore.QRect(50, 90, 121, 16))
        self.inputcoininfo.setInputMethodHints(QtCore.Qt.ImhLatinOnly|QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhUppercaseOnly)
        self.inputcoininfo.setInputMask("")
        self.inputcoininfo.setText("")
        self.inputcoininfo.setMaxLength(8)
        self.inputcoininfo.setDragEnabled(False)
        self.inputcoininfo.setReadOnly(False)
        self.inputcoininfo.setClearButtonEnabled(False)
        self.inputcoininfo.setObjectName("inputcoininfo")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 90, 141, 31))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        #MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 22))
        self.menubar.setObjectName("menubar")
        #MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        #MainWindow.setStatusBar(self.statusbar)
        self.action_XXXBTC = QtWidgets.QAction(MainWindow)
        self.action_XXXBTC.setObjectName("action_XXXBTC")
        self.action_XXXETH = QtWidgets.QAction(MainWindow)
        self.action_XXXETH.setObjectName("action_XXXETH")
        self.action_XXXBNB = QtWidgets.QAction(MainWindow)
        self.action_XXXBNB.setObjectName("action_XXXBNB")
        self.action_Cache_Reset = QtWidgets.QAction(MainWindow)
        self.action_Cache_Reset.setObjectName("action_Cache_Reset")

        self.retranslateUi(MainWindow)
        self.infobutton.clicked.connect(self.infocoin_coin)
        #self.infobutton.clicked.connect(self.label_2.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def infocoin_coin(self):
        a=self.inputcoininfo.text()
        b=x.get_symbol_ticker(symbol=a)
        self.label_2.setText(a+" : " + b["price"])


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.infobutton.setText(_translate("MainWindow", "Coin Price"))
        self.maintext.setText(_translate("MainWindow", "Binance Bot"))
        self.label.setText(_translate("MainWindow", "Example: HOTBTC"))
        self.action_XXXBTC.setText(_translate("MainWindow", " XXXBTC"))
        self.action_XXXETH.setText(_translate("MainWindow", " XXXETH"))
        self.action_XXXBNB.setText(_translate("MainWindow", " XXXBNB"))
        self.action_Cache_Reset.setText(_translate("MainWindow", " Cache Reset"))
