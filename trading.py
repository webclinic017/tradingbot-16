"""
This should be a wrapper class for our interactions with the brokerage.
For example, we write our own generic submit_order function that works more universally
rather than using alpaca_api.submit_order
"""

class Trader:
    def __init__(self, api):
        self.api = api
    
    def get_account(self):
        return api.get_account()
    
    def get_position(self, symbol):
        return api.get_position(symbol)
    
    def submit_order(self, symbol, qty, side, type, time_in_force, 
        limit_price=None, stop_price=None, client_order_id=None, order_class=None, take_profit=None, stop_loss=None):
        return api.submit_order(symbol, qty, side, type, time_in_force, limit_price, stop_price, client_order_id, order_class, take_profit, stop_loss)