sayi_1=int(input("1.sayı:"))
sayi_2= int(input("2.sayı:"))
eb=1
def ekok(sayi_1,sayi_2,eb):

    if(sayi_1>sayi_2):
        k_sayi=sayi_2
    else:
        k_sayi=sayi_1

    for i in range(1,k_sayi+1):
        if(sayi_1 % i == 0 and sayi_2 % i == 0):
            eb=i
            i+=1
            print(eb)
    return (sayi_1*sayi_2//eb)


print("Ekok:",ekok(sayi_1,sayi_2,eb))