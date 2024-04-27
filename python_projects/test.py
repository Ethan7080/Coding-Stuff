import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_openml
mnist = fetch_openml("mnist_784", version=1, as_frame=False)
mnist.target = mnist.target.astype(int)
X = mnist['data']
f,ax = plt.subplots(1, 7, figsize=(13,2))
for n in range(7):
    sns.heatmap(X[n].reshape(28, 28), cbar=False, cmap='gray_r', ax=ax[n])

