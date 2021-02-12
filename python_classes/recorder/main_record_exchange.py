import asyncio
import os, sys, time
import argparse, datetime, os, json
from log import log
from exchange_async import Exchange
import importlib
import ccxt as ccxt_not_async


root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root + '/python')



# arg parser
parser = argparse.ArgumentParser()
parser.add_argument("exchange")
args = parser.parse_args()
exchange_name = args.exchange

# check if we have a config for the given parser, if we do, check if all symbol in config are supported for inputed exchange
if '{}.py'.format(exchange_name) in os.listdir('configs/'):
    log('Importing config for exchange {}'.format(exchange_name))
    path_config = 'configs'
    spec = importlib.util.spec_from_file_location(exchange_name, path_config+'/{}.py'.format(exchange_name))
    config_exchange = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(config_exchange)
else:
    log('Exchange <{}> have no saved configs'.format(exchange_name))
    list_exch_configs = [filename.replace('ex_','').replace('.json','') for filename in os.listdir('configs/') if 'ex_' in filename]
    log('List of exchange configs availables: {} \n'.format(' / '.join(list_exch_configs)))
    quit()



import ccxt.async_support as ccxt

async def main2(exchange_name, config_exchange):
    exchange = Exchange(exchange_name, config_exchange)
    while True:
        input_coroutines = [exchange.record_data(symbol) for symbol in config_exchange.LIST_SYMBOL]
        successes = await asyncio.gather(*input_coroutines, return_exceptions=True)
         

loop = asyncio.get_event_loop()
loop.run_until_complete(main2(exchange_name, config_exchange))