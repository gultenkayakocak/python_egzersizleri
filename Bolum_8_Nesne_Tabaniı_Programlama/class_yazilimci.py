class Yazilimci():
    def  __init__(self,isim,soyisim,numara,maas,diller):
        self.isim=isim
        self.soyisim=soyisim
        self.numara=numara
        self.maas=maas
        self.diller=diller

    def bilgileri_goster(self):
        print("""
        
        Yazılımcı objesinin özellikleri
        
        İsim: {}
        Soyisim: {}
        Numara: {}
        Maaş: {}
        Bildiği Diller: {}
        
        """.format(self.isim,self.soyisim,self.numara,self.maas,self.diller))

    def zam_yap(selfself,zam_miktari):
        print("Zam yapılıyor...")
        self.maa+=zam_miktari

    def dil_ekle(self,yeni_dil):
        print("Dil eklenyor...")
        self.diller.append(yeni_dil)

yazilimci=Yazilimci("Gülten","Kaya Koçak",12345,30000,["python","C"])
yazilimci.bilgileri_goster()
yazilimci.dil_ekle("Golang")
yazilimci.bilgileri_goster()