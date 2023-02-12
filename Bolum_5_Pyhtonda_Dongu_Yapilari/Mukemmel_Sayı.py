sayı=int(input("Sayı:"))

i=1
toplam=0
while(sayı>i):
    if(sayı%i ==0):
        toplam +=i
    i +=1
if(toplam==sayı):
    print(sayı,"Mükemmel sayıdır")
else:
    print(sayı, "Mükemmel sayı değildir")