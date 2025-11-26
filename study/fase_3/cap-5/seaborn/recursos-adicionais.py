import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
sns.set_theme(style="dark")

# Gaussiana bivariada
n = 10000
mean = [0, 0]
cov = [(2, .4), (.4, .2)]
rng = np.random.RandomState(0)
x, y = rng.multivariate_normal(mean, cov, n).T

# Histograma scatterplot com contorno de densidade
f, ax = plt.subplots(figsize=(12, 6))
sns.scatterplot(x=x, y=y, s=5, color=".15")
sns.histplot(x=x, y=y, bins=50, pthresh=.1, cmap="mako")
sns.kdeplot(x=x, y=y, levels=5, color="w", linewidths=1)