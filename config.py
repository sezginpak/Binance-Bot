from binance import client
from currency_converter import currency_converter
import pickledb
db=pickledb.load('debug/config_api.db', auto_dump=True)

y=currency_converter.CurrencyConverter()

ak=db.get('api_key')
ask=db.get('api_secret_key')
x = client.Client(api_key=ak , api_secret=ask)
