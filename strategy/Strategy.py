""" 
This is the main file that runs our strategy. All strategy assets should be placed
in the strategy folder along with any helper files. 
Strategy files are the only files with access to indicators, prices, stock lists, etc.
It should not have any direct interactions with the brokerage api. Interactions are made via trading.py
"""

from abc import ABC, abstractmethod

class Strategy(ABC):
    def __init__(self, data, trader):
        self.data = data
        self.trader = trader
        super().__init__()
    
    @abstractmethod
    def run(self):
        pass
    
    @abstractmethod
    def update(self, new_data):
        pass

