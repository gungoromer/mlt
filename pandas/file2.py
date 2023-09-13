import pandas as pd
import matplotlib as mp

#series ile çalışmak
oyunlar = pd.read_csv("vgsalesGlobale.csv")

#print(oyunlar.head())

#print(oyunlar.dtypes)

#print(oyunlar.Genre.describe()) #bir kolondaki özet bilgiyi gösterir.

#print(oyunlar.Genre.value_counts()) #sqldeki groupby count gibi çalışıyor.

#print(oyunlar.Genre.value_counts(normalize=True)) #yüzde olarak gösterir.

#print(oyunlar.Global_Sales.mean())


#oyunlar.Year.plot(kind="bar")

