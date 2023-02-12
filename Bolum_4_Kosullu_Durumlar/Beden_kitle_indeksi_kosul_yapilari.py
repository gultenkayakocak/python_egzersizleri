boy=float(input("Boyunuzu Giriniz:"))
kilo=int(input("Kilonuzu Giriniz:"))
kitle_index=kilo/(boy**2)
print("Vücut kitle indeksiniz:",kitle_index)
if(kitle_index<18.5):
    print("Zayıf")
elif(kitle_index<25):
    print("Normal")
elif(kitle_index<30):
    print("Fazla kilolu")
else:
    print("Obez")
