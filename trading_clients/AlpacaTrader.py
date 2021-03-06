from trading_clients.Trader import Trader

class AlpacaTrader(Trader):
    def get_account(self):
        return self.api.get_account()
    
    def get_position(self, symbol):
        return self.api.get_position(symbol)
    
    def submit_order(self, symbol, qty, side, type, time_in_force, 
        limit_price=None, stop_price=None, client_order_id=None, order_class=None, take_profit=None, stop_loss=None, close_price=None):
        return self.api.submit_order(symbol, qty, side, type, time_in_force)
    
    def get_barset(self, symbol,barTimeframe,limit=100):
        return self.api.get_barset(symbol,barTimeframe,limit=100)