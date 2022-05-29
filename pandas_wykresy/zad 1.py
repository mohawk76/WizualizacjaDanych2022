import pandas as pd
import matplotlib.pyplot as plt

xlsx = pd.ExcelFile('datasets/imiona.xlsx')
df = pd.read_excel(xlsx)

lata = df.Rok.unique()
ilosc_dzieci = df.groupby('Rok').agg({'Liczba': ['sum']})

wykres = ilosc_dzieci.plot()
wykres.set_xticks(lata)
wykres.set_ylabel('Liczba urodzonych dzieci')
wykres.tick_params(axis='x', labelrotation=40)
wykres.legend()
plt.subplots_adjust(left=0.15, right=0.9, bottom=0.15, top=0.9)
plt.title("Liczba urodzonych dzieci dla każdego roku")
plt.show()
