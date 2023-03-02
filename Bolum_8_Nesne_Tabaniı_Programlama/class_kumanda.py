import random
import time
class kumanda():

    def __init__(self,tv_durum="Kapalı",tv_ses=0,kanal_listesi = ["Trt"],kanal="Trt"):
        self.tv_durum=tv_durum
        self.tv_ses=tv_ses
        self.kanal_listesi=kanal_listesi
        self.kanal=kanal
    def tv_ac(self):
        if(self.tv_durum=="Açık"):
            print("Tv zaten açık")
        else:
            print("Tv açılıyor...")
            self.tv_durum="Açık"

    def tv_kapat(self):
        if (self.tv_durum == "Kapalı"):
            print("Tv zaten kapalı")
        else:
            print("Tv kapanıyor...")
            self.tv_durum = "Kapak"
    def ses_ayar():
        while True:
            cevap=input("Ses azalt: '>'\n Sesi Artır: '>' \n Çıkış: çıkış")
            if(cevap=='<'):
                if(self.tv_ses!=0):

                    self.tv_ses-=1
                    print("Ses:", self.tv_ses)
                elif(cevap=='>'):
                    if(self.tv_ses!=0):

                        self.tv_ses+=1
                        print("Ses:", self.tv_ses)
                else:
                    print("Ses Güncellendi:",self.tv_ses)
                    break
            def kanal_ekle(self,kanal_isim):
                print("Kanal ekleniyor..")
                time.sleep(1)

                self.kanal_listesi.append(kanal_isim)
                print("Kanal eklendi....")




