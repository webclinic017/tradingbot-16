
# Tradingbot

## Usage
1. Make sure you have a file called .env which looks something like

```

export APCA_API_BASE_URL = "https://paper-api.alpaca.markets"

export APCA_API_KEY_ID = "PKKCZWUTJYNM5NEZSJOO"

export APCA_API_SECRET_KEY = "R30t8uWklbVBc1i8PM4rASnnBwVqsmqnxAG7mYDS"


```

2. Run `python3 server.py` with any of the following options. Here is the `-h` output.  
```
usage: server.py [-h] [-b [BACKTEST]] [-p] [-l]

optional arguments:
  -h, --help            show this help message and exit
  -b [BACKTEST], --backtest [BACKTEST]
                        Provide cash, timestamp, start_date, output_file to
                        backtest the assigned strategies. Uses default values
                        if not assigned.
  -p, --paper           Run bot in paper trading mode. Make sure to add API
                        keys to env.
  -l, --live            Run bot in live trading mode. Make sure to add API
                        keys to env.

```