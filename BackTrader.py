
import datetime  # For datetime objects
import os.path  # To manage paths
import sys  # To find out the script name (in argv[0])
import backtrader as bt
from backtesting_strategy.ExampleStrat import TestStrategy

cerebro = bt.Cerebro()
cerebro.addstrategy(TestStrategy)

modpath = os.path.dirname(os.path.abspath(sys.argv[0]))
datapath = 'FB.csv'

# Create a Data Feed
data = bt.feeds.YahooFinanceCSVData(
    dataname=datapath,
    fromdate=datetime.datetime(2017, 1, 1),
    todate=datetime.datetime(2017, 12, 31),
    reverse=False)

    # Add the Data Feed to Cerebro
cerebro.adddata(data)

# Set our desired cash start
cerebro.broker.setcash(100000.0)

# Add a FixedSize sizer according to the stake
cerebro.addsizer(bt.sizers.FixedSize, stake=10)

# Set the commission
cerebro.broker.setcommission(commission=0.000)


print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
cerebro.run()
print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
cerebro.plot()