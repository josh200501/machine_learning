# -*- coding: utf8 -*-
import getvalue
import numpy as np
import matplotlib.pyplot as plt

dataset, datalength = getvalue.loaddataset()
dataset = np.mat(dataset)
#dataset = np.zeros((82,382))
length = np.shape(dataset)[0]
length1 = np.shape(dataset)[1]
x = [0.0]*length
y = [0.0]*length
z = [0.0]*length1
for i in range(length):
    x[i]=i
    y[i]=getvalue.distEclud(dataset[i,:], z)
plt.scatter(x, y, s=15, alpha=0.5)
plt.scatter(x, datalength, s=30, alpha=0.9)
plt.show()    
