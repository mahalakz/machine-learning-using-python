import pandas as pd
import numpy as np
df=pd.read_excel(open("D:/study/projects technical/AI ML DM/dataset/irisdataset.xlsx","rb"))
x=df.iloc[:,:-1]
y=df.iloc[:,-1]
x=np.array(x)
y=np.array(y)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x=sc.fit_transform(x)   #processing speed

from sklearn.preprocessing import LabelEncoder
lb=LabelEncoder()
y=lb.fit_transform(y)

import matplotlib.pyplot as plt
plt.plot(x[:,1],x[:,3],'o')
plt.show()
#Reducing the data from 4 columns to 2 columns

from sklearn.decomposition import PCA

pcaRes = PCA(n_components=2)
principalComponents = pcaRes.fit_transform(x)
pcaFinal = pd.DataFrame(data = principalComponents, columns = ['Att1', 'Att2'])

pcaFinal=np.array(pcaFinal)
import matplotlib.pyplot as plt
plt.scatter(pcaFinal[:,0],pcaFinal[:,1],c=y,cmap='autumn')
plt.show()

from sklearn.cluster import KMeans
model=KMeans(n_clusters=3)
model.fit(pcaFinal)
print(model.labels_)

plt.scatter(pcaFinal[:,0],pcaFinal[:,1],c=model.labels_,cmap='autumn')
plt.show()

#next steps: implement supervised learning