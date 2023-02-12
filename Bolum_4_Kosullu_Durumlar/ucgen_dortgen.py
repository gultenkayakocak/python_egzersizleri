tip=input("Üçgen mi Dörtgen mi?")
if(tip=="Üçgen"):
    a =int(input("Birinci kenarı değeri:"))
    b = int(input("İkinci kenarı değeri:"))
    c = int(input("Üçüncü kenarı değeri:"))
    if (abs(a + b) > c and abs(a + c) > b and abs(b + c) > a):
        if(a==b and b==c):
            print("Eşkenar üçgen")
        elif(a==b or b==c ):
            print("İkizkenar üçgen")
        else:
            print("Normal üçgen")
elif (tip=="Dörtgen"):
    a=float(input("Birinci kenarı değeri:"))
    b = float(input("İkinci kenarı değeri:"))
    c = float(input("Üçüncü kenarı değeri:"))
    d = float(input("Dördüncü kenarı değeri:"))
    if(a==b and b==c and c==d):
        print("Kare")
    elif(a==b or b==c or c==d):
        print("Dikdörtgen")
    else:
        print("Normal dörtgen")