a=[3,2,5,12,8,4,9,7,]
a.sort()
print(a)
b=[]
c=[]
for i in a:
    if(i%2==0):
        b.append(i)
    else:
        c.append(i)
print(b[-1])
print(c[-1])