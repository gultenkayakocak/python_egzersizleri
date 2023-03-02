#zip fonksiyonu gruplama işlemi yapar
liste1=[1,2,3,4,5]
liste2=[6,7,8,9,10,11,12]
i=0
sonuc=list()
while(i < len(liste1) and i < len(liste2)):
    sonuc.append((liste1[i], liste2[i]))
    i+=1
print(sonuc)

zip(liste1,liste2)
print(list(zip(liste1,liste2)))
listex=[1,2,3,4]
listey=[5,7,8,9,9]
listez=["pyhton","c","java"]
print(list(zip(listex,listey,listez)))

for i,j  in zip(listex,listez):
    print(i,j)

    #sözlükler zipleme
sozluk1 = {"Elma": 1, "Armut": 2, "Kiraz": 3}
sozluk2 = {"Sıfır": 0, "Bir": 1, "İki": 2}
zip(sozluk1,sozluk2)
print(list(zip(sozluk1,sozluk2)) )#anahtar eşleşti
print(list(zip(sozluk1.values(),sozluk2.values())))