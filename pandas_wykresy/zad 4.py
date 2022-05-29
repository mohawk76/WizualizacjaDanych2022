import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('datasets/zamowienia.csv', delimiter=';')
new_df = df.groupby('Sprzedawca').size()

plot = new_df.plot.bar(ylabel='Ilość zamówień')
plt.xticks(rotation=0)
plot.legend()
plt.subplots_adjust(left=0.1, right=0.9, bottom=0.2, top=0.9)
plt.title("Ilość zamówień sprzedawców")
plt.show()
