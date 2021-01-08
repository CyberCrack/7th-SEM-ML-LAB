import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture

data = pd.read_csv("KMeansData.csv")
f1 = data['Distance_Feature']
f2 = data['Speeding_Feature']
X = np.array(list(zip(f1, f2)))
plt.scatter(f1, f2, color='black')
plt.show()
kmeans = KMeans(2).fit(X)
labels = kmeans.predict(X)
print("Graph using KMeans Algorithm")
plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.show()
gnm = GaussianMixture(3).fit(X)
labels = gnm.predict(X)
print("Graph using EM Algorithm")
plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.show()
