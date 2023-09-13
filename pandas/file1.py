import pandas as pd

#Series veri yapısı
#################################
obj = pd.Series([1,"Ali",3.5,"Hey"],index=["a","b","c","d"])

#print(obj.values)
#print(obj.index)
#################################
point = {"ali":90,"Can":80}
nt = pd.Series(point)#sözlüğü seriye çevirme

#print(nt)
#print(nt["ali"]) #belirli bir keye ait veri
#print(nt[nt>85])#85ten küçükleri filtrele
#print(nt<85)#85ten küçükleri hangileri true false

nt["can"]=60#serideki bir keye ait veriyi değiştirme
nt[nt<85]=60#serideki bir şarta ait veriyi değiştirme

#print(nt["can"])

print("ali" in nt)#serinin içinde ali keyi var mı ? 
#################################
