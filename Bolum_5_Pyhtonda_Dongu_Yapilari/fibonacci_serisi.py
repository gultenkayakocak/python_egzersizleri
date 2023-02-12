a=1
b=1
fibonacci=[a,b]
for i in range(20):
    print("a:",a,"b:",b)
    a,b=b,a+b
    fibonacci.append(b)
print(fibonacci)