import threading
import time
from concurrent.futures import ThreadPoolExecutor
import pickledb
executor=ThreadPoolExecutor(max_workers=5)

# from mainwin import Ui_MainWindow

db=pickledb.load('debug/config_api.db', auto_dump=True)


class func(object):

    def infocoin_coin2(self):
        a=self.infobutton.text()
        if a=="Stop":
            self.label_2.setText("Error! Please Stop...")
        else:
            self.infocoin_coin()
    def infocoin_coin(self):

        self.infobutton.setDown(True)
        while True:
            if db.get('api_key')==False:
                self.label_2.setText('Error Api Not Found!!')
                break
            else:
                from config import x, y
                self.control()
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
                self.label_2.setText("Error!!")
                executor.submit(threading.Timer(3, self.error_notification).start())
                threading.Timer(3, self.error_notification).start()
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
        from config import x, y
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















#
