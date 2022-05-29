import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('flags.csv', sep=';')
countries_in_zones = df.groupby('Zone').size()
countries_in_zones.plot.bar(ylabel='Ilość krajów', xlabel='Strefy')
plt.xticks(rotation=0)
plt.subplots_adjust(left=0.1, right=0.9, bottom=0.2, top=0.9)
plt.title("Ilość krajów w strefach")
plt.show()
