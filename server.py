from datetime import datetime

""" Overview:

Server.py should include:
-Configuration options (paper, backtrading, live, etc.)
-Strategy to use (a Strategy object)
-Server setup for the host we decide to use
-A log object

The only tasks that need to be continuously run off this file are:
-strategy.run or strategy.update and any server methods

log(event) is called whenever needed by any object in the global scope.
"""
import trading_clients.AlpacaTrader as at
import strategy.SMAStrategy as smas
import alpaca_trade_api as tradeapi 
import scraper
import time


#data items
trader = at.AlpacaTrader(tradeapi.REST())
assetsToTrade = scraper.get_top_gainers()[0:5]
barTimeframe = "5Min"
assetListLen = len(assetsToTrade)

data = {
    'assetsToTrade': assetsToTrade,
    'barTimeFrame': barTimeFrame,
    'assetListLen': assetListLen
}

strat = smas.Strategy(data, trader)

for i in range(0, 100000):
    strat.update()
    time.sleep(60)


