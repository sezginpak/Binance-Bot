# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'deneme.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from config import x, y
from concurrent.futures import ThreadPoolExecutor
executor=ThreadPoolExecutor(max_workers=5)



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 275)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 401, 231))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tabWidget.setToolTipDuration(-1)
        self.tabWidget.setObjectName("tabWidget")

        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")

        self.infobutton = QtWidgets.QPushButton(self.tab1)
        self.infobutton.setGeometry(QtCore.QRect(40, 120, 101, 31))
        self.infobutton.setStyleSheet("")
        self.infobutton.setObjectName("infobutton")

        self.inputcoininfo = QtWidgets.QLineEdit(self.tab1)
        self.inputcoininfo.setGeometry(QtCore.QRect(30, 90, 121, 16))
        self.inputcoininfo.setInputMethodHints(QtCore.Qt.ImhLatinOnly|QtCore.Qt.ImhPreferUppercase|QtCore.Qt.ImhUppercaseOnly)
        self.inputcoininfo.setInputMask("")
        self.inputcoininfo.setText("")
        self.inputcoininfo.setMaxLength(8)
        self.inputcoininfo.setDragEnabled(False)
        self.inputcoininfo.setReadOnly(False)
        self.inputcoininfo.setClearButtonEnabled(False)
        self.inputcoininfo.setObjectName("inputcoininfo")

        self.label = QtWidgets.QLabel(self.tab1)
        self.label.setGeometry(QtCore.QRect(40, 60, 111, 21))
        self.label.setObjectName("label")

        self.maintext = QtWidgets.QLabel(self.tab1)
        self.maintext.setGeometry(QtCore.QRect(30, 10, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.maintext.setFont(font)
        self.maintext.setScaledContents(False)
        self.maintext.setAlignment(QtCore.Qt.AlignCenter)
        self.maintext.setWordWrap(False)
        self.maintext.setObjectName("maintext")

        self.label_2 = QtWidgets.QLabel(self.tab1)
        self.label_2.setGeometry(QtCore.QRect(220, 70, 141, 31))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.tab1, "")
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")

        self.input_coin_trade = QtWidgets.QLineEdit(self.tab2)
        self.input_coin_trade.setGeometry(QtCore.QRect(60, 90, 121, 16))
        self.input_coin_trade.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.input_coin_trade.setInputMask("")
        self.input_coin_trade.setText("")
        self.input_coin_trade.setMaxLength(8)
        self.input_coin_trade.setDragEnabled(False)
        self.input_coin_trade.setReadOnly(False)
        self.input_coin_trade.setClearButtonEnabled(False)
        self.input_coin_trade.setObjectName("input_coin_trade")

        self.example_trade = QtWidgets.QLabel(self.tab2)
        self.example_trade.setGeometry(QtCore.QRect(50, 60, 111, 21))
        self.example_trade.setObjectName("example_trade")

        self.infobutton_trade = QtWidgets.QPushButton(self.tab2)
        self.infobutton_trade.setGeometry(QtCore.QRect(70, 150, 101, 31))
        self.infobutton_trade.setStyleSheet("")
        self.infobutton_trade.setObjectName("infobutton_trade")
        self.coin_price_trade = QtWidgets.QLabel(self.tab2)
        self.coin_price_trade.setGeometry(QtCore.QRect(210, 60, 141, 31))
        self.coin_price_trade.setText("")
        self.coin_price_trade.setObjectName("coin_price_trade")

        self.result_trade = QtWidgets.QLabel(self.tab2)
        self.result_trade.setGeometry(QtCore.QRect(210, 120, 141, 31))
        self.result_trade.setText("")
        self.result_trade.setObjectName("result_trade")

        self.input_coin_count_trade = QtWidgets.QLineEdit(self.tab2)
        self.input_coin_count_trade.setGeometry(QtCore.QRect(60, 120, 121, 16))
        self.input_coin_count_trade.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.input_coin_count_trade.setInputMask("")
        self.input_coin_count_trade.setText("")
        self.input_coin_count_trade.setMaxLength(8)
        self.input_coin_count_trade.setDragEnabled(False)
        self.input_coin_count_trade.setReadOnly(False)
        self.input_coin_count_trade.setClearButtonEnabled(False)
        self.input_coin_count_trade.setObjectName("input_coin_count_trade")

        self.label_3 = QtWidgets.QLabel(self.tab2)
        self.label_3.setGeometry(QtCore.QRect(0, 120, 57, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab2)
        self.label_4.setGeometry(QtCore.QRect(20, 90, 41, 20))
        self.label_4.setObjectName("label_4")

        self.maintext_2 = QtWidgets.QLabel(self.tab2)
        self.maintext_2.setGeometry(QtCore.QRect(40, 20, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.maintext_2.setFont(font)
        self.maintext_2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.maintext_2.setScaledContents(False)
        self.maintext_2.setAlignment(QtCore.Qt.AlignCenter)
        self.maintext_2.setWordWrap(False)
        self.maintext_2.setObjectName("maintext_2")
        self.tabWidget.addTab(self.tab2, "")
        self.tab3 = QtWidgets.QWidget()
        self.tab3.setObjectName("tab3")

        self.input_api_key_settings = QtWidgets.QLineEdit(self.tab3)
        self.input_api_key_settings.setGeometry(QtCore.QRect(110, 30, 251, 21))
        self.input_api_key_settings.setObjectName("input_api_key_settings")
        self.api_key_settings = QtWidgets.QLabel(self.tab3)
        self.api_key_settings.setGeometry(QtCore.QRect(50, 30, 57, 16))
        self.api_key_settings.setObjectName("api_key_settings")
        self.api_secret_key_settings = QtWidgets.QLabel(self.tab3)
        self.api_secret_key_settings.setGeometry(QtCore.QRect(10, 60, 101, 16))
        self.api_secret_key_settings.setObjectName("api_secret_key_settings")
        self.input_api_secret_key_settings = QtWidgets.QLineEdit(self.tab3)
        self.input_api_secret_key_settings.setGeometry(QtCore.QRect(110, 60, 251, 21))
        self.input_api_secret_key_settings.setObjectName("input_api_secret_key_settings")
        self.configure_button_settings = QtWidgets.QPushButton(self.tab3)
        self.configure_button_settings.setGeometry(QtCore.QRect(110, 90, 121, 32))
        self.configure_button_settings.setObjectName("configure_button_settings")
        self.reset_button_settings = QtWidgets.QPushButton(self.tab3)
        self.reset_button_settings.setGeometry(QtCore.QRect(240, 90, 121, 32))
        self.reset_button_settings.setObjectName("reset_button_settings")

        self.tabWidget.addTab(self.tab3, "")
        #MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 22))
        self.menubar.setObjectName("menubar")
        #MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        #MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.infobutton.clicked.connect(self.infocoin_coin2)
        self.infobutton_trade.clicked.connect(self.coin_price_trade.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def infocoin_coin2(self):
        a=self.infobutton.text()
        if a=="Stop":
            self.label_2.setText("Error! Please Stop...")
        else:
            self.infocoin_coin()
    def infocoin_coin(self):
        self.infobutton.setDown(True)
        while True:
            a=self.inputcoininfo.text()
            i=False
            c=a
            if True==a.endswith('TL'):
                turkish_liras=y.convert(1, 'USD', 'TRY')
                a=a.replace("TL","")
                a=a+"USDT"
            try:
                b=x.get_symbol_ticker(symbol=a)
            except:
                import time
                ti=time.time()
                self.label_2.setText("Error!!")
                executor.submit(threading.Timer(3, self.error_notification).start())

                threading.Timer(3, self.error_notification).start()

                print(threading.active_count())
                i=True
            if i==False:
                if True==c.endswith('TL'):
                    self.label_2.setText(c+" : " + (str(float(b["price"])*float(turkish_liras))))
                else:
                    self.label_2.setText(c+" : " + (b["price"]))
                    self.coin_price_reflesh()
            break

    def error_notification(self):
        self.label_2.setText("")
    def coin_price_reflesh_stop(self):
        self.i=True
        self.infobutton.setText("Coin Price")
        self.infobutton.clicked.connect(self.infocoin_coin2)
        self.inputcoininfo.setEnabled(True)

    def coin_price_reflesh(self, i=False):
        self.i=i
        threading.Thread(target=self.coin_price_reflesh2).start()
        self.infobutton.setText("Stop")
        self.infobutton.clicked.connect(self.coin_price_reflesh_stop)
        self.inputcoininfo.setEnabled(False)
    def coin_price_reflesh2(self):
        import time
        while self.i==False:
            a=self.inputcoininfo.text()
            b=x.get_symbol_ticker(symbol=a)
            self.label_2.setText(a+" : " + (b["price"]))
            threading.Thread(target=time.sleep(0.2)).start()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Binance Bot"))
        self.infobutton.setText(_translate("MainWindow", "Coin Price"))
        self.label.setText(_translate("MainWindow", "Example: HOTBTC"))
        self.maintext.setText(_translate("MainWindow", "Binance Bot"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("MainWindow", "Coin Price"))
        self.example_trade.setText(_translate("MainWindow", "Example: HOTBTC"))
        self.infobutton_trade.setText(_translate("MainWindow", "Coin Price"))
        self.label_3.setText(_translate("MainWindow", "Amount :"))
        self.label_4.setText(_translate("MainWindow", "Coin :"))
        self.maintext_2.setText(_translate("MainWindow", "Market Buy"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("MainWindow", "Trade"))
        self.api_key_settings.setText(_translate("MainWindow", "API Key :"))
        self.api_secret_key_settings.setText(_translate("MainWindow", "API Secret Key :"))
        self.configure_button_settings.setText(_translate("MainWindow", "Configure"))
        self.reset_button_settings.setText(_translate("MainWindow", "Reset"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), _translate("MainWindow", "Settings"))
