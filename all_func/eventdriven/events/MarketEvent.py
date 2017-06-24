__author__ = 'Devinderjeet'
from all_func.eventdriven.events import Event
class MarketEvent(Event.Event):
    """
    Handles the event of receiving a new market update with
    corresponding bars.
    """
    def __init__(self):
        """
        Initialises the MarketEvent.
        """
        self.type = 'MARKET'

