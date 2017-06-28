__author__ = 'Devinderjeet'
import warnings
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error
from func.eventdriven.data.HistoricalCSVDataHandler import HistoricalCSVDataHandler
'''
import pyximport
pyximport.install()

import sys
sys.path.append('data/')
from order1 import *
'''

def evaluate_arima_model(X, arima_order):
    # prepare training dataset
    #train_size = int(len(X) * 0.66)
    train_size = int(len(X)) -180

    train, test = X[0:train_size], X[train_size:]
    history = [x for x in train]
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

# evaluate combinations of p, d and q values for an ARIMA model
def evaluate_models(dataset, p_values, d_values, q_values):
    dataset = dataset.astype('float32')
    best_score, best_cfg = float("inf"), None
    for p in p_values:
        for d in d_values:
            for q in q_values:
                order = (p,d,q)
                try:
                    mse = evaluate_arima_model(dataset, order)
                    if mse < best_score:
                        best_score, best_cfg = mse, order
                    print('ARIMA%s MSE=%.3f' % (order,mse))
                except:
                    continue
    #print('Best ARIMA%s MSE=%.3f' % (best_cfg, best_score))
    print best_cfg
csv_dir = 'C:/Zerodha/Pi/Exported/'  # CHANGE THIS!
symbol_list = ['PVR-EQ']
a = HistoricalCSVDataHandler("ORDER",csv_dir,symbol_list)
stock =a._open_convert_csv_files()
# evaluate parameters
p_values = [0,1,2]
d_values = range(0, 3)
q_values = range(0, 3)
warnings.filterwarnings("ignore")
order=evaluate_models(stock['close'], p_values, d_values, q_values)
