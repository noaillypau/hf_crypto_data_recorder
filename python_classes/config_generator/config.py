import ccxt, pandas as pd, numpy as np, json, os

class Config():
    def __init__(self, name_exchange, config):
        self.name_exchange = name_exchange
        self.list_symbol = []
        self.lob_limit = 20
        self.trades_limit = 100
        self.config = config

    def add_symbol(self,symbol):
        if symbol not in self.list_symbol:
            self.list_symbol.append(symbol)

    def reset(self):
        self.__init__(self.name_exchange)

    def save(self):
        txt = 'LIST_SYMBOL={}\nLOB_LIMIT={}\nTRADES_LIMIT={}'.format(str(self.list_symbol),self.lob_limit,self.trades_limit)
        with open('{}/{}.py'.format(self.config['path_configs_exchange_folder'], self.name_exchange),'w') as f:
            f.write(txt)
            f.close()
