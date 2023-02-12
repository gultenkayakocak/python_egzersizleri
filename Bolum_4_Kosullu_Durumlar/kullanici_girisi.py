print("""
***************************
Kullanıcı Girişi
***********************
""")
sys_kullaniciadi="gkaya"
sys_paralo="12345"

kullanıcı_adi=input("Kullanıcı adını giriniz:")
paralo=input("Paralonuzu giriniz")

if(kullanıcı_adi==sys_kullaniciadi and sys_paralo!=paralo):
    print("Paroloa hatalı")
elif(kullanıcı_adi!=sys_kullaniciadi and sys_paralo==paralo):
    print("Kullanıcı adı hatalı")
elif(kullanıcı_adi!=sys_kullaniciadi and sys_paralo!=paralo):
    print("Bilgileriniz hatalı")
else:
    print("Girişiniz başarılı")