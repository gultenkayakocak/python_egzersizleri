#Python Armstrong Sayısı Bulma - Başka Bir Kod

sayi = int(input("Sayıyı Giriniz:"))
basamak = str(sayi)

toplam=0

for x in basamak:

    rakam = int(x)**len(basamak)
    toplam += rakam

if(sayi == toplam):
    print("Bu Bir Armstrong Sayısıdır.")
else:
    print("Armstong Sayısı Degildir.")