from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error
from math import sqrt
from all_func.stats.data_modeling import *
from statsmodels.tsa.arima_model import _arima_plot_predict
train_data_log=userDefined_Log_Data()
data = userDefined_Residual()


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
    model = ARIMA(train_data_log, order=(2, 1, 2))
    results_ARIMA = model.fit(disp=-1)
    ''''
    plt.plot(data)
    plt.plot(results_ARIMA.fittedvalues, color='red')
    plt.title('RSS: %.4f'% sum((results_ARIMA.fittedvalues-data)**2))
    plt.show()
    '''
    return results_ARIMA


results_AR = userDefined_ARModel()
predictions_ARIMA_diff = ARIMA.predict(results_AR.fittedvalues, copy=True)
print predictions_ARIMA_diff.head(10)