#break hiçbir koşula bağlı oladan durmasını sağlar
#break sadece ve sedace içinde bulunduğu döngüyü sonlandırır.

i=0
while(i<10):
    if(i==5):
        break
    print(i)
    i+=1


liste=[1,2,3,4,5]
for i in liste:
    if(i==3):
        break
    print("i",i)

while True: #sonsuza kadar döngü var demek
    isim=input("İsminizi girin (çıkmak için q ya basın)")
    if(isim=="q"):
        print("Programdan çıkılıyor")
        break
    print("isminiz:",isim)


