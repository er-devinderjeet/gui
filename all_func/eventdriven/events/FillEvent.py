__author__ = 'Devinderjeet'
from all_func.eventdriven.events import Event

class FillEvent(Event.Event):
    """
    Encapsulates the notion of a Filled Order, as returned
    from a brokerage. Stores the quantity of an instrument
    actually filled and at what price. In addition, stores
    the commission of the trade from the brokerage.
    """
    def __init__(self, timeindex, symbol, exchange, quantity,
                 direction, fill_cost, commission=None):
        """
        Initialises the FillEvent object. Sets the symbol, exchange,
        quantity, direction, cost of fill and an optional
        commission.
        If commission is not provided, the Fill object will
        calculate it based on the trade size and Interactive
        Brokers fees.
        Parameters:
        timeindex - The bar-resolution when the order was filled.
        symbol - The instrument which was filled.
        exchange - The exchange where the order was filled.
        quantity - The filled quantity.
        direction - The direction of fill (BUY or SELL)
        fill_cost - The holdings value in dollars.
        commission - An optional commission sent from IB.
        """
        self.type = 'FILL'
        self.timeindex = timeindex
        self.symbol = symbol
        self.exchange = exchange
        self.quantity = quantity
        self.direction = direction
        self.fill_cost = fill_cost

        # Calculate commission
        if commission is None:
            #self.commission = self.calculate_commission(2000)
            self.commission = self.calculate_commission(10000.0)
        else:
            self.commission = commission


    def calculate_commission(self, trading_value):
        """
        Calculates the fees of trading based on an Interactive
        Brokers fee structure for API, in USD.
        This does not include exchange or ECN fees.
        Based on "US API Directed Orders":
        https://www.interactivebrokers.com/en/index.php?
        f=commission&p=stocks2
        """
        full_cost  = 0.001
        if trading_value <= 20000:
            full_cost =  (0.001 * trading_value)
        else:
            full_cost = 20.0

        return full_cost
'''
a = FillEvent("12","BPCL","NSE",100,"BUY",0.001)
#print a.commission

'''