print("""
***************************
Faktöriyel Bulma
Çıkmak için q ya basınız
***************************
""")
# print(*range(2,5)) çıktı olarak 2,3,4 çıkacak bunu kullaabiliriz.
while True:
    sayi=input("Sayı:")
    if(sayi=="q"):
        print("Program sonlandırılıyor")
        break
    else:
        sayi=int(sayi)
        fak=1
        for i in range(2,sayi+1):
            print("Faktöriyel",fak,"i:", i)
            fak *= i
        print("Faktöriyel", fak)



