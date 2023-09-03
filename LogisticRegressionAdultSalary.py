import pandas as pd
df=pd.read_csv(open("D:/desktop/AI Training Content/Churn_Modelling.csv","rb"))

x=df.iloc[:,3:-1]
y=df.iloc[:,-1]


import numpy as np
x=np.array(x)
y=np.array(y)

#Preprocessing Starting
#1) Strings convert into integers(label)

from sklearn.preprocessing import LabelEncoder
lbl=LabelEncoder()
x[:,1]=lbl.fit_transform(x[:,1])
x[:,2]=lbl.fit_transform(x[:,2])


#2) Now we can deal with missing value

from sklearn.impute import SimpleImputer
imp=SimpleImputer()
x=imp.fit_transform(x)



#3) Now whatever columns we have use for creating labels that coulmns are require to convert in the form of dummies.

"""

america   0
germany   2
france    1
pakistan  3

But my question was: to find the country having best medical facility.

country with best medical facility: pakistan


Solution???  Dummies variable

            america   germany  france   pakistan
america       1         0        0         0
germany       0         1        0         0
france        0         0        1         0  
pakistan      0         0        0         1

"""

xx=pd.DataFrame(x[:,1],columns=['c1'])
from sklearn.preprocessing import OneHotEncoder
oe=OneHotEncoder()
xx1=oe.fit_transform(xx)   #here it returns the object
xx1=xx1.toarray()

xx2=pd.DataFrame(xx1,columns=['c1','c2','c3'])

#remove the 2nd column from the input data
x=x[:,[0,2,3,4,5,6,7,8,9]]

#now convert x also in data frame format
x=pd.DataFrame(x,columns=['1','2','3','4','5','6','7','8','9'])


#now join x and dummy variable
ip=x.join(xx2)

#convert your data back in array format
ip=np.array(ip)

#4) Scale your data: normalizing it
#find out the mean of all 0 and standard deviation of all 1.
from sklearn.preprocessing import MinMaxScaler #algorithm like MultiNomial Naive Bayes(Dnt accept negative value).
from sklearn.preprocessing import StandardScaler #includes the -ve values
sc=MinMaxScaler()
ip=sc.fit_transform(ip)


#5) Divide your data into training and testing set
from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(ip,y,test_size=0.2) 
#split rule: 80:20,75:25,60:40

#preprocessing is competed and my data is ready for the algorithms.


from sklearn.linear_model import LogisticRegression
lr=LogisticRegression()
lr.fit(xtrain,ytrain)
ypred=lr.predict(xtest)

from sklearn.metrics import accuracy_score #evaluation of result
acc=accuracy_score(ypred,ytest)


