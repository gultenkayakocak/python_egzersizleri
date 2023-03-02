class Araba():
    def __init__(self, model, renk, beygir, motor,yil):
        self.model=model
        self.renk=renk
        self.beygir=beygir
        self.motor=motor
        self.yil=yil
    def bilgileri_goster(self):
        print("*-" * 20)
        print("Araba Modeeli: ", self.model)
        print("Araba rengi: ", self.renk)
        print("Araba beygiri:: ", self.beygir)
        print("Araba motoru:", self.motor)
        print("Araba yılı:", self.yil)
        print("*-" * 20)

araba1= Araba("Opel Astra","Beyaz",110,1.6,2012)
araba1.bilgileri_goster()

