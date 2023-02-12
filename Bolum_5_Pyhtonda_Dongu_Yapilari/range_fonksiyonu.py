#range yapısı oluşturuyor listelere benziyor. başlangıç bitiş opsiyonel olarak artırma değeri alarak kisteye benzeyen bir sayı dizi oluşturuyor.
print(*range(0,20)) #0'dan 20 ye kadar 20 dahil değil
print(*range(0,20,2)) # artış miktarı 2 olarak
print(*range(15)) #başlangı. değeri olmadığı için 0 dan başlar.
print(*range(5,100,5))
print(*range(100,20,-5))#20'den 100 e kadar 5 atlayarak
for i in range(1,101):
    print(i)

for i in range(1,10):
    print("*"*i)
