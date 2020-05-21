from trading_clients.Trader import Trader
from pandas_datareader import data as pdr
from datetime import date
import yfinance as yf
import pandas as pd
from pathlib import Path
import datetime as datetime
import csv

class Backtrader(Trader):
    yf.pdr_override()
    # List of orders placed
    log = []

    # List of Yahoo Finance CSVs
    files = []

    # add more member variables to keep track of more things
    increment = 1

    def get_account(self):
        return self.api
    

    def get_position(self, symbol):
        #This function would normally throw an exception if position not found
        return None
    
    def submit_order(self, symbol, qty, side, type, time_in_force, 
        limit_price=None, stop_price=None, client_order_id=None, order_class=None, take_profit=None, stop_loss=None, close_price=None):
        #This function would normally return an Order object
        print("order submitted")
        params = [symbol, qty, side, type, time_in_force, limit_price, stop_price, client_order_id, order_class, take_profit, stop_loss, close_price]
        orders_dict = dict.fromkeys(params, 1)

        self.log.append(orders_dict)

        # append as row to csv
        with open(self.api.output_file, "a") as fp:
            print("writing order to file")
            wr = csv.writer(fp, dialect='excel')
            wr.writerow(params)
        
        return True


    def save_data(self, df, filename):
        df.to_csv('./data/'+filename+'.csv')


    def get_data(self, ticker):
        today = date.today()
        start_date = self.api.start_date
        end_date = today
    
        data = pdr.get_data_yahoo(ticker, start=start_date, end=end_date)
        dataname = ticker + "_" + str(today)

        print(dataname, " being created")
        self.files.append(dataname)
        self.save_data(data, dataname)

        return dataname

    
    
    def get_barset(self, symbol, barTimeframe,limit=100):
        print("getting barset for: ", symbol)
        class Object(object):
            pass
        today = date.today()
        dataname = symbol + "_" + str(today)
        barset = {}
        bars = []

        datafile = Path('./data/'+dataname+'.csv')

        if not datafile.exists():
            datafile = self.get_data(symbol)
            print(datafile, " created")

        # Fill bars
        df = pd.read_csv('./data/'+dataname+'.csv')

        # Add bars to list based on barTimeframe
        rows = df.shape[0]

        for i in range(self.api.timestamp-limit, min(self.api.timestamp, rows)):
            bar = Object()
            bar.t = df.iloc[i]['Date']
            bar.o = df.iloc[i]['Open']
            bar.h = df.iloc[i]['High']
            bar.l = df.iloc[i]['Low']
            bar.c = df.iloc[i]['Close']
            bar.v = df.iloc[i]['Volume']

            bars.append(bar)

            

        # Increment time
        self.api.timestamp += self.increment

        print("timestamp: ", self.api.timestamp)

        barset[symbol] = bars

        return barset
