liste = ["Elma","Armut","Muz","Kiraz"]

# sonucu [(0,'Elma'),(1,'Armut'),(2,'Muz'),(3,'Kiraz')] yapmak istiyoruz.

sonuc = list()

i = 0
while(i<len(liste)):
    sonuc.append((i,liste[i]))
    i+=1
print(sonuc)

#aynı işlemi enumerate fonksiyonu kullanarak yapılabilir

print(list(enumerate(liste)))
for i,j in enumerate(liste):
    print(i,j)


#numarası çift olanları yazdır
liste1=["a","b","c","d","e","f","g"]
for index,eleman in enumerate(liste1):
    if(index%2 ==0):
        print("Eleman:",eleman)
