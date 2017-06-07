import matplotlib.pyplot as plt
import matplotlib
import pymc3
import mpl_finance as finance
matplotlib.rcParams.update({'font.size':9})
#matplotlib.use('Qt4Agg')
import pandas as pd
import matplotlib.cbook as cbook




stocksName = 'PVR','RUSHIL','BPCL','RPOWER'
stockName = 'PVR'


def graphData(stock,guiDate):
    try:
        stockFile = cbook.get_sample_data('C:/Zerodha/Pi/Exported/'+ stock, asfileobj=False)
        print('loading', stockFile)
        data = pd.read_csv(stockFile,delimiter=',',usecols=(0,1,2,3,4,5),index_col='Date')

        print data

    except Exception,e:
        print str(e)


graphData('SBIN-EQ.csv','%d-%m-%Y %H:%M')
