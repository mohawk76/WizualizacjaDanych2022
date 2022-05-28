import pandas as pd


def printnl(content):
    print(content, end="\n\n")

#zad 1
xlsx = pd.ExcelFile('datasets/imiona.xlsx')
df = pd.read_excel(xlsx)

#zad 2
printnl(df[df.Liczba > 1000])
printnl(df[df.Imie == "MICHAŁ"])
printnl(df.Liczba.sum())
printnl(df[(df.Rok >= 2000) & (df.Rok <= 2005)].Liczba.sum())
printnl(df[df.Rok < 2006].groupby('Rok').agg({'Liczba': ['sum']}))
printnl(df.groupby('Plec').agg({'Liczba': ['sum']}))

df2 = df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec'])
for idx, group in enumerate(df2, start=1):
    print(f"{group[0]}")
    printnl(f"{group[1].iloc[0]['Imie']}: {group[1].iloc[0]['Liczba']}")



df3 = df.sort_values('Liczba', ascending=False).groupby(['Plec'])
for idx, group in enumerate(df3, start=1):
    print(f"{group[0]}")
    printnl(f"{group[1].iloc[0]['Imie']}: {group[1].iloc[0]['Liczba']}")


print("Chłopiec")
printnl(df[df['Plec'] == 'M'].groupby(['Imie']).agg({'Liczba': ['sum']}).sort_values(('Liczba', 'sum'),
                                                                                   ascending=False).iloc[0])
print("Dziewczynka")
printnl(df[df['Plec'] == 'K'].groupby(['Imie']).agg({'Liczba': ['sum']}).sort_values(('Liczba', 'sum'),
                                                                                   ascending=False).iloc[0])
