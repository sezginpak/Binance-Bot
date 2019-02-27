import pickledb

db_error = pickledb.load('cache/error.db', auto_dump=True)

db_trade = pickledb.load('cache/trade_log.db', auto_dump=True)
