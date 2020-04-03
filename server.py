import prices
import scraper
import alpaca_trade_api as tradeapi 
import time
from datetime import datetime
import numpy as np
import talib
assetsToTrade = scraper.get_top_gainers()[0:5]


#alpaca api
api = tradeapi.REST()

# api for placing paper trading
barTimeframe = "5Min" # 1Min, 5Min, 15Min, 1H, 1D

positionSizing = 0.25

# Tracks position in list of symbols to download
iteratorPos = 0 
assetListLen = len(assetsToTrade)

for i in range(0, 100000):
    while iteratorPos < assetListLen:
        symbol = assetsToTrade[iteratorPos]
        
        returned_data = api.get_barset(symbol,barTimeframe,limit=100)
        
        timeList = []
        openList = []
        highList = []
        lowList = []
        closeList = []
        volumeList = []

        # Reads, formats and stores the new bars
        for bar in returned_data[symbol]:
            timeList.append(bar.t)
            openList.append(bar.o)
            highList.append(bar.h)
            lowList.append(bar.l)
            closeList.append(bar.c)
            volumeList.append(bar.v)
        
        # Processes all data into numpy arrays for use by talib
        timeList = np.array(timeList)
        openList = np.array(openList,dtype=np.float64)
        highList = np.array(highList,dtype=np.float64)
        lowList = np.array(lowList,dtype=np.float64)
        closeList = np.array(closeList,dtype=np.float64)
        volumeList = np.array(volumeList,dtype=np.float64)

        # Calculated trading indicators
        SMA20 = talib.SMA(closeList,20)[-1]
        SMA50 = talib.SMA(closeList,50)[-1]
        print(SMA20, SMA50)
        # Calculates the trading signals
        if SMA20 > SMA50:
            try:
                openPosition = api.get_position(symbol)
                cashBalance = api.get_account().cash  
                returned = api.submit_order(symbol,100,"buy","market","gtc") # Market order to open position
                print("buying")
            # Opens new position if one does not exist
            except:
                cashBalance = api.get_account().cash  
                returned = api.submit_order(symbol,100,"buy","market","gtc") # Market order to open position
                print("buying")
            
        else:
            # Closes position if SMA20 is below SMA50
            #openPosition = api.get_position(symbol)
            #returned = api.submit_order(symbol,10,"sell","market","gtc") 
            try:
                returned = api.submit_order(symbol,10,"sell","market","gtc") # Market order to fully close position
                print("selling")
            except:
                print("error")
        
        iteratorPos += 1
    time.sleep(60)
    iteratorPos = 0

# For alpaca account information 
#account = api.get_account()

# For querying market data from alpaca
#barset = api.get_barset(symbol, 'day', limit=5)
# aapl_bars = barset[symbol]


