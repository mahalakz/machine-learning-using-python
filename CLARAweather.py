from pyclustering.utils import timedcall #conda install pyclustering
from pyclustering.cluster.clarans import clarans
import pandas as pd
obj=pd.read_excel(open('D:/desktop/AI Training Content/seattleWeather.xlsx','rb'))

x=obj.iloc[:,[1,2,3]]

import numpy as np
x=np.array(x)

import matplotlib.pyplot as plt
plt.plot(x[:,0],x[:,1],'or')
plt.show()

x=x.tolist()

model=clarans(x,2,4,10) #data,number_clusters,numlocal,maxneighbor
#calling claran process
#(ticks, result) = timedcall(model.process)

cluster=model.get_clusters()
print("The cluster points formed are:", cluster)
