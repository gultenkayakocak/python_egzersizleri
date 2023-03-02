#bir sınıfın özelliklerini (attribute) alma
class Calisan():
    def __init__(self,isim,soyisim,maas,departman):
        print("Çalışan sınıfının init fonsiyonu")
        self.isim=isim
        self.soyisim=soyisim
        self.maas=maas
        self.departman=departman

    def bilgileri_goster(self):
        print("Çalışan sınıfının bilgileri....")

        print("İsim: {}\n Soyaisim: {} \n Maas: {}\n Departman: {}".format(self.isim,self.soyisim,self.maas,self.departman))
    def departman_degistir(self,yeni_departman):
        self.departman=yeni_departman

class Yonetici(Calisan):
    def zam_yap(self,zam_miktar):
        self.maas+=zam_miktar

yonetici=Yonetici("Gülten","Kaya",30000,"IT")
yonetici.bilgileri_goster()
yonetici=Yonetici("Serhat","Sarı",3500,"Pazarlama")
yonetici.bilgileri_goster()
yonetici.zam_yap(3500)
yonetici.bilgileri_goster()


#overriding iptal etme
