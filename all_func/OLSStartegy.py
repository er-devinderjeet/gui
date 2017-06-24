__author__ = 'Devinderjeet'
import datetime
import numpy as np

from backtest import Backtest
from all_func.eventdriven.data.HistoricalCSVDataHandler import HistoricalCSVDataHandler
from all_func.eventdriven.events.SignalEvent import SignalEvent
from all_func.eventdriven.execution.SimulatedExecutionHandler import SimulatedExecutionHandler
from all_func.eventdriven.Portfolio import Portfolio
from all_func.eventdriven.strategy.Strategy import Strategy
from all_func.graph.charting import *
class OLSStrategy(Strategy):
        def __init__(self, bars, events, long_window_size=50,short_window_size=5,
        zscore_high=3.0,zscore_center=0.5, zscore_bhnc=1.5,outlinear=3.1):
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
            self.long_window_size = long_window_size

            # Set to True if a symbol is in the market
            #self.bought = self._calculate_initial_bought()
            self.short_ols_window = short_window_size

            self.zscore_high = zscore_high
            self.zscore_center = zscore_center
            self.zscore_high = zscore_high
            #zscore bhnc = Between High aNd Center
            self.zscore_bhnc = zscore_bhnc

            self.stock = ['PVR-EQ','Nifty50']
            self.stock_purchase = False
            self.outlinear = outlinear
        def calculate_Stock_Signals(self, zscore_last):
            """
            Calculates the actual x, y signal pairings
            to be sent to the signal generator.

            Parameters
            zscore_last - The current zscore to test against
            """
            y_signal = None
            x_signal = None
            p0 = self.stock[0]
            p1 = self.stock[1]
            dt = datetime.datetime.now()
            #hr = abs(self.hedge_ratio)

            # If we're long the market and below the
            # negative of the high zscore threshold
            if zscore_last <= -self.zscore_high and not self.stock_purchase:
                self.stock_purchase = True
                y_signal = SignalEvent(1, p0, dt, 'LONG', 1.0)
                #x_signal = SignalEvent(1, p1, dt, 'SHORT', hr)

            # If we're long the market and between the
            # absolute value of the low zscore threshold
            if abs(zscore_last) == self.zscore_center and self.stock_purchase:
                self.stock_purchase = False
                y_signal = SignalEvent(1, p0, dt, 'TARGET_1', 1.0)

            if abs(zscore_last) == self.zscore_bhnc and self.stock_purchase:
                self.stock_purchase = False
                y_signal = SignalEvent(1, p0, dt, 'TARGET_2', 1.0)

            if abs(zscore_last) == self.zscore_high and self.stock_purchase:
                self.stock_purchase = False
                y_signal = SignalEvent(1, p0, dt, 'TARGET_3', 1.0)

            if abs(zscore_last) == -self.outlinear and self.stock_purchase:
                self.stock_purchase = False
                y_signal = SignalEvent(1, p0, dt, 'STOPLOSS', 1.0)

            ''''
                #x_signal = SignalEvent(1, p1, dt, 'EXIT', 1.0)

            # If we're short the market and above
            # the high zscore threshold

            if zscore_last >= self.zscore_high and not self.short_market:
                self.short_market = True
                y_signal = SignalEvent(1, p0, dt, 'SHORT', 1.0)
                x_signal = SignalEvent(1, p1, dt, 'LONG', hr)

             If we're short the market and between the
             absolute value of the low zscore threshold
            if abs(zscore_last) <= self.zscore_low and self.short_market:
                self.short_market = False
                y_signal = SignalEvent(1, p0, dt, 'EXIT', 1.0)
                #x_signal = SignalEvent(1, p1, dt, 'EXIT', 1.0)

            #return y_signal, x_signal
            '''
            return y_signal




        def calculate_OLS_signals(self):

            y = self.bars.get_latest_bars_values(
            self.stock[0], "close", N=self.long_window_size
            )

            x = self.bars.get_latest_bars_values(
                self.stock[1], "close", N=self.long_window_size
            )
            '''
            data_y=self.stock[0]
            data_x = self.stock[1]
            '''
            if y is not None and x is not None:
                # Check that all window periods are available
                if len(y) >= self.long_window_size and len(x) >= self.long_window_size:
                    # Calculate the current hedge ratio using  OLS
                    self.beta = sm.OLS(y, x).fit().params[0]

                    # Calculate the current z-score of the residuals
                    spread = y - self.beta * x
                    zscore_last = ((spread - spread.mean())/spread.std())[-1]

                    # Calculate signals and add to events queue
                    y_signal = self.calculate_Stock_Signals(zscore_last)
                    if y_signal is not None:
                        self.events.put(y_signal)



        def calculate_signals(self, event):
                """
                Calculate the SignalEvents based on market data.
                """
                if event.type == 'MARKET':
                    self.calculate_OLS_signals()


if __name__ == "__main__":
    csv_dir = 'C:/Zerodha/Pi/Exported/'  # CHANGE THIS!
    symbol_list = ['PVR-EQ','Nifty50']
    initial_capital = 10000.0
    heartbeat = 0.0
    a = HistoricalCSVDataHandler("ORDER",csv_dir,symbol_list)
    start_date =a._read_csv_files()
    print start_date
    backtest = Backtest.Backtest(
        csv_dir, symbol_list, initial_capital, heartbeat,
        start_date, HistoricalCSVDataHandler, SimulatedExecutionHandler,
        Portfolio, OLSStrategy
    )
    backtest.simulate_trading()
