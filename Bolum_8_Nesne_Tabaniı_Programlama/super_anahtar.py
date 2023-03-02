#super en genel anlamıyla mirası alt sınıflarda kullanma anlamına gelir
class Calisan():
    def __init__(self,isim,maas,departman):
        print("Çalışan sınıfının init fonsiyonu")
        self.isim=isim
        self.maas=maas
        self.departman=departman


    def bilgileri_goster(self):
        print("Çalışan sınıfının bilgileri....")

        print("İsim: {}\n Soyaisim: {} \n Maas: {}\n Departman: {}".format(self.isim,self.soyisim,self.maas,self.departman))
    def departman_degistir(self,yeni_departman):
        self.departman=yeni_departman

class Yonetici(Calisan):
    def __init__(self,isim,maas,departman,kisi_sayisi):
        super().__init__(isim,maas,departman)
        #super anahtarını kullanarak miras aldığımız calisanlardaki isim maas departman özelliklerini tekrarlamamak için super anahtar kullanılır.

        print("Yönetici sınıfının init fonksiyonu")


        self.kisi_sayisi=kisi_sayisi

    def bilgileri_goster(self):
        print("Yönetici sınıfının bilgileri...")
        print("İsim: {} \n Maaş: {}\n Departman:{}\n Kişi Sayısı:{}".format(self.isim,self.maas,self.departman,self.kisi_sayisi))

    def zam_yap(self,zam_miktar):
        self.maas+=zam_miktar

yonetici= Yonetici("Ege Koçak",50000,"IT",12)
yonetici.bilgileri_goster()