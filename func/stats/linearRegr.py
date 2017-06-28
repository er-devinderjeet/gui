__author__ = 'Devinderjeet'

#import datetime
import matplotlib.pyplot as plt
#import matplotlib.ticker as mticker
import numpy as np
import matplotlib
#from matplotlib.finance import candlestick_ohlc
matplotlib.rcParams.update({'font.size':9})
#matplotlib.use('Qt4Agg')
#import datetime as dt
import pandas as pd
#from ..userstats import centralTendency
from func.graph.charting import *

import statsmodels.api as sm
from statsmodels import regression
from scipy import stats
from statsmodels.sandbox.regression.predstd import wls_prediction_std
from func.eventdriven.data import DataHandler


class user_Defined_Linear_Regression:
    def user_Defined_OLS(self):
        #stock, indice,stockDate,indiceDate
        try:
            user_Obj_A = DataHandler.DataHandler()
            date,indice_close,stock_close,indice_volume,stock_volume= user_Obj_A.user_Defined_CSV()
            alpha, beta, nobs, dfModel,result = self.user_Defined_Linreg(indice_close,stock_close)
            plt.scatter(indice_close,stock_close, alpha=0.3)

            plt.ylabel("Stock Price")
            plt.xlabel("Indice")

            print 'alpha: ' + str(alpha)
            print 'beta: ' + str(beta)
            print 'no. of Obsev: ' + str(nobs)
            print 'df Model: ' + str(dfModel)
            print 'Result: ' + str(result)

            X2 = np.linspace(indice_close.min(), indice_close.max(), nobs)
            Y_hat = X2 * beta + alpha

            plt.scatter(indice_close,stock_close, alpha=0.3)

            plt.ylabel("Stock Price")
            plt.xlabel("Indice")
            # Add the regression line, colored in red
            plt.plot(X2, Y_hat, 'r', alpha=0.9)

            X3 = sm.add_constant(X2)
            y_err = stock_close - Y_hat
            mean_x = indice_close.T[1].mean()
            dof = nobs - dfModel - 1
            t = stats.t.ppf(1-0.025, df=dof)
            s_err = np.sum(np.power(y_err, 2))
            conf = t * np.sqrt((s_err/(nobs-2))*(1.0/nobs + (np.power((X2-mean_x),2) /
                ((np.sum(np.power(X2,2))) - nobs*(np.power(mean_x,2))))))
            upper = Y_hat + abs(conf)
            lower = Y_hat - abs(conf)

            sdev, outter_lower, outter_upper = wls_prediction_std(result, exog=X3, alpha=0.05)

            #print 'Outter_Lower'+outter_lower
            plt.fill_between(X2, lower, upper, color='#888888', alpha=0.8)

            plt.fill_between(X2, outter_lower, outter_upper, color='#888888', alpha=0.1)
            #xx= result.predict()
            #plt.plot(xx,color='K')
            plt.show()
            return stock_close,indice_close,nobs
            #sharpe_y = self.equity_sharpe(closep_y)
            #print sharpe_y

        except Exception,e:
            print str(e)

    def calc_ADF(self):

        user_Obj_A = DataHandler.DataHandler()
        date,indice_close,stock_close,indice_volume,stock_volume= user_Obj_A.user_Defined_CSV()

        data = pd.DataFrame({'indice':indice_close,'stock':stock_close})
        print self.equity_sharpe(data,'stock')

    def user_Defined_Linreg(self,x,y):
        # We add a constant so that we can also fit an intercept (alpha) to the model
        # This just adds a column of 1s to our data
        x = sm.add_constant(x)
        model = regression.linear_model.OLS(y,x).fit()
        # Remove the constant now that we're done
        x = x[:, 1]
        print model.summary()

        return model.params[0], model.params[1],model.nobs,model.df_model,model

    def sharpe_ratio(self,returns):
        """
        Calculate the annualised Sharpe ratio of a returns stream
        based on a number of trading periods, N. N defaults to 252,
        which then assumes a stream of daily returns.
        The function assumes that the returns are the excess of
        those compared to a benchmark.
        """
        period =(252*6.5*60)
        return np.sqrt(period) * np.mean(returns) / np.std(returns)

    def equity_sharpe(self,var_a,stock_close_price):
        """
        Calculates the annualised Sharpe ratio based on the daily
        returns of an equity ticker symbol listed in Google Finance.
        The dates have been hardcoded here for brevity.
        """
        period =(252*6.5*60)
        # Obtain the equities daily historic data for the desired time period
        # and add to a pandas DataFrame
        # Use the percentage change method to easily calculate daily returns
        daily_ret = var_a[stock_close_price].pct_change()

        # Assume an average annual risk-free rate over the period of 5%
        excess_daily_ret = daily_ret/period

        # Return the annualised Sharpe ratio based on the excess daily returns
        return self.sharpe_ratio(excess_daily_ret)

