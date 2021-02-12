import ccxt, pandas as pd, numpy as np, json, os

def get_list_exchange():
    return ccxt.exchanges

def get_ccxt_ex(exchange_name):
    return getattr(ccxt, exchange_name)()

def get_list_markets(ccxt_ex):
    return ccxt_ex.fetchMarkets()

def get_list_symbol(list_markets):
    return list(ccxt_ex.fetchMarkets().keys())