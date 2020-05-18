from trading_clients.Trader import Trader
from pandas_datareader import data as pdr
from datetime import date
import yfinance as yf
import pandas as pd


class Backtrader(Trader):
    yf.pdr_override()
    # List of orders placed
    log = []

    # List of Yahoo Finance CSVs
    files = []

    # add more member variables to keep track of more things
    timestamp = 0
    increment = 1

    def get_account(self):
        class Object(object):
            pass
        act = Object()
        act.cash = 10000

        return act
    

    def get_position(self, symbol):
        #This function would normally throw an exception if position not found
        return None
    
    def submit_order(self, symbol, qty, side, type, time_in_force, 
        limit_price=None, stop_price=None, client_order_id=None, order_class=None, take_profit=None, stop_loss=None):
        #This function would normally return an Order object

        params = [symbol, qty, side, type, time_in_force, limit_price, stop_price, client_order_id, order_class, take_profit, stop_loss]
        orders_dict = dict.fromkeys(params, 1)

        self.log.append(orders_dict)
        
        return True


    def save_data(self, df, filename):
        df.to_csv('./data/'+filename+'.csv')


    def get_data(self, ticker):
        today = date.today()
        start_date = "2017-01-01"
        end_date = today
    
        data = pdr.get_data_yahoo(ticker, start=start_date, end=end_date)
        dataname = ticker + "_" + str(today)

        print(dataname, " being created")
        self.files.append(dataname)
        self.save_data(data, dataname)

        return dataname

    
    
    def get_barset(self, symbol, barTimeframe,limit=100):
        class Object(object):
            pass
        
        barset = {}
        bars = []

        # Fill bars
        datafile = self.get_data(symbol)
        print(datafile, " created")

        df = pd.read_csv('./data/'+datafile+'.csv')

        # Add bars to list based on barTimeframe
        n = 0
        if barTimeframe == "5Min":
            n = 5
        
        for i in range(n):
            df_row = df[i:i+1]

            bar = Object()
            bar.t = df_row['Date']
            bar.o = df_row['Open']
            bar.h = df_row['High']
            bar.l = df_row['Low']
            bar.c = df_row['Close']
            bar.v = df_row['Volume']

            bars.append(bar)

        # Increment time
        self.timestamp += self.increment

        barset[symbol] = bars
        return barset
