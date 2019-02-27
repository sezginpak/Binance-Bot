import time
from config import x
import data_control
import menu
db_trade= data_control.db_trade


class tool_func(object):
    """docstring for tool_func."""
    def __init__(self, arg):
        super(tool_func, self).__init__()
        self.arg = arg

    def price_func(self, par=None):
        while True:
            print("\nXXX ? \n")
            time.sleep(1)
            giris=input()
            try:
                a=giris+par
                result=x.get_symbol_ticker(symbol=a)
                return result
            except:
                print("Please Check! Error!")
                continue
        return result
    def market_trade(self, tr="BTC"):
        while True:
            print("XXX{} ? Enter parity. \n".format(tr))
            giris = input()
            try:
                a = giris + tr
                tr = giris
                result = x.get_symbol_ticker(symbol=a)
                break
            except:
                print("Please Check! Error!")
                continue
        print(result["price"])
        while True:
            print("1.Market buy\n2.Limit order(coming soon)\n3.Back")
            time.sleep(1)
            giris=input()
            if (giris == "1" or giris == "2" or giris == "3"):
                break
        if giris == "1":
            while True:
                print("How many of coin? %s Back(q)  ", tr)
                time.sleep(1)
                giris = input()
                if giris == "q":
                    menu.menu.trade()
                try:
                    adet = giris
                    while True:
                        print("1.BUY\n2.SELL")
                        giris=input()
                        if (giris=="1" or giris=="2"):
                            break
                    if giris=="1":
                        side="BUY"
                    else:
                        side="SELL"
                    break
                except:
                    print("Error!")
                    time.sleep(0.8)
                    continue
            y=x.create_test_order(symbol=a, type="MARKET", side=side, quantity=adet)
            while True:
                try:
                    db_trade.ladd('trade_log', value=y)
                    break
                except:
                    db_trade.lcreate('trade_log')
                    continue
        elif giris == "2":
            pass
        else:
            menu.menu.trade()
