import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('flags.csv', sep=';')

countries_N = df[(df.Zone == 'N') | (df.Zone == 'NE') | (df.Zone == 'NW')]
print(countries_N)

countries_N_grouped = countries_N.groupby('Landmass')
countries_N_grouped_area = countries_N_grouped.agg({'Area': ['sum']})

countries_N_grouped_area.plot.pie(subplots=True, autopct='%.2f %%', fontsize=14)
plt.legend()
plt.title("Wielkości kontynetów")
plt.show()
