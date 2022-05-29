import pandas as pd
import matplotlib.pyplot as plt

xlsx = pd.ExcelFile('datasets/imiona.xlsx')
df = pd.read_excel(xlsx)

plcie_ilosc = df[df.Rok > 2012].groupby(['Plec']).agg({'Liczba': ['sum']})

wykres = plcie_ilosc.plot.pie(subplots=True, autopct='%.2f %%', fontsize=20)
plt.legend()
plt.title("Urodzenia dziewczynki i chłopcy 2013 - 2017")
plt.show()
