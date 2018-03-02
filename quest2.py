a=[4,5,6,7,8]
b=[1,2,3]
for i in range(len(a)):
    if len(a)==len(b):
        v=[a[x]+b[x] for x in range(0,5)]
    else:
         b.append(0)
print(v)
