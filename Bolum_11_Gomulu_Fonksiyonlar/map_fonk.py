def double (x):
    return x*2
map(double,[1,4,5,6,7])
print(list(map(double,[1,4,5,6,7])))


print(list(map(lambda x : x ** 2,[1,4,5,6,7])))

liste1=[1,2,3,4]
liste2=[4,5,12,45]
liste3=[9,7,5,7]
print(list(map(lambda x,y: x*y, liste1,liste2)))

print(list(map(lambda x,y,z: x*y*z, liste1,liste2,liste3)))