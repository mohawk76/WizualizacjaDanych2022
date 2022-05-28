import pandas as pd


def printnl(content):
    print(content, end="\n\n")


df = pd.read_csv("datasets/zamowienia.csv", sep=';', header=0, decimal='.')

printnl(df.Sprzedawca.unique())
printnl(df.sort_values('Utarg', ascending=False).head(5))
printnl(df.groupby('Sprzedawca').size())
printnl(df.groupby('Kraj').size())
printnl(df.groupby('Kraj').agg({'Utarg': ['sum']}))
printnl(df[(df['Kraj'] == 'Polska') & (df['Data zamowienia'] >= '2005-01-01') & (
        df['Data zamowienia'] <= '2005-12-31')].size)

printnl(df[(df['Kraj'] == 'Polska') & (df['Data zamowienia'] >= '2005-01-01') & (
        df['Data zamowienia'] <= '2005-12-31')].agg({'Utarg': ['sum']}))

printnl(df[(df['Data zamowienia'] >= '2004-01-01') & (
        df['Data zamowienia'] <= '2004-12-31')].agg({'Utarg': ['mean']}))

df[(df['Data zamowienia'] >= '2004-01-01') & (
        df['Data zamowienia'] <= '2004-12-31')].to_csv("datasets/zamowienia_2004.csv")
df[(df['Data zamowienia'] >= '2005-01-01') & (
        df['Data zamowienia'] <= '2005-12-31')].to_csv("datasets/zamowienia_2005.csv")