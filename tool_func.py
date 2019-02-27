import time
from config import x



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
