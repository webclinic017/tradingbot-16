from trading_clients.Trader import Trader

class BackTrader(Trader):
    def get_account(self):
        return self.account
    
    def get_position(self, symbol):
        #needs to get position from a list of positions with index incremented at each tick
        return
    
    def submit_order(self, symbol, qty, side, type, time_in_force, 
        limit_price=None, stop_price=None, client_order_id=None, order_class=None, take_profit=None, stop_loss=None):
        #needs to log and close position
        return
    
    def get_barset(self, symbol,barTimeframe,limit=100):
        #needs to return {time, open, high, low, close, volume} as an object
        return

    def set_account(self, amount, data):
        Account = type('Account', (object,), {})
        obj = Account()
        obj.cash = amount
        self.account = obj
        self.data = data