"""
birinci parametre mutlaka mantıksal değer döner(true, False)
bir fonksiyon alır ve liste gibi veri tiplerinin her bir elemanına bu fonksiyonu uygular
"""
#çift tek
print(list(filter(lambda x : x % 2 == 0,[1,2,3,4,5,6,7])))

#Asal sayılar
def asal (x):
    i=2
    if(x==1):
        return False
    elif(x==2):
        return True
    else:
        while(i<x):
            if(x%i==0):
                return False
            i+=1
            return True
print(asal(9))