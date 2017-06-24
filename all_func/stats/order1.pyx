__author__ = 'Devinderjeet'
import warnings
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error
from all_func.eventdriven.data.HistoricalCSVDataHandler import HistoricalCSVDataHandler

def evaluate_arima_model(double X, int arima_order):
    # prepare training dataset
    #train_size = int(len(X) * 0.66)
    cdef double error =0
    cdef int train_size = int(len(X)) -180

    cdef int train  = X[0:train_size],
    cdef int test = X[train_size:]
    cdef int history = [x for x in train]
    # make predictions
    predictions = list()
    for t in range(len(test)):
        model = ARIMA(history, order=arima_order)
        model_fit = model.fit(disp=0)
        yhat = model_fit.forecast()[0]
        predictions.append(yhat)
        history.append(test[t])
    # calculate out of sample error
    error = mean_squared_error(test, predictions)
    return error

