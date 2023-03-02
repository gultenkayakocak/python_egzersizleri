#her bir dosya her bir modül anlamına gelir.
import math
print(math.factorial(5))

print(math.floor(5.6)) #aşağı yuvarlama
print(math.ceil(5.6)) #yukarı yuvarlama
from math import * #math modülün içindeki tüm fonk dahil etme

def faktorial(sayi):
    print("Yeni fonksiyonum")
    faktoriyel=1
    if(sayi==0 or sayi==1):
        return 1
    else:
        while(sayi>=1):
            faktoriyel*=sayi
            sayi-=1
        return faktoriyel
print(faktorial(5))