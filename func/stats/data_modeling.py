__author__ = 'Devinderjeet'
__author__ = 'Devinderjeet'

import warnings
from matplotlib import pyplot
import numpy as np
from func.eventdriven.data.HistoricalCSVDataHandler import HistoricalCSVDataHandler
from func.stats.stationarity import *
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import acf, pacf
import pandas as pd

'''
def predict(coef, history):
	yhat = 0.0
	for i in range(1, len(coef)+1):
		yhat += coef[i-1] * history[-i]
	return yhat

def difference(dataset):
	diff = list()
	for i in range(1, len(dataset)):
		value = dataset[i] - dataset[i - 1]
		diff.append(value)
	return numpy.array(diff)


'''''
csv_dir = 'C:/Zerodha/Pi/Exported/'  # CHANGE THIS!
symbol_list = ['PVR-EQ']
a = HistoricalCSVDataHandler("ORDER", csv_dir, symbol_list)
stock = a._open_convert_csv_files()

warnings.filterwarnings("ignore")


# moving-average on train data(log)
#  window-size of 20
def moving_average(data):
	moving_average = pd.Series(data).rolling(window=20).mean()
	'''
	plt.plot(data)
	plt.plot(moving_average, color='red')
	plt.show()
	'''
	return moving_average

X = stock['close']
def userDefined_Log_Data():

	train_size = len(X) - 180
	train_data, test_data = X[0:train_size], X[train_size:]
	# rolmean = pd.Series(train_data).rolling(window=20).mean()
	# rolstd = pd.Series(train_data).rolling(window=20).std()

	#train_stationarity(train_data)

	train_data_log = np.log(train_data)
	'''
	print train_data.tail()
	plt.plot(train_data_log)
	plt.show()
	'''
	return train_data_log

#Test Stationary with moving-Average
def userdefined_moving_average():

	train_data_log = userDefined_Log_Data()
	#Train data moving average
	moving_avg = moving_average(train_data_log)
	'''
    #print moving_avg.tail()
    plotting(train_data, rolmean,rolstd)
    plt.plot(train_data_log)
    plt.plot(moving_avg, color='red')
    plt.show()
    '''
	train_data_log_moving_avg_diff = train_data_log - moving_avg
	'''
	print train_data_log_moving_avg_diff.head()
	print train_data_log_moving_avg_diff.tail()
	plt.subplot(2,1,1)
	plt.plot(train_data_log)
	plt.plot(moving_avg, color='red')
	plt.subplot(2,1,2)
	plt.plot(train_data_log_moving_avg_diff)
	plt.show()
	'''
	#Remove NaN from train_data_log_moving_avg_diff.head() headS
	train_data_log_moving_avg_diff = train_data_log_moving_avg_diff.dropna()
	'''
	#mean and train_data_log_moving_avg_diff start after 20 steps
	plt.subplot(2,1,1)
	plt.plot(train_data_log)
	plt.plot(moving_avg, color='red')
	plt.subplot(2,1,2)
	plt.plot(train_data_log_moving_avg_diff)
	plt.show()
	'''
	#test_stationarity_2(train_data_log_moving_avg_diff)
	#return Difference of train data log and  moving average
	return train_data_log_moving_avg_diff

#Test Stationary with log
#playing with log
def userDefined_Log_Shift():
	train_data_log =userDefined_Log_Data()

	train_data_log_shift = train_data_log.shift()

	#print train_data_log_shift.head(),train_data_log.head()

	train_data_log_diff = train_data_log - train_data_log_shift
	'''
	print train_data_log_diff
	print train_data_log_diff.head()
	plt.subplot(2,1,1)
	plt.plot(train_data_log)
	plt.plot(train_data_log_shift, color='red')
	plt.subplot(2,1,2)
	plt.plot(train_data_log_diff)
	plt.show()
	'''
	#train_data_log = train_data_log_diff.dropna(inplace=True)
	train_data_log_diff = train_data_log_diff.dropna()
	test_stationarity_2(train_data_log_diff)
	return train_data_log_diff

#userDefined_Log_Shift()
#userdefined_moving_average()
def userDefined_Residual():
	train_data_log = userDefined_Log_Data()
	decomposition = seasonal_decompose(train_data_log, model='additive', filt=None, freq=10)
	trend = decomposition.trend
	seasonal = decomposition.seasonal
	residual = decomposition.resid
	'''
	plt.subplot(411)
	plt.plot(train_data_log, label='Original')
	plt.legend(loc='best')
	plt.subplot(412)
	plt.plot(trend, label='Trend')
	plt.legend(loc='best')
	plt.subplot(413)
	plt.plot(seasonal,label='Seasonality')
	plt.legend(loc='best')
	plt.subplot(414)
	plt.plot(residual, label='Residuals')
	plt.legend(loc='best')
	plt.tight_layout()
	plt.show()
	'''''
	train_data_log_decompose = residual
	train_data_log_decompose = train_data_log_decompose.dropna()
	'''

	print train_data_log_decompose

	plt.subplot(2,1,1)
	plt.plot(train_data_log)
	plt.subplot(2,1,2)
	plt.plot(train_data_log_decompose)
	plt.show()
	'''
	#test_stationarity_2(train_data_log_decompose)
	return train_data_log_decompose


'''
a=userdefined_moving_average()
b=userDefined_Log_Shift()
c=userDefined_Residual()
'''
def acf_N_pacf():
	data=userdefined_moving_average()

	lag_acf = acf(data, nlags=40)
	lag_pacf = pacf(data, nlags=40, method='ols') #, method='ols'
	'''
	plt.subplot(121)
	plt.plot(lag_acf)
	plt.axhline(y=0,linestyle='--',color='gray')
	plt.axhline(y=-1.96/np.sqrt(len(data)),linestyle='--',color='gray')
	plt.axhline(y=1.96/np.sqrt(len(data)),linestyle='--',color='gray')
	plt.title('Autocorrelation Function')
	#pacf graph
	plt.subplot(122)
	plt.plot(lag_pacf)
	plt.axhline(y=0,linestyle='--',color='gray')
	plt.axhline(y=-1.96/np.sqrt(len(data)),linestyle='--',color='gray')
	plt.axhline(y=1.96/np.sqrt(len(data)),linestyle='--',color='gray')
	plt.title('Partial Autocorrelation Function')
	plt.tight_layout()

	plt.show()
	'''


#acf_N_pacf()