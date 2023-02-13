#lamda ifadeler (expression)
liste1=[1,2,3,4,5] #list comprehension yöntemini hatırlıyalım tek bir satırla liste oluşturma
liste2=[i*2 for i in liste1]

print(liste2)

# lamda tek bir satırla fonksiyon tanımlamayı sağlar.
def ikiylecarp(x):
    return x*2
print(ikiylecarp(4))

ikiylecarp2= lambda x: x*2
print(ikiylecarp2(3))

def toplama(x,y,z):
    return x+y+z
print(toplama(3,4,5))

toplama= lambda x,y,z:x+y+z
print(toplama(6,7,8))

ters=lambda s: s[::-1]
print(ters("pyhton"))

cift= lambda sayi: sayi % 2==0
print(cift(34))