""""
2. dereceden bir bilinmeyenli denklemin köklerini bulma
Deklem: ax^2 +bc+clickDeltayı Hesaplama: b**2 - 4*a*click
1. kök:  (-b-delta**0.5 /(2*a))
2.kök:  (-b +delta**0.5 /(2*a))
"""

a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))

delta=b**2-4*a*c
x1=  (-b - delta **0.5) /(2*a)
x2=  (-b + delta **0.5) /(2*a)
print("Birinci Kök: {}\n İkinci Kök: {}\n".format(x1,x2))
