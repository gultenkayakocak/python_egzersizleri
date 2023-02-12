liste=[1,2,3,4,5,6,65,74,67,68]
for eleman in liste:
    print(eleman)
toplam=0
for i in liste:
    toplam=toplam+i
    print("Toplam: {} Eleman: {}".format (toplam,i))
print(toplam)

#çift sayıları ekrana bastırma
for i in liste:
    if i%2==0:
        print(i)

#string üzerinde for döngsü ile gezinmek
s="Python"
for i in s:
    print(i*3)

#Demetler üzerinde for döngüsü ile gezinmek
demet=(1,2,3,4)
for i in demet:
    print(i)

liste2=[(1,2), (3,4),(5,6)]
for eleman in liste2:
    print(eleman)
#aşaıdaki gibi yaparsak index in 1. elemanı i 2. elemanı j olur
#demetler çindeki her elemanı almak için
for(i,j) in liste2:

    print("i: {} j:{}".format(i,j))

#demet içindeki elemanların çarpımı
liste3=[(1,2,7), (3,4,5),(5,6,9)]
for(i,j,k) in liste3:
    print("i: {} j:{} k: {}".format(i,j,k))
print(i*j*k)

#dictionary sözlük üzerinde gezinmek
#sözlükte 3 method vardır keys() values() items()
sozluk={"bir":1,"iki":3,"üç":3}
#method kullanmadan sözlük üzerine gezinmek: sadece keys gözükür.
for i in sozluk:
    print(i)

#values değerleri için
for i in sozluk.values():
    print(i)

#item için i anahtar j values değeri olacak
for i,j in sozluk.items():
    print("Anahtar :{} Değer: {}".format(i,j))
