import binance
import config
import time
import pickledb
import data_control
import tool_func

x=config.x
db=data_control.db
try:
    if (pickledb.load(location="cache").get("error")!=0):
        pass
except:
    error=0

class menu():
    """docstring for menu."""

    def anamenu(self):
        while True:
            print("1.Price\n2.Trade\n3.Wallet\n4.Settings\n5.Exit\n\n")
            giris= input()
            if (giris=="1" or giris=="2" or giris=="3" or giris=="4" or giris=="5"):
                break
            else:
                print("Error!!")
                ti=time.time()
                er="error-"+str(error)
                db.set(er, ti)
                db.set("error", error)
                db.dump()
                time.sleep(1.5)
                continue
        return giris

    def price():
        while True:
            print("1.XXXBTC\n2.XXXETH\n3.XXXBNB\n4.Back")
            time.sleep(2)
            giris= input()
            if (giris=="1" or giris=="2" or giris=="3" or giris=="4"):
                break
            else:
                print("Error!! Please check!!")
                time.sleep(1)
                continue
        if (giris=="1"):
            ap=tool_func.price_func(par="BTC")
            print(ap)
        elif giris=="2":
            ap=tool_func.price_func(par="BTC")
            print(ap)
        elif giris=="3":
            ap=tool_func.price_func(par="BTC")
            print(ap)
        else:
            anamenu()
    def trade():
        while True:
            print("1.XXXBTC\n2.XXXETH\n3.XXXBNB\n4.Back")
            time.sleep(1)
            giris=input()
            if (giris=="1" or giris=="2" or giris=="3" or giris=="4"):
                break
            else:
                print("Error!! Please check!!")
                time.sleep(1)
                continue
        if giris=="1":
            while True:
                print("XXXBTC ? Enter parity. \n")
                giris=input()
                try:
                    a=giris+"BTC"
                    result=x.get_symbol_ticker(symbol=a)
                    return result
                except:
                    print("Please Check! Error!")
                    continue

        elif giris=="2":
            pass
        elif giris=="3":
            pass
        else:
            anamenu()











#
