#continue ifadesi ile karşılaşıldığında zaman geri kalan işlemleri yapmadan direk bloğun başına döner
liste=[1,2,3,4,5,6,65,74,67,68]
for eleman in liste:
    if(eleman==3 or eleman==65):
        continue
    print("eleman",eleman)
