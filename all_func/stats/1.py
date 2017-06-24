__author__ = 'Devinderjeet'

#testing_log

moving_avg =pd.Series(testing_log).rolling(window=20).mean()
#pd.rolling_mean(ts_log,12)
plt.plot(testing_log)
plt.plot(moving_avg, color='red')
plt.show()
#moving_avg
testing_log_moving_avg_diff = testing_log - moving_avg
print testing_log_moving_avg_diff.tail()

testing_log_moving_avg_diff.dropna(inplace=True)
test_stationarity_2(testing_log_moving_avg_diff)

testing_log_diff = testing_log - testing_log.shift()
plt.plot(testing_log_diff)
#testing_log_diff
plt.show()

testing_log_diff.dropna(inplace=True)
test_stationarity_2(testing_log_diff)


decomposition = seasonal_decompose(testing_log, model='additive', filt=None, freq=10)

trend = decomposition.trend
seasonal = decomposition.seasonal
residual = decomposition.resid

plt.subplot(411)
plt.plot(testing_log, label='Original')
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

testing_log_decompose = residual
testing_log_decompose.dropna(inplace=True)
test_stationarity_2(testing_log_decompose)


'''
size = len(X) - 180
train, test = X[0:size], X[size:]

history = [x for x in train]
predictions = list()
for t in range(len(test)):
	model = ARIMA(history, order=(len(test),0,len(test)))
	#model_fit = model.fit(trend='nc', disp=False)
	#model = ARIMA(history, order=order)
	model_fit = model.fit()

	ar_coef, ma_coef = model_fit.arparams, model_fit.maparams
	resid = model_fit.resid
	diff = difference(history)
	yhat = history[-1] + predict(ar_coef, diff) + predict(ma_coef, resid)
	predictions.append(yhat)
	obs = test[t]

	history.append(obs)
	print('>predicted=%.3f, expected=%.3f' % (yhat, obs))


crmse = sqrt(mean_squared_error(test, predictions))
print('Test RMSE: %.3f' % rmse)
(model_fit.summary())

#AR Model
model = ARIMA(testing_log, order=(2, 1, 0))
results_AR = model.fit(disp=-1)
plt.plot(testing_log_diff)
plt.plot(results_AR.fittedvalues, color='red')
plt.title('RSS: %.4f'% sum((results_AR.fittedvalues-testing_log_diff)**2))
plt.show()
#MA Model
model = ARIMA(testing_log, order=(0, 1, 2))
results_MA = model.fit(disp=-1)
plt.plot(testing_log_diff)
plt.plot(results_MA.fittedvalues, color='red')
plt.title('RSS: %.4f'% sum((results_MA.fittedvalues-testing_log_diff)**2))
plt.show()
'''
#ARIMA Model
model = ARIMA(testing_log, order=(1, 0, 0))
results_ARIMA = model.fit(disp=0)
plt.plot(testing_log_diff)
plt.plot(results_ARIMA.fittedvalues, color='red')
plt.title('RSS: %.4f'% sum((results_ARIMA.fittedvalues-testing_log_diff)**2))
plt.show()

predictions_ARIMA_diff =  results_ARIMA.forecast(steps=180)[0]
plt.plot(predictions_ARIMA_diff)
plt.show()

