import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('datasets/iris.data', header=0, sep=',', decimal='.')
print(df)
# przygotowanie wektora kolorów
colors = np.random.randint(0, 50, len(df.index))
# przygotowanie wektora z rozmiarami 'kropek'
scale = np.abs(df['sepal length'] - df['sepal width'])
plt.scatter(df['sepal length'], df['sepal width'], c=colors, s=scale)
plt.xlabel('sepal length')
plt.ylabel('sepal width')
plt.show()