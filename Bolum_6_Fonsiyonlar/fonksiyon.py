def selamla():
    print("Merhaba")
    print("Nasılsın?")

print(type(selamla))
selamla()
#selamla() parametre vermediğimiz için parantez içine bişey yazamayız

#parametre alan fonksiyon
def selam(isim):  #isim parametre
    print("İsiminiz", isim)

selam("Kemal") #Kemall arguman çünkü  gönderilen değerlere argüman denir

def toplama(a,b,c):
    print("Toplamları",a+b+c)
toplama(3,4,5)
toplama(20,45,34)

def faktoriyel(sayi):
    fakt=1
    if(sayi==0 or sayi==1):
        print("Faktöriyel=", fakt)
    else:
        while(sayi>1):
            fakt *=sayi
            sayi-=1
        print("Faktoriyel:", fakt)
faktoriyel(5)