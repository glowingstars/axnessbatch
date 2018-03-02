import copy
a=[1,2,[6,7,8],6,7]
b=a

b.append(20)
#print(b)
#print(a)

c=copy.deepcopy(a)
del(c[2][0])
print(c)
#print(b)
print(a)