# tradingbot

`python server.py`

Development branch for working on the custom backtrader client.


Idea:

- Each point in time is a tick
- Tick has data associated with it - market price, open, high, low, close, volume, etc.
- Backtrader.get_barset returns bars with each tick's data
- The bars are created from a data file (probably a CSV from an API like Yahoo Finance)
- Methods like submit_order are logged internally
- Every call to Strategy.update should ideally be requesting a new bar set. We can simulate time passing by incrementing the Backtrader's internal clock. We can pass in a parameter to specify this increment.