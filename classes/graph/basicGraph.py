__author__ = 'Devinderjeet'
import time
import datetime
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import numpy as np
import matplotlib
from mpl_finance import candlestick_ohlc
matplotlib.rcParams.update({'font.size':19})


stockName='PVR','RUSHIL'

def drawStockGraph(stock):
    try:
        stockFile = 'stock/1_year/'+ stock +'.txt'
        date, close, high , low, open, volume = np.loadtxt(stockFile,delimiter=',', unpack=True,
                                                            converters={0: mdates.strpdate2num('%Y%m%d')})


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
