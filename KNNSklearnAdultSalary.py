import pandas as pd
obj=pd.read_excel(open('D:\\desktop\\content ML\\adult_salary_dataset.xlsx','rb'))

x=obj.iloc[:,:-1]
y=obj.iloc[:,-1]

import numpy as np
x=np.array(x)
y=np.array(y)

#preprocessing
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


from sklearn.preprocessing import Imputer
im=Imputer()
x=im.fit_transform(x)

#dummies   the attribute whose label encoded are further use for making dummies.  1,2,3,4. 
from sklearn.preprocessing import OneHotEncoder
one=OneHotEncoder(categorical_features=[1,3,5,6,7,8,9,13])
x=one.fit_transform(x).toarray()

from sklearn.preprocessing import MinMaxScaler
sc=MinMaxScaler()
x=sc.fit_transform(x)


from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2)

from sklearn.neighbors import KNeighborsClassifier as knn
knnobject=knn()
knnobject.fit(xtrain,ytrain)  #training
ypred=knnobject.predict(xtest) #testing

from sklearn.naive_bayes import GaussianNB,MultinomialNB
gnb=GaussianNB()
gnb.fit(xtrain,ytrain)
ypredg=gnb.predict(xtest)

mnb=MultinomialNB()
mnb.fit(xtrain,ytrain)
ypredm=mnb.predict(xtest)

from sklearn.ensemble import RandomForestClassifier
rf=RandomForestClassifier(n_estimators=500)
rf.fit(xtrain,ytrain)
ypredf=rf.predict(xtest)


from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_recall_fscore_support as prfs
res=prfs(ytest,ypred)
cm=confusion_matrix(ypred,ytest)
acc=accuracy_score(ypred,ytest)
accg=accuracy_score(ypredg,ytest)
accrf=accuracy_score(ypredf,ytest)
accm=accuracy_score(ypredm,ytest)





