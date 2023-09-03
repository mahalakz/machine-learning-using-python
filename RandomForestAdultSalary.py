import pandas as pd
obj=pd.read_excel(open('D:/desktop/content ML/adult_salary_dataset.xlsx','rb'))

x=obj.iloc[:,:-1]
y=obj.iloc[:,-1]

import numpy as np
x=np.array(x)
y=np.array(y)

#data-preprocessing
from sklearn.preprocessing import LabelEncoder
lb=LabelEncoder()
x[:,1]=lb.fit_transform(x[:,1])
x[:,3]=lb.fit_transform(x[:,3])
x[:,5]=lb.fit_transform(x[:,5])
x[:,6]=lb.fit_transform(x[:,6])
x[:,7]=lb.fit_transform(x[:,7])
x[:,8]=lb.fit_transform(x[:,8])
x[:,9]=lb.fit_transform(x[:,9])
x[:,13]=lb.fit_transform(x[:,13])
y=lb.fit_transform(y)


#from sklearn.preprocessing import Imputer
#im=Imputer()
#x=im.fit_transform(x)

from sklearn.impute import SimpleImputer
imp=SimpleImputer()
x=imp.fit_transform(x)


"""
Ques: Which country have the highest GDP.

india      2
pakistan   3
china      1
america    0

           india  pakistan  china  america
india       1         0       0       0
china       0         0       1       0
pakistan    0         1       0       0
america     0         0       0       1

"""

#dummies   the attribute whose label encoded are further use for making dummies.  1,2,3,4. 
from sklearn.preprocessing import OneHotEncoder

one=OneHotEncoder(categorical_features=[1,3,5,6,7,8,9,13])
x=one.fit_transform(x).toarray()
#In latest anaconda software this feature is now changed. So in place of it you have to write:
"""
from sklearn.preprocessing import OneHotEncoder
onehotencoder=OneHotEncoder(handle_unknown='ignore')
ip=pd.DataFrame(column whose dummy we want,columns=['test']) #converting our column in data frame
ip1=onehotencoder.fit_transform(ip[['test']]).toarray()
b = pd.DataFrame(ip1,columns=['10','11','12']) #10,11,12 means 3 coulmns will produce because in this coulmn we have three strings: germany, spain, france
X=actualdata in dataframe format.join(b)


"""

from sklearn.preprocessing import StandardScaler,MinMaxScaler
sc=StandardScaler()
x=sc.fit_transform(x)

#splitting our dataset into two parts.

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2) #80:20, 75:25, 60:40


#Now my data is ready for the algo development.

from sklearn.ensemble import RandomForestClassifier
lr=RandomForestClassifier(n_estimators=1000)
lr.fit(xtrain,ytrain)  #teaching
ypred=lr.predict(xtest) #exam

from sklearn.metrics import accuracy_score
acc=accuracy_score(ypred,ytest)
