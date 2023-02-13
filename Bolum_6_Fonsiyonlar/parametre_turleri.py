def selamla(isim="İsimsiz"): #varsayılan değer verme
    print("Selam", isim)

selamla("Gülten")
selamla() #varsayılan değer verdiğimiz için parametresiz çağırdığımızda "isimsiz " gözüküyor

def bilgileri_goster(ad="Bilgi Yok",soyad="Bilgi Yok",numara="Bilgi Yok"):
    print("Ad:",ad,"Soyad:", soyad, "Numara:",numara)

bilgileri_goster()
bilgileri_goster("Gülten", "Kaya") #numaraya otomatik olarak bilgi yok yazacak

def toplama(*a): #* koyarak istedeğiiz kadar değer gireriz
    print(a)
    toplam=0
    for i in a:
        toplam+=i
        print(toplam)
toplama(4,5)



