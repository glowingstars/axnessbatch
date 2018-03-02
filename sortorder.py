l=['a','c','b','A','B','C']
v=[]
l.sort()
print(l)
for i in l:
    if i.isupper():
        for j in l:
            if j.islower():
                v.append(i)
                v.append(j)
                #l.remove(i)
                l.remove(j)
                break
print(v)
