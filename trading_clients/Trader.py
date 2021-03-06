"""
This should be a wrapper class for our interactions with the brokerage.
For example, we write our own generic submit_order function that works more universally
rather than using alpaca_api.submit_order
"""
from abc import ABC, abstractmethod

class Trader(ABC):
    def __init__(self, api):
        self.api = api
        super().__init__()
    
    @abstractmethod
    def get_account(self):
        pass
    
    @abstractmethod
    def get_position(self, symbol):
        pass
    
    @abstractmethod
    def submit_order(self, symbol, qty, side, type, time_in_force, 
        limit_price=None, stop_price=None, client_order_id=None, order_class=None, take_profit=None, stop_loss=None, close_price=None):
        pass