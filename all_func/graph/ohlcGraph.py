__author__ = 'Devinderjeet'
import time
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import numpy as np
import matplotlib
import mpl_finance as finance
matplotlib.rcParams.update({'font.size':9})
import pandas as pd
import matplotlib.cbook as cbook
from matplotlib.dates import bytespdate2num
from ..userstats import centralTendency
from rsi import *
import statsmodels.api as sm
from statsmodels import regression
from scipy import stats
from statsmodels.sandbox.regression.predstd import wls_prediction_std



stocksName = 'BHARTIARTL-EQ.csv','BPCL-EQ.csv'
stockName = 'PVR'

class graphing:
    def calculateCT(self,stock,guiDate):
        try:
            stockFile = cbook.get_sample_data('C:/Zerodha/Pi/Exported/'+ stock, asfileobj=False)
            print('loading', stockFile)
            date, openp, highp , lowp, closep, volume = np.loadtxt(stockFile,delimiter=',',skiprows=2,unpack=True,usecols=(0,1,2,3,4,5),
                                                          converters={0: bytespdate2num(guiDate)})


            print centralTendency.artmeticMean(closep)


            self.candlestickChart(stock,date,openp,highp,lowp,closep,volume)

        except Exception,e:
            print str(e)


    def candlestickChart(self, stock,date,openp,highp,lowp,closep,volume):
            x = 0
            y = len(date)
            candleAr = []
            while x < y:
                appendLine = date[x],openp[x],highp[x],lowp[x],closep[x],volume[x]
                candleAr.append(appendLine)
                x+=1
            fig = plt.figure(figsize=(12,6))
            ax1 = plt.subplot2grid((6,4),(0,0),rowspan =4, colspan=4) #(2,3,1)
            finance.candlestick_ohlc(ax1, candleAr, width=0.2,colorup='b', colordown='r', alpha=0)

            plt.ylabel('Stock Price')
            ax1.grid(True)

            ax2 = plt.subplot2grid((6,4),(5,0), rowspan =1, colspan=4,  sharex = ax1)
            ax2.bar(date, volume)
            ax2.grid(True)
            plt.ylabel('Volume')
            ax2.axes.yaxis.set_ticklabels([])
            ax2.xaxis.set_major_locator(mticker.MaxNLocator(10))
            ax2.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))

            ax3 = plt.subplot2grid((6,4), (4,0), sharex=ax1, rowspan=1, colspan=4)
            rsi = rsiFunc(closep)
            rsiCol = 'k'
            posCol = '#386d13'
            negCol = '#8f2020'

            ax3.plot(date, rsi, rsiCol, linewidth=1.5)
            ax3.axhline(70, color=negCol)
            ax3.axhline(30, color=posCol)
            ax3.fill_between(date, rsi, 70, where=(rsi>=70), facecolor=negCol, edgecolor=negCol)
            ax3.fill_between(date, rsi, 30, where=(rsi<=30), facecolor=posCol, edgecolor=posCol)
            ax3.set_yticks([30,70])
            ax3.yaxis.label.set_color("b")
            ax3.spines['bottom'].set_color("#5998ff")
            ax3.spines['top'].set_color("#5998ff")
            ax3.spines['left'].set_color("#5998ff")
            ax3.spines['right'].set_color("#5998ff")
            ax3.tick_params(axis='y', colors='b')
            plt.ylabel('RSI')

            for label in ax2.xaxis.get_ticklabels():
                label.set_rotation(45)

            plt.subplots_adjust(left=.15, bottom=.19, right=.93, top=.94, wspace=.20,hspace=0.00)
            plt.xlabel('Date')
            plt.suptitle(stock+ ' Stock Price')
            plt.setp(ax1.get_xticklabels(), visible=False)
            plt.setp(ax2.get_yticklabels(), visible=False)

            plt.show()





def forever():
    print "Hello"
    while True:
        for eachStock in stocksName:
            child = graphing()

            child.calculateCT(eachStock,'%d-%m-%Y %H:%M')
            time.sleep(10)
def exitGraphing():
    import sys
    sys.exit("Error message")