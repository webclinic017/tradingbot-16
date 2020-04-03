import prices
import scraper
import alpaca_trade_api as tradeapi 

stocks = scraper.get_top_gainers()
print(prices.get_latest_prices(stocks))

#alpaca api
api = tradeapi.REST()

# api for placing paper trading
""" api.submit_order(
        symbol=stock,
        qty=1,
        side='sell',
        type='market',
        time_in_force='gtc'
    ) """

# For alpaca account information 
#account = api.get_account()

# For querying market data from alpaca
#barset = api.get_barset(symbol, 'day', limit=5)
# aapl_bars = barset[symbol]


