import pandas as pd
import matplotlib.pyplot as plt

xlsx = pd.ExcelFile('datasets/imiona.xlsx')
df = pd.read_excel(xlsx)

plcie_ilosc = df.groupby(['Plec']).agg({'Liczba': ['sum']})

wykres = plcie_ilosc.plot.bar(ylabel='Liczba urodzeń')
wykres.legend()
plt.xticks(rotation=0)
plt.title("Liczba urodzonych chłopców i dziewczynek")
plt.show()
