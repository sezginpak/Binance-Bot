import threading
import time
from concurrent.futures import ThreadPoolExecutor
import pickledb
executor=ThreadPoolExecutor(max_workers=5)

# from mainwin import Ui_MainWindow

db=pickledb.load('debug/config_api.db', auto_dump=True)


class func(object):

    def infocoin_coin2(self, buton, label):
        a=buton.text()
        if a=="Stop":
            label.setText("Error! Please Stop...")
        else:
            self.infocoin_coin(i_buton=self.infobutton, label=self.label_2, input_coin=self.inputcoininfo)

    def info_price(self):
        self.infocoin_coin(self.infobutton,self.label_2, self.inputcoininfo)
    def infocoin_coin(self, i_buton, label, input_coin):

        i_buton.setDown(True)
        while True:
            if db.get('api_key')==False:
                label.setText('Error Api Not Found!!')
                break
            else:
                from config import x, y
                self.control()
            a=input_coin.text()
            b=x.get_symbol_ticker(symbol=a)
            label.setText(a+" : " + (b["price"]))
            self.coin_price_reflesh(button=self.infobutton,t_func=self.coin_price_info_reflesh2, clicked_connect_func=self.coin_price_info_reflesh_stop, button_text=self.infobutton, input_line=self.inputcoininfo)
            break

    def error_notification(self):
        self.label_2.setText("")
    def coin_price_info_reflesh_stop(self):
        self.i=True
        self.infobutton.setText("Coin Price")
        self.infobutton.clicked.connect(self.infocoin_coin)
        self.inputcoininfo.setEnabled(True)

    def coin_price_reflesh(self, i=False, button=None, button_text="", t_func=None, clicked_connect_func=None, input_line=None):
        self.i=i
        threading.Thread(target=t_func).start()
        button.setText("Stop")
        button_text.clicked.connect(clicked_connect_func)
        input_line.setEnabled(False)
    def coin_price_info_reflesh2(self):
        from config import x
        while self.i==False:
            a=self.inputcoininfo.text()
            b=x.get_symbol_ticker(symbol=a)
            self.label_2.setText(a+" : " + (b["price"]))
            threading.Thread(target=time.sleep(0.2)).start()
    def api_key_settings_configure(self):
        while True:
            line_text=self.input_api_key_settings.text()
            line_secret_text=self.input_api_secret_key_settings.text()
            if line_text=="" or line_secret_text=="":
                break
            self.input_api_key_settings.setEnabled(False)
            self.input_api_secret_key_settings.setEnabled(False)
            db.set('api_key', line_text)
            db.set('api_secret_key', line_secret_text)
            db.dump()
            break
    def api_key_settings_reset(self):
        db.deldb()

        self.input_api_key_settings.setText("")
        self.input_api_secret_key_settings.setText("")
        self.input_api_key_settings.setEnabled(True)
        self.input_api_secret_key_settings.setEnabled(True)
    def control(self):
        if db.get('api_key')!=False:
            self.input_api_key_settings.setEnabled(False)
            self.input_api_secret_key_settings.setEnabled(False)
        else:
            self.input_api_key_settings.setEnabled(True)
            self.input_api_secret_key_settings.setEnabled(True)

    def coin_price_reflesh_trade(self, text):
        from config import x
        i=0
        while i<=2:
            try:
                arg=x.get_symbol_ticker(symbol=text)
                threading.Thread(target=reflesh(arg, text)).start()
                break
            except:
                i+=1
            threading.Thread(target=time.sleep(0.15)).start()

        def reflesh(arg, text):
            self.label_4.text(text + " : " + arg['price'])













#
