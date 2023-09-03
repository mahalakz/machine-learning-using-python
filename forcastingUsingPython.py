import pandas as pd
import numpy as np
import matplotlib.pylab as plt

data = pd.read_excel('D:/Desktop/Content DS/datasetShampoo.xlsx')
print(data.head())
print('\n Data Types:')
print(data.dtypes)

from datetime import datetime
con=data['Month']
data['Month']=pd.to_datetime(data['Month'])
data.set_index('Month', inplace=True)
#check datatype of index
data.index

#convert to time series:
ts = data['Sales']
ts.head(10)
plt.plot(ts)


from statsmodels.tsa.stattools import adfuller
def test_stationarity(timeseries):
    
    #Determing rolling statistics
    rolmean = timeseries.rolling(window=12).mean()
    rolstd = timeseries.rolling(window=12).std()
    #Plot rolling statistics:
    print("roll mean",rolmean)
    print("roll std",timeseries)
    plt.plot(timeseries, color='blue',label='Original')
    plt.plot(rolmean, color='red', label='Rolling Mean')
    plt.plot(rolstd, color='black', label = 'Rolling Std')
    plt.legend(loc='best')
    plt.title('Rolling Mean & Standard Deviation')
    plt.show()
    #Perform Dickey-Fuller test:
    print('Results of Dickey-Fuller Test:')
    dftest = adfuller(timeseries, autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
    for key,value in dftest[4].items():
        dfoutput['Critical Value (%s)'%key] = value
    print (dfoutput)
#parsing our model in function
test_stationarity(ts)


#making time series statistic.
ts_log=np.log(ts)
plt.plot(ts_log)

#we will find some noise here which is require to remove
#smoothing using rolling/moving average

mv_avg= ts_log.rolling(12).mean()
plt.plot(ts_log)
plt.plot(mv_avg,color='red')

#subtracting rolling mean from the original series
ts_log_mv_avg_di=ts_log- mv_avg
ts_log_mv_avg_di.head(12)

ts_log_mv_avg_di.dropna(inplace=True)
ts_log_mv_avg_di.head()

test_stationarity(ts_log_mv_avg_di)


#use of exponential weight moving average

expwgt=ts_log.ewm(halflife=12).mean()
plt.plot(ts_log)
plt.plot(expwgt,color='red')

#check stationary now
ts_log_ewm_di=ts_log-expwgt
test_stationarity(ts_log_ewm_di)

#now you will find it is stationary as the rolling variation is less and test statistic is less then 1%

#lets take the difference now
ts_log_di=ts_log-ts_log.shift()
plt.plot(ts_log_di)

#gives a curve which looks like fine. Now pass it to test function
ts_log_di.dropna(inplace=True)
test_stationarity(ts_log_di)


#now do time series forecasting.

from statsmodels.tsa.arima_model import ARIMA

#plots
from statsmodels.tsa.stattools import acf,pacf

lag_acf=acf(ts_log_di,nlags=20)
lag_pacf=pacf(ts_log_di,nlags=20,method='ols')

#plot ACF:
plt.subplot(121)
plt.plot(lag_acf)
plt.axhline(y=0,linestyle='--',color='gray')
plt.axhline(y=-1.96/np.sqrt(len(ts_log_di)),linestyle='--',color='gray')
plt.axhline(y=1.96/np.sqrt(len(ts_log_di)),linestyle='--',color='gray')
plt.title('Autocorrelation function')

#plot PACF
plt.subplot(122)
plt.plot(lag_pacf)
plt.axhline(y=0,linestyle='--',color='gray')
plt.axhline(y=-1.96/np.sqrt(len(ts_log_di)),linestyle='--',color='gray')
plt.axhline(y=1.96/np.sqrt(len(ts_log_di)),linestyle='--',color='gray')
plt.title('Partial Autocorrelation function')
plt.tight_layout()

#graph dotted line is the confidence interval
#print RSS for each ARIMA models

#AR model
model=ARIMA(ts_log,order=(2, 1, 0))
results_AR=model.fit(disp=-1)
plt.plot(ts_log_di)
plt.plot(results_AR.fittedvalues,color='red')
plt.title('RSS: %.4f'%sum((results_AR.fittedvalues-ts_log_di)**2))

#MA model
model=ARIMA(ts_log,order=(0,1,2))
results_MA=model.fit(disp=-1)
plt.plot(ts_log_di)
plt.plot(results_MA.fittedvalues,color='red')
plt.title('RSS: %.4f'%sum(results_MA.fittedvalues-ts_log_di)**2)
