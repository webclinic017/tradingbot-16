from trading_clients.Trader import Trader

class Backtrader(Trader):
    # List of orders placed
    log = []

    # add more member variables to keep track of more things
    timestamp = 0
    increment = 1

    def get_account(self):
        class Object(object):
            pass
        act = Object()
        act.cash = 10000

        return act
    

    def get_position(self, symbol):
        #This function would normally throw an exception if position not found
        return None
    
    def submit_order(self, symbol, qty, side, type, time_in_force, 
        limit_price=None, stop_price=None, client_order_id=None, order_class=None, take_profit=None, stop_loss=None):
        #This function would normally return an Order object

        params = [symbol, qty, side, type, time_in_force, limit_price, stop_price, client_order_id, order_class, take_profit, stop_loss]
        orders_dict = dict.fromkeys(params, 1)

        self.log.append(orders_dict)
        
        return True
    
    def get_barset(self, symbol, barTimeframe,limit=100):
        barset = {}

        # Fill barset

        # Increment time

        self.timestamp += self.increment
        return barset
