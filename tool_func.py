from PyQt5.Qt import QThread
import time
from PyQt5.QtCore import pyqtSignal
import threading
# from concurrent.futures import ThreadPoolExecutor
import pickledb
# executor=ThreadPoolExecutor(max_workers=5)

# from mainwin import Ui_MainWindow

# db=pickledb.load('debug/config_api.db', auto_dump=True)
from config import db

class func(object):
    def start_func(self):
        self.db=db
        for i in self.db.lgetall('coin_parity'):
            self.coin_price_combo.addItem(i)
    def info_price(self):
        try:
            self.text=self.coin_price_combo.currentText()
            self.text=self.text.upper()
        except:
            pass
        def response_price(label, combo):
            from config import x
            # try:
            x.get_symbol_ticker(symbol=self.text)
            response_price_print(self.coin_price_combo.currentText(), 0, 0)
                # QtCore.QMetaObject.invokeMethod(combo, "setEnabled", QtCore.Qt.QueuedConnection, QtCore.Q_ARG(bool, False))
            # except:
            #     print('hataa')
            #     self.cont_res_while=False

        def response_price_print(text, label, combo):
            from config import x
            if label==0 and combo==0:
                self.infobutton.setText("Stop")

                while self.cont_res_while==True:
                    try:
                        res=x.get_symbol_ticker(symbol=text)
                        self.label_2.setText(text+" : " + res['price'])
                    except:
                        print("hata")
            elif label==1 and combo==1:
                pass

            elif tab==1:
                pass
        if 0==self.tabWidget.currentIndex():
            threading.Thread(target=response_price, args=(0, 0)).start()
            self.button_connect(tab=0)
                # threading.Timer(0.2, response_price, args=(self.label_2, self.coin_price_combo,)).start()
        else:
            pass
    def button_connect(self,tab=0):
        if tab==0:
            self.infobutton.clicked.connect(self.response_price_while_stopper)

    def control(self):
        self.cont_res_while=True

    def response_price_while_stopper(self):
        self.cont_res_while=False
        # self.coin_price_combo.setEditable(True)
        self.infobutton.clicked.connect(self.info_price)
        self.infobutton.setText("Coin Price")



# class TimerThread(QThread):
#     update = pyqtSignal()
#
#     def __init__(self, event):
#         QThread.__init__(self)
#         self.stopped = event
#
#     def run(self):
#         while not self.stopped.wait(0.02):
#             self.update.emit()












#
