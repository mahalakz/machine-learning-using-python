import pandas as pd
df=pd.read_csv(open("D:/study/projects technical/AI ML DM/dataset/Life Expectancy Data.csv","rb"))
x=df.iloc[:,[0,1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]]
y=df.iloc[:,3] 


import numpy as np
x=np.array(x)
y=np.array(y)



#Preprocessing Starting
#1) Strings convert into integers(label)

from sklearn.preprocessing import LabelEncoder
lbl=LabelEncoder()
x[:,0]=lbl.fit_transform(x[:,0])
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

xx=pd.DataFrame(x[:,0],columns=['c1'])
from sklearn.preprocessing import OneHotEncoder
oe=OneHotEncoder()
xx1=oe.fit_transform(xx)   #here it returns the object
xx1=xx1.toarray()


seq=np.linspace(1, xx1.shape[1],xx1.shape[1])

xx2=pd.DataFrame(xx1,columns=seq)

#remove the 2nd column from the input data
x=x[:,[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]]

arr=[]
for i in range(20):
    arr.append('c'+str(i))
    
    
#now convert x also in data frame format
x=pd.DataFrame(x,columns=arr)


#now join x and dummy variable
ip1=x.join(xx2)

#convert your data back in array format
ip=np.array(ip1)


#use one concept to convert the data type

xFloat=ip.astype('int')
yFloat=y.astype('int')


#4) Scale your data: normalizing it
#find out the mean of all 0 and standard deviation of all 1.
from sklearn.preprocessing import MinMaxScaler #algorithm like MultiNomial Naive Bayes(Dnt accept negative value).
from sklearn.preprocessing import StandardScaler #includes the -ve values
sc=MinMaxScaler()
xFloat=sc.fit_transform(xFloat)


#5) Divide your data into training and testing set
from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(xFloat,yFloat,test_size=0.2) 
#split rule: 80:20,75:25,60:40



#apply algo

from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(xtrain,ytrain)
pred=lr.predict(xtest)

#for regression the evaluation method is completely different.
#1) visualization

xaxis=np.linspace(1,len(pred),len(pred))
import matplotlib.pyplot as plt
plt.plot(xaxis,pred,color='red')
plt.plot(xaxis,ytest,color='blue')
plt.show()

#2) how much good??? to define it in a number RMSE calculate
from sklearn.metrics import mean_squared_error
res=np.sqrt(mean_squared_error(pred,ytest))
