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

strats = [smas.Strategy(None, trader)]

for strat in strats:
    strat.run()

for i in range(0, 100000):
    for strat in strats:
        strat.update()
    time.sleep(60)


