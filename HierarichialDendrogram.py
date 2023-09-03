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

from scipy.cluster.hierarchy import dendrogram,linkage
resLink=linkage(x)
model=dendrogram(resLink)
#plt.show()
