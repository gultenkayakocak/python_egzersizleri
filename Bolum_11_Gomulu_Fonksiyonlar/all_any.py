# Bütün değerler True ise True en az birisi False ise False döndürmek istiyoruz.
def hepsi(liste):
    for i in liste:
        if not i:
            return False
    return True
liste=[True,False,True,True]
print(hepsi(liste)) # en az biri false ise false döner

liste1=[1,2,3,4,5]
print(hepsi(liste1)) #hepsi 1 den büyük true old için true döner

#tüm değerle false ise false dönecek
def herhangi(liste):
    for i in liste:
        if i:
            return True
    return False
# Herhangi bir değer True ise True, Hepsi False ise False döndürmek istiyoruz.
print(herhangi(liste))

liste = [0,0,0,0,0,0,0] # Bütün değerler False , 0 = False
print(herhangi(liste))
#hepsi fonksiyonu all fonksyonuna eşit
#herhangi fonk any fonksiyonuna eşit
liste = [0,0,0,0,0,0,0]
print(any(liste))