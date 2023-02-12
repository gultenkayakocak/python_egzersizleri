print("""
************************
Hesap Makinesi Programı
İşlemler;

1.Toplama İşlemi
2.Çıkarma işlemi
3.Çarpma İşlemi
4.Bölme İşlmei
************************
""")
a=int(input("Birinci sayıyı giriniz:"))
b=int(input("İkinci sayıyı giriniz:"))
islem=input("İşlemi giriniz:")

if(islem=="1"):
    print("{}, ile {}'in toplamı {} dir".format (a,b,a+b))
elif(islem=="2"):
    print("{}, ile {}'in toplamı {} dir".format (a,b,a-b))
elif(islem=="3"):
    print("{}, ile {}'in toplamı {} dir".format (a,b,a*b))
elif(islem=="4"):
    print("{}, ile {}'in toplamı {} dir".format (a,b,a/b))
else:
    print("Geçersiz İşlem")