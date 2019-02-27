import binance
import config
import time
import pickledb
import data_control
import tool_func

x=config.x
db_error=data_control.db
tool = tool_func.tool_func(arg=None)
try:
    if (pickledb_error.load(location="cache/error").get("error")!=0):
        pass
except:
    error=0

class menu():
    """docstring for menu."""
    def __init__(self, hiz=1):
        self.hiz=hiz


    def anamenu():

        while True:
            print("1.Price\n2.Trade\n3.Wallet\n4.Settings\n5.Exit\n\n")
            giris = input()
            if (giris=="1" or giris=="2" or giris=="3" or giris=="4" or giris=="5"):
                break
            else:
                print("Error!!")
                ti=time.time()
                er="error-"+str(error)
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
            giris= input()
            if (giris=="1" or giris=="2" or giris=="3" or giris=="4"):
                break
            else:
                print("Error!! Please check!!")
                time.sleep(1)
                continue
        if (giris=="1"):
            ap=tool.price_func(par="BTC")
            print(ap)
        elif giris=="2":
            ap=tool.price_func(par="ETH")
            print(ap)
        elif giris=="3":
            ap=tool.price_func(par="BNB")
            print(ap)
        else:
            menu.anamenu()
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
                    tr=giris
                    result=x.get_symbol_ticker(symbol=a)
                    break
                except:
                    print("Please Check! Error!")
                    continue
            print(result["price"])
            while True:
                print("1.Market buy\n2.Limit order(coming soon)\n3.Back")
                time.sleep(1)
                if (giris=="1" or giris=="2" or giris=="3"):
                    break
            if giris=="1":
                while True:
                    print("How many of coin? %s Back(q)  ", tr)
                    time.sleep(1)
                    giris=input()
                    if giris=="q":
                        anamenu.trade()
                    try:
                        adet=int(giris)
                        break
                    except:
                        print("Error!")
                        time.sleep(0.8)
                        continue
                while True:
                    break
            elif giris=="2":
                pass
            else:
                menu.trade()
        elif giris=="2":
            pass
        elif giris=="3":
            pass
        else:
            menu.anamenu()











#
