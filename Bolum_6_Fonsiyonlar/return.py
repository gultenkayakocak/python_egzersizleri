#return komutu fonksiyondan değer döndürmemizi sağlıyor
def toplama(a,b,c):
    return(a+b+c)

def ikiylecarp(a):
    return(a*2)

toplam=toplama(1,2,3)
print(ikiylecarp(toplam))


def ucle_carp(a):
    print("1.işlem yapıldı")
    return a*3

def ikiyle_topla(a):
    print("2. işlem yapıldı")
    return a+2

def dorde_bol(a):
    print("3. işlem yapıldı")
    return a/4

print(dorde_bol(ikiyle_topla(ucle_carp(6))))

def carpma(a,b):
    print("Çarpma sonucu") #return komutunun altına yazsaydık ekranda gözükmeyecekti
    return a * b
print(carpma(5,5))
