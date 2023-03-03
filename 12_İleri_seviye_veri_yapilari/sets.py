#küme olultur
x={1,2,3}
print(type(x))


liste=[1,1,3,4,5,6,7] # Aynı elemanı birçok defa  barındıran bir liste
x=set(liste) # Veri tipi dönüşümü
print(x)

y=set("Python dili kullanımı")
print(y)

#for döngüsü ile gezinmek
z={"Python","C","Java",".NET"}
for i in z:
    print(i)

#Küme methodları
q={1,2,3}
q.add(4)
print(q)

#iki kümenin farkı
kume1 = {1,2,3,10,34,100,-2}
kume2 = {1,2,23,34,-1}
print(kume1.difference(kume2)) #kümeler arasındaki farkı listeler
print(kume2.difference(kume1)) #2.kumenin 1 den farkını yazar


#İki kümenin farkı ve güncelleme : difference_update() metodu
print(kume1.difference_update(kume2))

#Kümeden Eleman Çıkartmak : discard() metodu
kume1.discard(2)
print(kume1)

#Küme kesişimleri : intersection() metodu
print(kume1)
kume1.add(23) #ortak sayı olması için ekleme yaptım
print(kume2)
print(kume1.intersection(kume2))


# Kümeler ayrık küme mi ? : isdisjoint() metodu
#Bu metod, eğer iki kümenin kesişim kümesi boş ise True, değilse False döner.
kume3 = {1,2,3,10,34,100,-2}
kume4 = {1,2,23,34,-1}
kume5 = {30,40,50}
print(kume3.isdisjoint(kume4))
print(kume3.isdisjoint(kume5))


#Alt kümesi mi ? : issubset() metodu
#Bu metod , birinci küme ikinci kümenin alt kümesiyse True, değilse False döner.
print(kume3.issubset(kume4))


#Birleşim Kümesi : union() metodu
#Bu metod, iki kümenin birleşim kümesini döner.
print(kume5.union(kume3))
print(kume5.update(kume3))