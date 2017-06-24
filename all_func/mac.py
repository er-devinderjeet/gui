import datetime
import numpy as np

from backtest import Backtest
from all_func.eventdriven.data.HistoricalCSVDataHandler import HistoricalCSVDataHandler
from all_func.eventdriven.events.SignalEvent import SignalEvent
from all_func.eventdriven.execution.SimulatedExecutionHandler import SimulatedExecutionHandler
from all_func.eventdriven.Portfolio import Portfolio
from all_func.eventdriven.strategy.Strategy import Strategy


class MovingAverageCrossStrategy(Strategy):
    """
    Carries out a basic Moving Average Crossover strategy with a
    short/long simple weighted moving average. Default short/long
    windows are 100/400 periods respectively.
    """

    def __init__(self, bars, events, short_window=10, long_window=40):
        """
        Initialises the buy and hold strategy.

        Parameters:
        bars - The DataHandler object that provides bar information
        events - The Event Queue object.
        short_window - The short moving average lookback.
        long_window - The long moving average lookback.
        """
        self.bars = bars
        self.symbol_list = self.bars.symbol_list
        self.events = events
        self.short_window = short_window
        self.long_window = long_window

        # Set to True if a symbol is in the market
        self.bought = self._calculate_initial_bought()

    def _calculate_initial_bought(self):
        """
        Adds keys to the bought dictionary for all symbols
        and sets them to 'OUT'.
        """
        bought = {}
        for s in self.symbol_list:
            bought[s] = 'OUT'
        return bought

    def calculate_signals(self, event):
        """
        Generates a new set of signals based on the MAC
        SMA with the short window crossing the long window
        meaning a long entry and vice versa for a short entry.    

        Parameters
        event - A MarketEvent object. 
        """
        if event.type == 'MARKET':
            for symbol in self.symbol_list:
                bars = self.bars.get_latest_bars_values(symbol, "close", N=self.long_window)               

                if bars is not None and bars != []:
                    short_sma = np.mean(bars[-self.short_window:])
                    long_sma = np.mean(bars[-self.long_window:])

                    dt = self.bars.get_latest_bar_datetime(symbol)
                    sig_dir = ""
                    strength = 1.0
                    strategy_id = 1

                    if short_sma > long_sma and self.bought[symbol] == "OUT":
                        sig_dir = 'LONG'
                        signal = SignalEvent(strategy_id, symbol, dt, sig_dir, strength)
                        self.events.put(signal)
                        self.bought[symbol] = 'LONG'

                    elif short_sma < long_sma and self.bought[symbol] == "LONG":
                        sig_dir = 'EXIT'
                        signal = SignalEvent(strategy_id, symbol, dt, sig_dir, strength)
                        self.events.put(signal)
                        self.bought[symbol] = 'OUT'


if __name__ == "__main__":
    csv_dir = 'C:/Zerodha/Pi/Exported/'  # CHANGE THIS!
    symbol_list = ['NCC']
    initial_capital = 10000.0
    #start date
    a = HistoricalCSVDataHandler("ORDER",csv_dir,symbol_list)
    start_date =a._open_convert_csv_files()
    print start_date
    heartbeat = 0.0

    backtest = Backtest.Backtest(csv_dir,
                        symbol_list, 
                        initial_capital, 
                        heartbeat,
                        start_date,
                        HistoricalCSVDataHandler,
                        SimulatedExecutionHandler, 
                        Portfolio, 
                        MovingAverageCrossStrategy)
    
    backtest.simulate_trading()
