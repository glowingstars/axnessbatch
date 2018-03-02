a=int(raw_input("enter the number"))
b=int(raw_input("enter the  number"))
c=int(raw_input("enter the number"))
if(a is b or a is c or b is c):
  print("a is not valid") 
elif(a<b and a<c):
  print(" a is the smallest number")
elif(b<c and b!=c):
  print(" b is the smallest number")
else:
  print(" c is the smallest number")