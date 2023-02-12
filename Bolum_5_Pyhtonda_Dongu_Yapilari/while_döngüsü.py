#döngüdeki i değerini ekrana yazdırma
i=0
while(i<10):
    print("i'nin değeri",i)
    i+=1 #koşulun bir süre sonra False olması için gerekli - unutma!!!


#20 kere ekrana merhaba yazdıralım
j=0
while(j<20):
    print("Merhaba")
    j+=1 #koşulun bir süre sonra False olması için gerekli - unutma!!!


#liste üzerinde gezinme
liste=[1,2,3,4,5,6]
index=0
while(index<len(liste)):
    print("index:",index, "Liste Elemanı", liste[index])
    index+=1