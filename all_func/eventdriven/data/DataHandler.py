
__author__ = 'Devinderjeet'
from abc import ABCMeta, abstractmethod

import numpy as np
import matplotlib.cbook as cbook
from matplotlib.dates import bytespdate2num
__metaclass__ = ABCMeta

class DataHandler(object):
    def user_Defined_CSV(self):
            try:
                indiceFile = cbook.get_sample_data('C:/Zerodha/Pi/Exported/Nifty 50.csv', asfileobj=False)

                print('loading', indiceFile)
                date_x, openp_x, highp_x , lowp_x, closep_x, volume_x = np.loadtxt(indiceFile,delimiter=',',skiprows=2,unpack=True,usecols=(0,1,2,3,4,5),
                                                              converters={0: bytespdate2num('%d-%m-%Y %H:%M')})

                stockFile_b = cbook.get_sample_data('C:/Zerodha/Pi/Exported/BPCL-EQ.csv', asfileobj=False)
                print('loading', stockFile_b)
                date_y, openp_y, highp_y , lowp_y, closep_y, volume_y = np.loadtxt(stockFile_b,delimiter=',',skiprows=2,unpack=True,usecols=(0,1,2,3,4,5),
                                                              converters={0: bytespdate2num('%d-%m-%Y %H:%M')})
                return date_y,closep_x,closep_y,volume_x,volume_y

            except Exception,e:
                print str(e)

    def user_Defined_Historical_Data(self):
        pass
    def user_Defined_Live_Data(self):
        pass

    @abstractmethod
    def get_latest_bar(self, symbol):
        """
        Returns the last bar updated.
        """
        raise NotImplementedError("Should implement get_latest_bar()")

    @abstractmethod
    def get_latest_bars(self, symbol, N=1):
        """
        Returns the last N bars updated.
        """
        raise NotImplementedError("Should implement get_latest_bars()")
    @abstractmethod
    def get_latest_bar_datetime(self, symbol):
        """
        Returns a Python datetime object for the last bar.
        """
        raise NotImplementedError("Should implement get_latest_bar_datetime()")
    @abstractmethod
    def get_latest_bar_value(self, symbol, val_type):
        """
        Returns one of the Open, High, Low, Close, Volume or OI
        from the last bar.
        """
        raise NotImplementedError("Should implement get_latest_bar_value()")
    @abstractmethod
    def get_latest_bars_values(self, symbol, val_type, N=1):
        """
        Returns the last N bar values from the
        latest_symbol list, or N-k if less available.
        """
        raise NotImplementedError("Should implement get_latest_bars_values()")

    @abstractmethod
    def update_bars(self):
        """
        Pushes the latest bars to the bars_queue for each symbol
        in a tuple OHLCVI format: (datetime, open, high, low,
        close, volume, open interest).
        """
        raise NotImplementedError("Should implement update_bars()")
