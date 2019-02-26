
def price_func(par=None):
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
