import pandas as pd
obj=pd.read_csv(open("D:/study/projects technical/AI ML DM/dataset/New Dataset/weather-dataset-preprocessed/weatherAUS.csv","rb"))
x=obj.iloc[:,[1,2,3,4,7,8,9,10,11,12,13,14,15,16,19,20,21,22]]
y=obj.iloc[:,-1]
#convert it in the form of array from data frame

import numpy as np
x=np.array(x)
y=np.array(y)

#preprocessing

#Label encoding

from sklearn.preprocessing import LabelEncoder
lbl=LabelEncoder()
x[:,0]=lbl.fit_transform(x[:,0])
x[:,4]=lbl.fit_transform(x[:,4])
x[:,6]=lbl.fit_transform(x[:,6])
x[:,7]=lbl.fit_transform(x[:,7])
x[:,16]=lbl.fit_transform(x[:,16])
y=lbl.fit_transform(y)


#missing values
#from sklearn.preprocessing import Imputer
from sklearn.impute import SimpleImputer
imp=SimpleImputer()
#imp=Imputer()
x=imp.fit_transform(x)

#create dummies
from sklearn.preprocessing import OneHotEncoder
oe=OneHotEncoder(categories=[0,4,6,7,16])
x=oe.fit_transform(x).toarray()


1
2
3
4
5
  1 2 3 4 5
1 1 0 0 0 0
2 0 1 0 0 0 
3 0 0 1 0 0
4  
  
#scale our data
from sklearn.preprocessing import MinMaxScaler
sc=MinMaxScaler()
x=sc.fit_transform(x)

#split into training and testing set
from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2)

#apply an algorithm
#we have classification problem
from sklearn.naive_bayes import GaussianNB
gnb=GaussianNB()
gnb.fit(xtrain,ytrain)
ypred=gnb.predict(xtest)

from sklearn.ensemble import RandomForestClassifier
rf=RandomForestClassifier()
rf.fit_transform(xtrain,ytrain)
ypredrf=rf.predict(xtest)


#evaluating our model
from sklearn.metrics import accuracy_score
acc=accuracy_score(ypred,ytest)


from sklearn.naive_bayes import MultinomialNB
mnb=MultinomialNB()
mnb.fit(xtrain,ytrain)
ypredm=mnb.predict(xtest)

#evaluating our model for classification algorithms
from sklearn.metrics import accuracy_score
accm=accuracy_score(ypredm,ytest)

from sklearn.metrics import confusion_matrix,precision_recall_fscore_score
cm=confusion_matrix(ypred,ytest)
precision_recall_fscore_score(ypred,ytest)