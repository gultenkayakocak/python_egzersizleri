def tam_bolen(sayi):
    tam_bolen=[]
    for i in range(2,sayi):
        if(sayi%i==0):
            tam_bolen.append(i)
    return tam_bolen
while True:
    sayi=input("Sayı:")
    if(sayi=="q"):
        print("Program sonlandırılıyor")
        break
    else:
        sayi=int(sayi)
        print(tam_bolen(sayi))
