def fonksiyon():
    a=10 #yerel değişken
    print(10)

fonksiyon()
# print(a)  hata verir a sadece fonksiyon içinde tanımlı bir değişken

b=4 #global değişken
def fonksiyon_2():
    print(b)
fonksiyon_2()

c=10
def fonksiyon_3():
    c=2
    print(c)
fonksiyon_3() # yerel değişkeni alır 2
print(c) #globaldaki değeri gösterir 10

d=5
def fonksiyon_4():
    global d=3
    print(d)
fonksiyon_4() #gloabal değeri bastırır 3
print(d) #gloabal değeri bastırır 3
