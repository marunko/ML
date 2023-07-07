import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

import tensorflow as tf
import tensorflow_hub as hub

df = pd.read_csv("../diabetes.csv")
x = df[df.columns[:-1]].values
y = df[df.columns[-1]].values

#print(df[df.columns[:-1]].values)

#plt.hist(df.points, bins=20)
xpoints = np.array([1, 8])
ypoints = np.array([3, 10])
#plt.plot(xpoints, ypoints)
#plt.show()

