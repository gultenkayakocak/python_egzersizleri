print("""
*****************
Kullanıcı Girişi
*****************
""")
sys_kullanıcı_adı="gkaya"
sys_paralo="12345"
giriş_hakkı=3

while True:
    kullanıcı_adı=input("Kullnıcı adınızı giriniz:")
    paralo=input("Paralo:")
    if(kullanıcı_adı!=sys_kullanıcı_adı and paralo==sys_paralo):
        print("Kullanıcı adı hatalı")
        giriş_hakkı-=1
    elif (kullanıcı_adı==sys_kullanıcı_adı and paralo!=sys_paralo):
        print("Paralo Hatalı adı hatalı")
        giriş_hakkı-=1
    elif (kullanıcı_adı!=sys_kullanıcı_adı and paralo!=sys_paralo):
        print("Paralo  ve Kullanıcı Adı Hatalı adı hatalı")
        giriş_hakkı-=1
    else:
        print("Sisteme başarıyla giriş yapıldı")
        break
    if(giriş_hakkı==0):
        print("Giriş hakkınız bitti")
        break