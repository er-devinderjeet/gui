__author__ = 'Devinderjeet'
from statsmodels.tsa.stattools import acf,pacf
import numpy as np
import matplotlib.cbook as cbook
from matplotlib.dates import bytespdate2num
import matplotlib.pyplot as plt
from statsmodels.tsa.ar_model import AR

def calAcf(stock,guiDate):
    stockFile = cbook.get_sample_data('C:/Zerodha/Pi/Exported/'+ stock, asfileobj=False)
    print('loading', stockFile)
    date, openp, highp , lowp, closep, volume = np.loadtxt(stockFile,delimiter=',',skiprows=2,unpack=True,usecols=(0,1,2,3,4,5),
                                                  converters={0: bytespdate2num(guiDate)})

    closep_acf= acf(closep,unbiased=True,nlags=40)
    closep_pacf= pacf(closep,nlags=40)
    closep_ar = AR(20)


    #draw
    plt.plot(closep_ar,'ro')
    plt.xlabel('Lag')
    plt.ylabel('Close PRice ACF ')
    plt.show()

calAcf('BPCL-EQ.csv','%d-%m-%Y %H:%M')