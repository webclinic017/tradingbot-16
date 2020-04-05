""" Overview:
Server.py includes:
- Config options
- A Strategy object
- Initialization steps
- A loop

To-do:
- Add a universal logging object
"""
import trading_clients.AlpacaTrader as at
import strategy.SMAStrategy as smas
import alpaca_trade_api as tradeapi 
import time


trader = at.AlpacaTrader(tradeapi.REST())

strat = smas.Strategy(None, trader)

strat.run()

for i in range(0, 100000):
    strat.update()
    time.sleep(60)


