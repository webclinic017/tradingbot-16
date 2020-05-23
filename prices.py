""" 
Overview:
prices.py includes:
- Method to get price data of given symbols from AlphaVantage

To-do:
- Hide API keys
- Add more functions to generate more data
- Make functions usable in Backtrader.py
"""

import urllib.request
import json

API_KEY = "TEBSN97EQCF11024"


def get_latest_prices(symbols):
    """Uses Quote Endpoint API to get latest price and volume information

    Arguments:
        symbols {list} -- A list of symbols (strings) from the NYSE

    Returns:
        [dict] -- A dictionary of data in the format {symbol: data} where data is the object returned by the API
    """
    prices = {}
    for symbol in symbols:
        alpha_url = "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=" + \
            symbol+"&apikey="+API_KEY
        with urllib.request.urlopen(alpha_url) as url:
            data = json.loads(url.read().decode())
            prices[symbol] = data

    return prices
