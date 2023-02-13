def asal(sayi):
    if(sayi==1):
        return False
    elif (sayi==2):
        return True
    else:
        for i in range(2,sayi):
            if(sayi%i==0):
                return False
            else:
                return True

while True:
    sayi=input("Sayi:")
    if(sayi=="q"):
        break
    else:
        sayi=int(sayi)
        if(asal(sayi)):
            print(sayi,"asal sayıdır")
        else:
            print(sayi,"asal sayı değildir")

