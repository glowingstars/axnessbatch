a={"r":20,"a":10,"v":13,"a":2,"l":1,"i":3}
x={k:(v*2) for (k,v) in a.items() if v>=10}
print(x)