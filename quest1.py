#a=[1,2,3,4,5,6,7,8,9,10]
print([(y**2 if y%2==0 else y**3) for y in range(1,100) if y%3!=0])
#print(v)