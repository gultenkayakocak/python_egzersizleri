print("""
**************************************
ATM Makinesine Hoş geldiniz
**************************************
İşlemler:
1. Bakiye sorgulama
2. Para Yatırma
3. Para Çekme
Programdan çıkmak için q ya basınız.
""")
bakiye=1000
while True:
    işlem=input("İşleminizi seçiniz")
    if (işlem=="q"):
        print("Yne bekleriz.")
        break
    elif (işlem=="1"):
        print("Bakiyeniz {} tl dir.".format(bakiye))

    elif (işlem == "2"):
        miktar=int(input("Miktarınızı giriniz:"))
        bakiye+=miktar
        print("Kalan bakiyeni {} tl dir".format(bakiye))

    elif (işlem == "3"):
        miktar = int(input("Miktarınızı giriniz:"))
        if (bakiye < miktar):
            print("Yeterli miktarınız yoktur")
            continue
        bakiye -= miktar
        print("Kalan bakiyeni {} tl dir".format(bakiye))
    else:
        print("İşlem Geçersiz")