from strategy.Strategy import Strategy
import talib
import numpy as np


class SMAStrategy(Strategy):
    def run(self):
        return
    
    def update(self, new_data):
        iteratorPos = 0
        while iteratorPos < self.data['assetListLen']:
            symbol = self.data['assetsToTrade'][iteratorPos]
            
            returned_data = self.trader.get_barset(symbol,barTimeframe,limit=100)
            
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
                    openPosition = trader.get_position(symbol)
                    cashBalance = trader.get_account().cash  
                    returned = trader.submit_order(symbol,100,"buy","market","gtc") # Market order to open position
                    print("buying")
                # Opens new position if one does not exist
                except:
                    cashBalance = trader.get_account().cash  
                    returned = trader.submit_order(symbol,100,"buy","market","gtc") # Market order to open position
                    print("buying")
                
            else:
                # Closes position if SMA20 is below SMA50
                #openPosition = api.get_position(symbol)
                #returned = api.submit_order(symbol,10,"sell","market","gtc") 
                try:
                    returned = trader.submit_order(symbol,10,"sell","market","gtc") # Market order to fully close position
                    print("selling")
                except:
                    print("error")
            
            iteratorPos += 1
