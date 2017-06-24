__author__ = 'Devinderjeet'
from statsmodels import api as sm
from matplotlib import pyplot as plt
from scipy import stats
import numpy as np
import matplotlib.animation as anim


def acf_and_pacf(stock,nlags = 100):
    for _ in xrange(481 / 60):
        stock = np.concatenate((stock, np.random.normal(0, 0.1, 60) + stock[:60]))
    stock = stock[:]
    n = stock.shape[0]
    pa = sm.tsa.pacf(stock, nlags=nlags)
    acf = sm.tsa.acf(stock, nlags=nlags)

    plt.figure()
    plt.subplot(4, 1, 1)
    plt.plot(stock)
    plt.title("Time Series with a Lag of 60, White Noise of .1")
    plt.subplot(4, 1, 2)
    plt.plot(stock.reshape(-1, 481).T)
    plt.title("Overlapping Windows")
    plt.subplot(4, 1, 3)
    plt.plot(acf)
    z = stats.norm.ppf(0.95)
    c = '#660099'
    plt.axhline(y=z / np.sqrt(n), linestyle='--', color=c)
    plt.axhline(y=-z / np.sqrt(n), linestyle='--', color=c)
    plt.title("ACF")
    plt.subplot(4, 1, 4)
    plt.plot(pa)
    plt.axhline(y=z / np.sqrt(n), linestyle='--', color=c)
    plt.axhline(y=-z / np.sqrt(n), linestyle='--', color=c)
    plt.title("PACF")
    plt.show()

def draw_Graph_Of_Stock(stock):
    plt.figure()
    plt.subplot(1, 1, 1)
    plt.plot(stock)
    plt.title("Y Stock")
    plt.show()
def draw_LRScatter(x,y,label_x,label_y):
    plt.scatter(x,y, alpha=0.3)
    plt.ylabel(label_x)
    plt.xlabel(label_y)
    # Add the regression line, colored in red

def plot_price_series(x_close, y, x_label,y_label):
    '''
    months = mdates.MonthLocator() # every month
    fig, ax = plt.subplots()
    ax.plot(index, x, label=x_label)
    ax.plot(index, y, label=y_label)

    ax.xaxis.set_major_locator(months)
    ax.xaxis.set_major_formatter(mdates.DateFormatter(%b %))
    ax.set_xlim(datetime.datetime(2012, 1, 1), datetime.datetime(2013, 1, 1))
    ax.grid(True)
    fig.autofmt_xdate()
    plt.xlabel(Month/Year)
    plt.ylabel(Price ($))
    plt.title(%s and %s Daily Prices% (ts1, ts2))
    plt.legend()
    plt.show()
    '''
def plot_cont(stock):

    plt.ion() ## Note this correction
    fig=plt.figure()
    len_stock = len(stock)
    plt.axis([0,len_stock,0,1])

    i=0
    x=list()
    y=list()

    while i <len_stock:
        temp_y=stock
        x.append(i)
        y.append(temp_y)
        plt.plot(i,temp_y)
        i+=1;
        plt.show()
        plt.pause(0.0001)
