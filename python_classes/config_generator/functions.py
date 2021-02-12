import ccxt, pandas as pd, numpy as np, json, os

def get_list_exchange():
    return ccxt.exchanges

def get_ccxt_ex(exchange_name):
    return getattr(ccxt, exchange_name)()

def get_list_markets(ccxt_ex):
    return ccxt_ex.fetchMarkets()

def get_list_symbol(list_markets):
    return list(ccxt_ex.fetchMarkets().keys())




class Exchange():
    def __init__(self, name_exchange):
        self.name_exchange = name_exchange
        self.ex = getattr(ccxt, name_exchange)()
        self.list_markets = self.get_list_markets()
        self.config = Config(name_exchange)

    def get_list_markets(self):
        return self.ex.fetchMarkets()

    def get_list_symbol(self):
        return [market['symbol'] for market in self.list_markets]

    # get list possibles params

    def get_possible_type(self):
        try:
            return list(np.unique([market['type'] for market in self.list_markets]))
        except:
            return []

    def get_possible_maker(self):
        try:
            return list(np.unique([market['maker'] for market in self.list_markets]))
        except:
            return []

    def get_possible_taker(self):
        try:
            return list(np.unique([market['taker'] for market in self.list_markets]))
        except:
            return []

    def get_possible_base(self):
        return list(np.unique([market['base'] for market in self.list_markets]))

    def get_possible_quote(self):
        return list(np.unique([market['quote'] for market in self.list_markets]))

    # filters

    def filter_markets_by_symbol(self, symbol):
        if symbol:
            return [market for market in self.list_markets if market['symbol']==symbol][0]
        else:
            print('ERROR symbol is none')
            return self.list_markets 

    def filter_markets_by_base_currency(self, base):
        if base:
            return [market for market in self.list_markets if market['base']==base]
        return self.list_markets

    def filter_markets_by_quote_currency(self, quote):
        if quote:
            return [market for market in self.list_markets if market['quote']==quote]
        return self.list_markets

    def filter_markets_by_type(self, typee):
        if typee:
            return [market for market in self.list_markets if market['type']==typee]
        return self.list_markets

    def filter_markets_by_taker(self, taker):
        if taker:
            return [market for market in self.list_markets if market['taker']==taker]
        return self.list_markets

    def filter_markets_by_maker(self, maker):
        if maker:
            return [market['symbol'] for market in self.list_markets if market['maker']==maker]
        return self.list_markets

    def filter_markets(self, base, quote, typee, taker, maker):
        print([m['symbol'] for m in self.filter_markets_by_base_currency(base)])
        print([m['symbol'] for m in self.filter_markets_by_quote_currency(quote)])
        print([m['symbol'] for m in self.filter_markets_by_type(typee)])
        print([m['symbol'] for m in self.filter_markets_by_maker(maker)])
        print([m['symbol'] for m in self.filter_markets_by_taker(taker)])

        return [market['symbol'] for market in self.list_markets if market['symbol'] in [m['symbol'] for m in self.filter_markets_by_base_currency(base)] and market['symbol'] in [m['symbol'] for m in self.filter_markets_by_quote_currency(quote)] and market['symbol'] in [m['symbol'] for m in self.filter_markets_by_type(typee)] and market['symbol'] in [m['symbol'] for m in self.filter_markets_by_maker(maker)] and market['symbol'] in [m['symbol'] for m in self.filter_markets_by_taker(taker)]]

    # extract info for symbol

    def symbol_get_base(self, symbol):
        return self.filter_markets_by_symbol(symbol)['base']

    def symbol_get_quote(self, symbol):
        return self.filter_markets_by_symbol(symbol)['quote']

    def symbol_get_maker(self, symbol):
        try:
            return self.filter_markets_by_symbol(symbol)['maker']
        except:
            return None

    def symbol_get_taker(self, symbol):
        try:
            return self.filter_markets_by_symbol(symbol)['taker']
        except:
            return None

    def symbol_get_type(self, symbol):
        try:
            return self.filter_markets_by_symbol(symbol)['type']
        except:
            return None

    def symbol_get_active(self, symbol):
        try:
            return self.filter_markets_by_symbol(symbol)['active']
        except:
            return None

    def symbol_get_costMin(self, symbol):
        try:
            return self.filter_markets_by_symbol(symbol)['limits']['cost']['min']
        except:
            return None

    def symbol_get_priceStep(self, symbol):
        try:
            return self.filter_markets_by_symbol(symbol)['precision']['price']
        except:
            return None

    # def order by

    def order_symbol_list(self, symbol_list, sorter):
        if sorter == 'alphabet quote':
            return self.sort_symbol_by_alphabet_quote(symbol_list)
        elif sorter == 'alphabet base':
            return self.sort_symbol_by_alphabet_base(symbol_list)
        elif sorter == '24h quote volume':
            return self.sort_symbol_by_24hquoteVolume(symbol_list)
        elif sorter == '24h base volume':
            return self.sort_symbol_by_24hbaseVolume(symbol_list)
        elif sorter == 'vwap price':
            return self.sort_symbol_by_vwap(symbol_list)
        else:
            return symbol_list

    def sort_symbol_by_alphabet_quote(self, symbol_list):
        sub_list_markets = [market for market in self.list_markets if market['symbol'] in symbol_list]
        return list(pd.DataFrame(sub_list_markets).sort_values('quote').symbol.values)

    def sort_symbol_by_alphabet_base(self, symbol_list):
        sub_list_markets = [market for market in self.list_markets if market['symbol'] in symbol_list]
        return list(pd.DataFrame(sub_list_markets).sort_values('base').symbol.values)

    def sort_symbol_by_24hquoteVolume(self, symbol_list):
        sub_list_markets = [market for market in [dict for key,dict in self.ex.fetchTickers().items()] if market['symbol'] in symbol_list]
        return list(pd.DataFrame(sub_list_markets).fillna(0).sort_values('quoteVolume').iloc[::-1].symbol)

    def sort_symbol_by_24hbaseVolume(self, symbol_list):
        sub_list_markets = [market for market in [dict for key,dict in self.ex.fetchTickers().items()] if market['symbol'] in symbol_list]
        return list(pd.DataFrame(sub_list_markets).fillna(0).sort_values('baseVolume').iloc[::-1].symbol)

    def sort_symbol_by_vwap(self, symbol_list):
        sub_list_markets = [market for market in [dict for key,dict in self.ex.fetchTickers().items()] if market['symbol'] in symbol_list]
        return list(pd.DataFrame(sub_list_markets).fillna(0).sort_values('vwap').iloc[::-1].symbol)



class Config():
    def __init__(self, name_exchange):
        self.name_exchange = name_exchange
        self.list_symbol = []
        self.lob_limit = 20
        self.trades_limit = 100

    def add_symbol(self,symbol):
        if symbol not in self.list_symbol:
            self.list_symbol.append(symbol)

    def reset(self):
        self.__init__(self.name_exchange)

    def save(self):
        with open('config_exe.json','r') as f:
            config_exe = json.load(f)
            f.close()
        txt = 'LIST_SYMBOL={}\nLOB_LIMIT={}\nTRADES_LIMIT={}'.format(str(self.list_symbol),self.lob_limit,self.trades_limit)
        with open('C://Users//Paul Noailly//Work//Trading//crypto//DATA//HF_live_recording/configs/{}.py'.format(self.name_exchange),'w') as f:
            f.write(txt)
            f.close()
