'''
# RSI = 100 - 100 / (1 + RS)
# RS = Average gain / Average loss
# First Average Gain = Sum of Gains over the past 14 periods / 14
# First Average Loss = Sum of Losses over the past 14 periods / 14
# Average Gain = [(previous Average Gain) x 13 + current Gain] / 14
# Average Loss = [(previous Average Loss) x 13 + current Loss] / 14
#
# RSI is 0 when the Average Gain equals zero. Assuming a 14-period RSI, a zero RSI value means prices moved lower all
# 14 periods. There were no gains to measure.
# RSI is 100 when the Average Loss equals zero. This means prices moved higher all 14 periods.
# There were no losses to measure.
#
# If Average Loss equals zero, a "divide by zero" situation occurs for RS and RSI is set to 100 by definition.
# Similarly, RSI equals 0 when Average Gain equals zero.
#
# RSI is considered overbought when above 70 and oversold when below 30.
# These traditional levels can also be adjusted to better fit the security or analytical requirements.
# Raising overbought to 80 or lowering oversold to 20 will reduce the number of overbought/oversold readings.
# Short-term traders sometimes use 2-period RSI to look for overbought readings above 80 and oversold readings below 20.

def gain_loss_one(prevValue, nextValue):
    change = nextValue - prevValue
    if change < 0:
        gain = 0
        loss = abs(change)
    else:
        gain = change
        loss = 0
    return gain, loss


# [begin, end)
def avg_gain_loss(values, begin, end):
    rangeLen = end - begin
    if rangeLen < 2:
        return None

    gain = 0
    loss = 0
    for i in xrange(begin+1, end):
        currGain, currLoss = gain_loss_one(values[i-1], values[i])
        gain += currGain
        loss += currLoss
    return (gain/float(rangeLen-1), loss/float(rangeLen-1))


def rsi(values, period):
    assert(period > 1)
    if len(values) < period + 1:
        return None

    avgGain, avgLoss = avg_gain_loss(values, 0, period)
    for i in xrange(period, len(values)):
        gain, loss = gain_loss_one(values[i-1], values[i])
        avgGain = (avgGain * (period - 1) + gain) / float(period)
        avgLoss = (avgLoss * (period - 1) + loss) / float(period)

    if avgLoss == 0:
        return 100
    rs = avgGain / avgLoss
    return 100 - 100 / (1 + rs)


class RSIEventWindow(technical.EventWindow):
    def __init__(self, period):
        assert(period > 1)
        # We need N + 1 samples to calculate N averages because they are calculated based on the diff with previous values.
        super(RSIEventWindow, self).__init__(period + 1)
        self.__value = None
        self.__prevGain = None
        self.__prevLoss = None
        self.__period = period

    def onNewValue(self, dateTime, value):
        super(RSIEventWindow, self).onNewValue(dateTime, value)

        # Formula from http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:relative_strength_index_rsi
        if value is not None and self.windowFull():
            if self.__prevGain is None:
                assert(self.__prevLoss is None)
                avgGain, avgLoss = avg_gain_loss(self.getValues(), 0, len(self.getValues()))
            else:
                # Rest of averages are smoothed
                assert(self.__prevLoss is not None)
                prevValue = self.getValues()[-2]
                currValue = self.getValues()[-1]
                currGain, currLoss = gain_loss_one(prevValue, currValue)
                avgGain = (self.__prevGain * (self.__period-1) + currGain) / float(self.__period)
                avgLoss = (self.__prevLoss * (self.__period-1) + currLoss) / float(self.__period)

            if avgLoss == 0:
                self.__value = 100
            else:
                rs = avgGain / avgLoss
                self.__value = 100 - 100 / (1 + rs)

            self.__prevGain = avgGain
            self.__prevLoss = avgLoss

    def getValue(self):
        return self.__value


class RSI(technical.EventBasedFilter):
    """Relative Strength Index filter as described in http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:relative_strength_index_rsi.

    :param dataSeries: The DataSeries instance being filtered.
    :type dataSeries: :class:`pyalgotrade.dataseries.DataSeries`.
    :param period: The period. Note that if period is **n**, then **n+1** values are used. Must be > 1.
    :type period: int.
    :param maxLen: The maximum number of values to hold.
        Once a bounded length is full, when new items are added, a corresponding number of items are discarded from the
        opposite end. If None then dataseries.DEFAULT_MAX_LEN is used.
    :type maxLen: int.
    """

    def __init__(self, dataSeries, period, maxLen=None):
        super(RSI, self).__init__(dataSeries, RSIEventWindow(period), maxLen)
'''
import numpy as np
def rsiFunc(prices, n=14):
    deltas = np.diff(prices)
    seed = deltas[:n+1]
    up = seed[seed>=0].sum()/n
    down = -seed[seed<0].sum()/n
    rs = up/down
    rsi = np.zeros_like(prices)
    rsi[:n] = 100. - 100./(1.+rs)

    for i in range(n, len(prices)):
        delta = deltas[i-1] # cause the diff is 1 shorter

        if delta>0:
            upval = delta
            downval = 0.
        else:
            upval = 0.
            downval = -delta

        up = (up*(n-1) + upval)/n
        down = (down*(n-1) + downval)/n

        rs = up/down
        rsi[i] = 100. - 100./(1.+rs)

    return rsi