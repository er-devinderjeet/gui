from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.arima_model import ARMA

from sklearn.metrics import mean_squared_error
from math import sqrt
from all_func.stats.data_modeling import *
from statsmodels.tsa.arima_model import _arima_plot_predict
train_data_log=userDefined_Log_Data()
data = userDefined_Residual()
import pandas as pd
import all_func.stats.data_modeling
import itertools


data=userDefined_Log_Shift()
def userDefined_ARModel():
    model = ARIMA(train_data_log, order=(2, 1, 0))
    results_AR = model.fit(disp=-1)
    ''''
    plt.plot(data)
    plt.plot(results_AR.fittedvalues, color='red')
    plt.title('RSS: %.4f'% sum((results_AR.fittedvalues-train_data_log)**2))

    plt.show()
    '''
    return results_AR

def userDefined_MAModel():
    model = ARIMA(train_data_log, order=(0, 1, 2))
    results_MA = model.fit(disp=-1)
    plt.plot(data)
    plt.plot(results_MA.fittedvalues, color='red')
    plt.title('RSS: %.4f'% sum((results_MA.fittedvalues-data)**2))
    plt.show()

def userDefined_ARIMAModel():
    model = ARIMA(data, order=(2, 1, 2))
    results_ARIMA = model.fit(disp=-1)
    ''''
    plt.plot(data)
    plt.plot(results_ARIMA.fittedvalues, color='red')
    plt.title('RSS: %.4f'% sum((results_ARIMA.fittedvalues-data)**2))
    plt.show()
    '''
    return results_ARIMA


results_ARIMA = userDefined_ARIMAModel()
'''
predictions_ARIMA_diff = pd.Series(results_ARIMA.fittedvalues, copy=True)
print predictions_ARIMA_diff.head()

predictions_ARIMA_diff_cumsum = predictions_ARIMA_diff.cumsum()
print predictions_ARIMA_diff_cumsum.head()
predictions_ARIMA_log = pd.Series(train_data_log.ix[100], index=train_data_log.index)
predictions_ARIMA_log = predictions_ARIMA_log.add(predictions_ARIMA_diff_cumsum,fill_value=0)
print predictions_ARIMA_log.tail()

predictions_ARIMA = np.exp(predictions_ARIMA_log)
plt.plot(predictions_ARIMA)
plt.title('RMSE: %.4f'% np.sqrt(sum((predictions_ARIMA-train_data_log)**2)/len(train_data_log)))
plt.show()
'''
forecast=results_ARIMA.forecast(10, exog=None, alpha=0.05)[0]
history = [x for x in data]


minute = 2
minute_in_day = 10
def invert_graph(values,forecast_vaules,period=1):
    return values + forecast_vaules[-period]

for yhats in forecast:
    invert_graph(history,forecast,minute_in_day)
    history.append(yhats)
    minute +=2