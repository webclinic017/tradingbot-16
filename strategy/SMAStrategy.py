from strategy.Strategy import Strategy
import talib
import numpy as np
import scraper


class SMAStrategy(Strategy):
    def run(self):
        assetsToTrade = scraper.get_top_gainers()[0:5]
        self.barTimeFrame = "1D"
        assetListLen = len(assetsToTrade)

        self.data = {
            'assetsToTrade': assetsToTrade,
            'barTimeFrame': self.barTimeFrame,
            'assetListLen': assetListLen
        }
        
        return
    
    def update(self, new_data):
        iteratorPos = 0
        while iteratorPos < self.data['assetListLen']:
            symbol = self.data['assetsToTrade'][iteratorPos]
            
            returned_data = self.trader.get_barset(symbol,self.barTimeFrame,limit=100)
            
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
                    openPosition = self.trader.get_position(symbol)
                    cashBalance = self.trader.get_account().cash  
                    returned = self.trader.submit_order(symbol,100,"buy","market","gtc", close_price=closeList[-1]) # Market order to open position
                    print("buying")
                # Opens new position if one does not exist
                except:
                    cashBalance = self.trader.get_account().cash  
                    returned = self.trader.submit_order(symbol,100,"buy","market","gtc", close_price=closeList[-1]) # Market order to open position
                    print("buying")
                
            else:
                # Closes position if SMA20 is below SMA50
                #openPosition = api.get_position(symbol)
                #returned = api.submit_order(symbol,10,"sell","market","gtc") 
                try:
                    returned = self.trader.submit_order(symbol,10,"sell","market","gtc", close_price=closeList[-1]) # Market order to fully close position
                    print("selling")
                except:
                    print("error")
            
            iteratorPos += 1
