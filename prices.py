""" 
Using AlphaVantage API to get updated prices of 5 symbols per minute.
"""

import urllib.request, json

API_KEY = "TEBSN97EQCF11024"

""" Uses Quote Endpoint API to get latest price and volume information """
def get_latest_prices(symbols):
    prices = []
    for symbol in symbols:
        alpha_url = "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol="+symbol+"&apikey="+API_KEY
        with urllib.request.urlopen(alpha_url) as url:
            data = json.loads(url.read().decode())
            prices.append(data)
    
    return prices