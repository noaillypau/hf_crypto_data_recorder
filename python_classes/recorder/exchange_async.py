import ccxt.async_support as ccxt # async ccxt
import aiofiles as aiof # async write in file
import numpy as np, time, datetime


class Exchange():
    def __init__(self, name_exchange, config_exchange):
        # reprocess entry
        self.config = config_exchange
        self.limit_lob = min(config_exchange.LOB_LIMIT,20)
        self.limit_trades = min(config_exchange.TRADES_LIMIT,500)
        # create ccxt exchange
        self.exchange = getattr(ccxt, name_exchange) () 
        self.name_exchange = name_exchange

    # main functions

    async def record_data(self, symbol):
        data_to_reccord = await self.get_data(symbol)
        await self.upload_data(symbol, data_to_reccord)

    async def get_data(self, symbol):
        lob = await self.exchange.fetch_order_book(symbol, limit=self.limit_lob)
        trades = await self.exchange.fetchTrades(symbol, limit=self.limit_trades)
        ticker = await self.exchange.fetchTicker(symbol)
        return self.process_data(lob, trades, ticker)

    async def upload_data(self, symbol, data_to_reccord):
        date_ticker = datetime.datetime.fromtimestamp(data_to_reccord['timestamp_ticker']/1000)
        filename = '{}_{}_{}{}{}{}.txt'.format(self.name_exchange,symbol.replace('/',''),date_ticker.year,date_ticker.month,date_ticker.day,date_ticker.hour)
        async with aiof.open('data/'+filename, "a") as out:
            await out.write(str(data_to_reccord)+'|')
            await out.flush()


    # sub familly data

    def process_ticker_data(self, ticker):
        dict_ticker = {}
        dict_ticker['timestamp_ticker'] = ticker['timestamp']
        dict_ticker['bid'] = ticker['bid']
        dict_ticker['ask'] = ticker['ask']
        dict_ticker['vwap'] = ticker['vwap']
        dict_ticker['bidVolume'] = ticker['bidVolume']
        dict_ticker['askVolume'] = ticker['askVolume']
        dict_ticker['base24hVolume'] = ticker['baseVolume']
        dict_ticker['quote24hVolume'] = ticker['quoteVolume']
        return dict_ticker

    def process_trades_data(self, trades):
        dict_trades = {}
        # extract arrays
        list_price = np.array([trade['price'] for trade in trades])
        list_buyPrice = np.array([trade['price'] for trade in trades if trade['side']=='buy'])
        list_sellPrice = np.array([trade['price'] for trade in trades if trade['side']=='sell'])
        list_volume = np.array([trade['amount'] for trade in trades])
        list_buyVolume = np.array([trade['amount'] for trade in trades if trade['side']=='buy'])
        list_sellVolume = np.array([trade['amount'] for trade in trades if trade['side']=='sell'])
        # std price
        dict_trades['trades_std_price'] = list_price.std()
        dict_trades['trades_std_buyPrice'] = list_buyPrice.std()
        dict_trades['trades_std_sellPrice'] = list_sellPrice.std()
        # std volume
        dict_trades['trades_std_volume'] =list_volume.std()
        dict_trades['trades_std_buyVolume'] = list_buyVolume.std()
        dict_trades['trades_std_sellVolume'] = list_sellVolume.std()
        # sum volume
        dict_trades['trades_volume'] = list_volume.sum()
        dict_trades['trades_buyVolume'] = list_buyVolume.sum()
        dict_trades['trades_sellVolume'] = list_sellVolume.sum()
        # timing
        dict_trades['trades_total_time'] =  (trades[-1]['timestamp'] - trades[0]['timestamp'])
        dict_trades['trades_nbs_trades'] = len(trades)
        return dict_trades

    def process_lob_data(self, lob):
        dict_lob = {}
        i = 0
        for price, volume in lob['bids']:
            dict_lob['bidVolume_{}'.format(i)] = volume
            dict_lob['bidPrice_{}'.format(i)] = price
            i += 1
        i = 0
        for price, volume in lob['asks']:
            dict_lob['askVolume_{}'.format(i)] = volume
            dict_lob['askPrice_{}'.format(i)] = price
            i += 1
        dict_lob['timestamp_lob'] = lob['timestamp']
        return dict_lob

    def process_data(self, lob, trades, ticker):
        return {**self.process_ticker_data(ticker), **self.process_trades_data(trades), **self.process_lob_data(lob)}


    async def debug(self, symbol):
        dict_ticker = await self.get_ticker_data(symbol)
        dict_trades = await self.get_trades_data(symbol)
        dict_lob = await self.get_lob_data(symbol)
        data_to_reccord = {**dict_ticker, **dict_trades, **dict_lob}
        for key, item in data_to_reccord.items():
            print('{}: {}'.format(key,item))
        print('\n')
