__author__ = 'Devinderjeet'
import time
import datetime
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import numpy as np
import matplotlib
#from matplotlib.finance import candlestick_ohlc
import mpl_finance as finance
matplotlib.rcParams.update({'font.size':9})
#matplotlib.use('Qt4Agg')
import datetime as dt
import pandas as pd
import matplotlib.cbook as cbook
from matplotlib.dates import bytespdate2num
from ..stats import centralTendency
from rsi import *
import statsmodels.api as sm
from statsmodels import regression




stocksName = 'BHARTIARTL-EQ.csv','BPCL-EQ.csv'
stockName = 'PVR'

class graphing:
    def calculateCT(self,stock,guiDate):
        try:

            stockFile = cbook.get_sample_data('C:/Zerodha/Pi/Exported/'+ stock, asfileobj=False)
            print('loading', stockFile)
            date, openp, highp , lowp, closep, volume = np.loadtxt(stockFile,delimiter=',',skiprows=2,unpack=True,usecols=(0,1,2,3,4,5),
                                                          converters={0: bytespdate2num(guiDate)})



            self.ols()
            print centralTendency.artmeticMean(closep)


            #candlestickChart(stock,date,openp,highp,lowp,closep,volume)

        except Exception,e:
            print str(e)
    def ols(self):
        #stock, indice,stockDate,indiceDate
        try:
            indiceFile = cbook.get_sample_data('C:/Zerodha/Pi/Exported/NiftyIT.csv', asfileobj=False)

            print('loading', indiceFile)
            date_x, openp_x, highp_x , lowp_x, closep_x, volume_x = np.loadtxt(indiceFile,delimiter=',',skiprows=2,unpack=True,usecols=(0,1,2,3,4,5),
                                                          converters={0: bytespdate2num('%d-%m-%Y %H:%M:%S')})

            stockFile_b = cbook.get_sample_data('C:/Zerodha/Pi/Exported/HCLTECH-EQ.csv', asfileobj=False)
            print('loading', stockFile_b)
            date_y, openp_y, highp_y , lowp_y, closep_y, volume_y = np.loadtxt(stockFile_b,delimiter=',',skiprows=2,unpack=True,usecols=(0,1,2,3,4,5),
                                                          converters={0: bytespdate2num('%d-%m-%Y %H:%M')})


            alpha, beta = self.linreg(closep_x,closep_y)
            print 'alpha: ' + str(alpha)
            print 'beta: ' + str(beta)

            X2 = np.linspace(closep_x.min(), closep_x.max(), 20)
            Y_hat = X2 * beta + alpha

            plt.scatter(closep_x,closep_y, alpha=0.3)

            plt.ylabel("Stock PRice")
            plt.xlabel("Indice")
             # Add the regression line, colored in red
            plt.plot(X2, Y_hat, 'r', alpha=0.9);
            plt.show()

        except Exception,e:
            print str(e)

    def linreg(self,x,y):
        # We add a constant so that we can also fit an intercept (alpha) to the model
        # This just adds a column of 1s to our data
        x = sm.add_constant(x)
        model = regression.linear_model.OLS(y,x).fit()
        # Remove the constant now that we're done
        x = x[:, 1]
        return model.params[0], model.params[1]
        return model.summary()

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