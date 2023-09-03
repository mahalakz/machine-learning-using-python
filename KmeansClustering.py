import pandas as pd
obj=pd.read_excel(open('D:/desktop/AI Training Content/irisdataset.xlsx','rb'))

#x=obj.iloc[:,[2,3]]
x=obj.iloc[:,:-1]

y=obj.iloc[:,-1]
from sklearn.impute import SimpleImputer
im=SimpleImputer()
x=im.fit_transform(x)

import numpy as np
x=np.array(x)
y=np.array(y)


#to convert our string values from target into lanbel we use

from sklearn.preprocessing import LabelEncoder
lbl=LabelEncoder()
y=lbl.fit_transform(y)

import matplotlib.pyplot as plt
plt.plot(x[:,2],x[:,3],'or')
plt.show()

import matplotlib.pyplot as plt
plt.scatter(x[:,2],x[:,3],c=y)


from sklearn.cluster import KMeans
model=KMeans(n_clusters=3)
model.fit(x)
print(model.labels_)

plt.scatter(x[:,2],x[:,3],c=model.labels_)
plt.show()



#whatever target we get from unsupervised learning we can use for making predictive model using suoervised learning.

#FOR TESTING WE  can show the real target over a plot

plt.scatter(x[:,0],x[:,1],c=y,cmap='autumn')
plt.show()



y=model.labels_ 

#NNow use any classification algo for creating a model