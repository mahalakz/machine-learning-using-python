import pandas as pd
obj=pd.read_excel(open('D:/desktop/content ML/multireg.xlsx','rb'))

x=obj.iloc[:,:-1]
y=obj.iloc[:,-1]

import numpy as np
x=np.array(x)
y=np.array(y)

#preprocessing

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x=sc.fit_transform(x)

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2)

"""
from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(xtrain,ytrain)
ypred=lr.predict(xtest)
"""

from sklearn.ensemble import RandomForestRegressor
lr=RandomForestRegressor(n_estimators=1000)
lr.fit(xtrain,ytrain)
ypred=lr.predict(xtest)

#evaluating the result of regression
#visualization
xaxis=np.linspace(1,len(ytest),len(ytest))
import matplotlib.pyplot as plt
plt.plot(xaxis,ypred,color='blue')
plt.plot(xaxis,ytest,color='red')
plt.show()

#RMSE 
import numpy as np
from sklearn.metrics import mean_squared_error as mse
res=np.sqrt(mse(ytest,ypred))

