import binance
import config
import time
import pickledb
import data_control
import tool_func

x = config.x
db_error = data_control.db_error
db_trade = data_control.db_trade
tool = tool_func.tool_func(arg=None)
try:
    if (pickledb_error.load(location="cache/error.db").get("error") != 0):
        pass
except:
    error = 0


class menu():
    """docstring for menu."""

    def __init__(self, hiz=1):
        self.hiz = hiz

    def anamenu():

        while True:
            print("1.Price\n2.Trade\n3.Wallet\n4.Settings\n5.Exit\n\n")
            giris = input()
            if (giris == "1" or giris == "2" or giris == "3" or giris == "4" or giris == "5"):
                break
            else:
                print("Error!!")
                ti = time.time()
                er = "error-" + str(error)
                db_error.set(er, ti)
                db_error.set("error", error)
                db_error.dump()
                time.sleep(1)
                continue
        return giris

    def price():
        while True:
            print("1.XXXBTC\n2.XXXETH\n3.XXXBNB\n4.Back")
            time.sleep(2)
            giris = input()
            if (giris == "1" or giris == "2" or giris == "3" or giris == "4"):
                break
            else:
                print("Error!! Please check!!")
                time.sleep(1)
                continue
        if (giris == "1"):
            ap = tool.price_func(par="BTC")
            print(ap)
        elif giris == "2":
            ap = tool.price_func(par="ETH")
            print(ap)
        elif giris == "3":
            ap = tool.price_func(par="BNB")
            print(ap)
        else:
            menu.anamenu()

    def trade():
        while True:
            print("1.XXXBTC\n2.XXXETH\n3.XXXBNB\n4.Back")
            time.sleep(1)
            giris = input()
            if (giris == "1" or giris == "2" or giris == "3" or giris == "4"):
                break
            else:
                print("Error!! Please check!!")
                time.sleep(1)
                continue
        if giris == "1":
            tool.market_trade("BTC")
        elif giris == "2":
            tool.market_trade("ETH")
        elif giris == "3":
            tool.market_trade("BNB")
        else:
            menu.anamenu()





#
