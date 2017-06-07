__author__ = 'Devinderjeet'
import time
import datetime
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import numpy as np
import matplotlib
import matplotlib.cbook as cbook
from matplotlib.dates import bytespdate2num

from mpl_finance import candlestick_ohlc
matplotlib.rcParams.update({'font.size':19})


stockName=[]

def drawStockGraph(stock,date):
    try:
        #stockFile = 'C:/Zerodha/Pi/Exported/'+ stock
        stockFile = cbook.get_sample_data('C:/Zerodha/Pi/Exported/'+ stock , asfileobj=False)
        print('loading', stockFile)
        date, open, high , low, close, volume = np.loadtxt(stockFile,delimiter=',',
                                                          converters={0:bytespdate2num(date)},
                                                           skiprows=2,unpack=True)

        #bytespdate2num('%d-%b-%y')},skiprows=1, usecols=(0, 2), unpack=True
        #  mdates.strpdate2num('%d-%m-%Y %H:%M:%S')}
        fig = plt.figure()
        ax1 = plt.subplot(1,1,1)
        ax1.plot(date,close)
        plt.ylabel('Stock PRice')
        ax1.grid(True)
        plt.subplots_adjust(left=.17)

        plt.show()


    except Exception,e:
        print str(e)," error"

def forever():
        print "Hello"
        for eachStock in stockName:
            drawStockGraph(eachStock)
