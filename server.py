""" Overview:
server.py includes:
- Command line options
- A list of strategies to run on separate threads
- A strategy execution function

To-do:
- Add a thread pool/queue
- Better logging
"""


import argparse
import time
import dotenv
import os
import sys
import threading

import alpaca_trade_api as tradeapi

import trading_clients.AlpacaTrader as at
import trading_clients.Backtrader as bt
import strategy.SMAStrategy as smas


def execute_strategy(strategy, data, timer):
    """This function is the target for threading.Thread. It runs the given strategy and updates it in a loop for some long period of time.

    Arguments:
        strategy {Strategy} -- The Strategy object to be executed on this thread.
        data {object} -- The data object that the Strategy can choose to be initialized with.
        timer {int} -- The number of seconds of time.sleep between each iteration.
    """
    strategy.run()
    for _ in range(0, 100000):
        strategy.update(data)
        time.sleep(timer)


def main():
    """Entry point for the program. It accepts command line arguments and creates the threads to run each strategy.
    """
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-b", "--backtest", help="Provide cash, timestamp, start_date, output_file to backtest the assigned strategies. Uses default values if not assigned.", nargs="+")
    parser.add_argument(
        "-p", "--paper", help="Run bot in paper trading mode. Make sure to add API keys to env.", action='store_true')
    parser.add_argument(
        "-l", "--live", help="Run bot in live trading mode. Make sure to add API keys to env.", action='store_true')

    args = parser.parse_args()

    trader = None

    if args.backtest:
        class Object(object):
            pass
        data = Object()
        try:
            data.cash = float(args.backtest[0])
        except:
            data.cash = 10000

        try:
            data.timestamp = int(args.backtest[1])
        except:
            data.timestamp = 100

        try:
            data.start_date = args.backtest[2]
        except:
            data.start_date = "2017-01-01"

        try:
            data.output_file = args.backtest[3]
        except:
            data.output_file = "output.csv"

        trader = bt.Backtrader(data)

    elif args.paper:
        if os.path.isfile(".env"):
            dotenv.load_dotenv()
        else:
            print("Error: Create a .env file containing API keys")
            sys.exit()

        trader = at.AlpacaTrader(tradeapi.REST())

    strats = [smas.SMAStrategy(None, trader)]

    for i, strat in enumerate(strats):
        try:
            t = threading.Thread(target=execute_strategy,
                                 kwargs=dict(strategy=strat, data=None, timer=1))
            t.start()
        except:
            print("Error: unable to start thread: ", i)


if __name__ == "__main__":
    main()
