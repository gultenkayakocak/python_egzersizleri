#biz tanımlamasak bile otomatik olarak tanımlanan methodlar
class kitap():
    pass
kitap=kitap()##__init__methodunu çağırıyor
print(kitap)
# len(kitap) len methodunu çağırıyor ama hata verir nasıl çağıracağını bilmediği için hata verir
del kitap #del methodunu çağırıyor  ve kitap objesini siler

class Kitap():
    def __init__(self,isim,yazar,sayfa_sayisi,turu):
        print("init fonksiyonu")
        self.isim=isim
        self.yazar=yazar
        self.sayfa_sayisi=sayfa_sayisi
        self.turu=turu
    def __str__(self):
        return "isim:{} \n Yazar: {}\n Sayfa Sayısı:{}\n Türü: {}".format(self.isim,self.yazar,self.sayfa_sayisi,self.turu)

    def __len__(self):
        return self.sayfa_sayisi



kitap=Kitap("İstanbul Hatırası ","Ahmet Ümit", 561,"Polisiye")
print(kitap)
len(kitap)