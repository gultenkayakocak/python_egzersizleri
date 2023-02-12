vize1=float(input("Vize1 Notunuzu giriniz:"))
vize2=float(input("Vize2 Notunuzu giriniz:"))
final=float(input("Final Notunuzu giriniz:"))

note= (vize1*0.3)+ (vize2*0.3)+(final*0.4)
if(note>=90):
    print("AA")
elif(note>=85):
    print("BA")
elif(note>=80):
    print("BB")
elif(note>=75):
    print("CB")
elif(note>=70):
    print("CC")
elif(note>=65):
    print("DC")
elif(note>=60):
    print("DD")
else:
    print("kaldınız")