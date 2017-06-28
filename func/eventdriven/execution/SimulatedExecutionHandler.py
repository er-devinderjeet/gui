from abc import ABCMeta, abstractmethod
import datetime
try:
    import Queue as queue
except ImportError:
    import queue

from func.eventdriven.events import FillEvent, OrderEvent

from func.eventdriven.data import HistoricalCSVDataHandler
from func.eventdriven.execution import ExecutionHandler

class SimulatedExecutionHandler(ExecutionHandler.ExecutionHandler):
    """
    The simulated execution handler simply converts all order
    objects into their equivalent fill objects automatically
    without latency, slippage or fill-ratio issues.

    This allows a straightforward "first go" test of any strategy,
    before implementation with a more sophisticated execution
    handler.
    """
    
    def __init__(self, events):
        """
        Initialises the handler, setting the event queues
        up internally.

        Parameters:
        events - The Queue of Event objects.
        """
        self.events = events

    def execute_order(self, event):
        """
        Simply converts Order objects into Fill objects naively,
        i.e. without any latency, slippage or fill ratio problems.

        Parameters:
        event - Contains an Event object with order information.
        """
        if event.type=='ORDER':
            csv_dir = 'C:/Zerodha/Pi/Exported/'  # CHANGE THIS!
            symbol_list = ['PVR-EQ','ICICIBANK-EQ']
            initial_capital = 100000.0
            #start date
            a = HistoricalCSVDataHandler.HistoricalCSVDataHandler("ORDER",csv_dir,symbol_list)
            start_date =a._read_csv_files()
            fill_event = FillEvent.FillEvent(
                start_date , event.symbol,
                'NSE', event.quantity, event.direction, None
            )
            print self.events.put(fill_event)
            self.events.put(fill_event)
'''
b =  ['12', 'BPCL', 'NSE', 100,'Long', 0.001, None]
a = SimulatedExecutionHandler(1)
a.execute_order(b)

csv_dir = 'C:/Zerodha/Pi/Exported/'  # CHANGE THIS!
symbol_list = ['BPCL-EQ']

class_obj_A = HistoricalCSV.HistoricalCSVDataHandler("ORDER",csv_dir,symbol_list)
start_date = class_obj_A._open_convert_csv_files()
print start_date
'''