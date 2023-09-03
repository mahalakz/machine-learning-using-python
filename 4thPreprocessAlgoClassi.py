import pandas as pd
df=pd.read_csv(open("C:\Study Materials\DataSets\Churn_Modelling.xlsx","rb"))


#variable=dataframe.iloc[rows,columns]
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

#make sure your data should not have any string column.
#2) Now we can deal with missing value (data should not have any string value))

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


0   1000
1   0100
2   0010
3   0001 
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


#Algorithm use: Problem it contain 2 category in op. Classification: Gaussian Naive Bayes, Multinomial Naive Bayes, Random forest and so on.
# first algo is Naive bayes: This algo is the modification of Bayes theorem.
from sklearn.naive_bayes import GaussianNB
gnb=GaussianNB()
gnb.fit(xtrain,ytrain)  #normal classes teaching student how the ip is depending on op
pred=gnb.predict(xtest)  #taking the exam.


#evaluating classification problems
#1) accuracy score

from sklearn.metrics import accuracy_score
acc=accuracy_score(pred,ytest)

#2) confusion matrix
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(pred,ytest)

from sklearn.metrics import precision_recall_fscore_support
prfs=precision_recall_fscore_support(pred,ytest)


#if we need to find the reason of reduction in accuracy then we find confusion_matrix



"""
              0pred no        1pred yes
actual 0no    v1 higher       v2 lowest
actual 1yes   v3 lowest       v4 higher
"""


#till this step our first algo is done

from sklearn.naive_bayes import MultinomialNB   #it dnt consider negative values.
mnb=MultinomialNB()
mnb.fit(xtrain,ytrain)
predmnb=mnb.predict(xtest)


#evaluating classification problems
#1) accuracy score

from sklearn.metrics import accuracy_score
accmnb=accuracy_score(predmnb,ytest)

from sklearn.metrics import confusion_matrix
cmMnb=confusion_matrix(predmnb,ytest)



#it works on the concept of decision tree. collection of decision tree.
from sklearn.ensemble import RandomForestClassifier
rf=RandomForestClassifier(n_estimators=1000)
rf.fit(xtrain,ytrain)
predrf=rf.predict(xtest)


#evaluating classification problems
#1) accuracy score

from sklearn.metrics import accuracy_score
accrf=accuracy_score(predrf,ytest)


#import matplotlib.pyplot as plt
#plt.scatter(ip[:60,0],ip[:60,6],c=y[:60])



#KNN
from sklearn.neighbors import KNeighborsClassifier as KNN
model=KNN(n_neighbors=9)
predknn=model.fit(xtrain,ytrain).predict(xtest)
accKnn=accuracy_score(predknn,ytest)
print("Accuracy from KNN ",accKnn)


#Decision Tree with gini
from sklearn.tree import DecisionTreeClassifier
modelTree=DecisionTreeClassifier(criterion='gini')
modelTree.fit(xtrain,ytrain)
predgini=modelTree.predict(xtest)

from sklearn.metrics import accuracy_score
acc_gi=accuracy_score(predgini,ytest)
acc_gi*100
print("Accuracy from Decision Tree ",acc_gi)

#Pruning

#cost complexity

alpha=modelTree.cost_complexity_pruning_path(xtrain, ytrain)    

predTest=[]
predTrain=[]
for i in alpha['ccp_alphas']:
    modelTree1=DecisionTreeClassifier(ccp_alpha=i)
    modelTree1.fit(xtrain,ytrain)
    predTest.append(modelTree1.predict(xtest))
    predTrain.append(modelTree1.predict(xtrain))

#finds the accuracy for all the value of alpha
acctest=[]
acctrain=[]
for i in predTest:
    acctest.append(accuracy_score(i,ytest))
for j in predTrain:
    acctrain.append(accuracy_score(j,ytrain))



#visualize it.
axis=np.linspace(1,len(acctest),len(acctest))
import matplotlib.pyplot as plt
plt.plot(axis,acctest,color='blue')
plt.plot(axis,acctrain,color='red')
plt.show()
    
    


##SVM
from sklearn.svm import SVC
# Kernel = poly
model_poly = SVC(kernel = "poly")
model_poly.fit(xtrain,ytrain)
fpred_test_poly = model_poly.predict(xtest)
from sklearn.metrics import confusion_matrix,accuracy_score
print("Accuracy from SVC Poly kernel ",accuracy_score(ytest,fpred_test_poly))


# kernel = rbf
model_rbf = SVC(kernel = "rbf")
model_rbf.fit(xtrain,ytrain)
pred_test_rbf = model_rbf.predict(xtest)
from sklearn.metrics import confusion_matrix,accuracy_score
print("Accuracy from SVC RBF kernel ",accuracy_score(ytest,pred_test_rbf))



# kernel = sigmoid
model_sigmoid = SVC(kernel = "sigmoid")
model_sigmoid.fit(xtrain,ytrain)
pred_test_sigmoid = model_sigmoid.predict(xtest)
from sklearn.metrics import confusion_matrix,accuracy_score
print("Accuracy from SVC sigmoid kernel ",accuracy_score(ytest,pred_test_sigmoid))



# kernel = linear
model_linear = SVC(kernel = "linear")
model_linear.fit(xtrain,ytrain)
pred_test_linear = model_linear.predict(xtest)
from sklearn.metrics import confusion_matrix,accuracy_score
print("Accuracy from SVC Linear kernel ",accuracy_score(ytest,pred_test_linear))

#precision recall and fscore value to find out the performance given by the system
from sklearn.metrics import precision_recall_fscore_support
value=precision_recall_fscore_support(pred,ytest)


from sklearn.linear_model import LogisticRegression
modelLR=LogisticRegression()
modelLR.fit(xtrain,ytrain)
predLR = modelLR.predict(xtest)
from sklearn.metrics import confusion_matrix,accuracy_score
print("Accuracy from logistic Regression ",accuracy_score(ytest,predLR))

#precision recall and fscore value to find out the performance given by the system
from sklearn.metrics import precision_recall_fscore_support
valueLR=precision_recall_fscore_support(predLR,ytest)


