import pandas as pd
obj=pd.read_excel(open('D:/desktop/AI Training Content/irisdataset.xlsx','rb'))

x=obj.iloc[:,[2,3]]
y=obj.iloc[:,-1]
from sklearn.impute import SimpleImputer
im=SimpleImputer()
x=im.fit_transform(x)

import numpy as np
x=np.array(x)
y=np.array(y)


import matplotlib.pyplot as plt
plt.plot(x[:,0],x[:,1],'or')
plt.show()

from sklearn.cluster import DBSCAN
model=DBSCAN(eps=0.35,min_samples=30) 
model.fit(x)
print(model.labels_)

plt.scatter(x[:,0],x[:,1],c=model.labels_,cmap='autumn')
plt.show()
