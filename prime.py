n=int(input("enter the number"))
for i in range(1,n):
    if(n%i==0):
        c=+1
if(c==2):
    print("the number is not prime")
else:
    print("the number is prime")
