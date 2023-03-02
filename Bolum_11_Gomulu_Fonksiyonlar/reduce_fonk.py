#reduce değer aldığı soldan başlayaraklistenin ilk 2 elemanına uygulanır. daha sonra 3. elemanına uygulanır bu şekilde devam eder

from functools import reduce
def toplam (x,y):
    return x+y

print(reduce(toplam,[12,15,16]))

print(reduce(lambda x,y : x*y , [1,2,3,4,5]))
#5'in faktöriyelini bulmuş olduk

def mak(x,y):
    if(x>y):
        return x
    else:
        return y
print(mak(5,7))
print(reduce(mak,[1,200,4,567]))