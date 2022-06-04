f = 1
s = 1
print(f,"\t",s,end="")
for i in range(10):
    fib = f + s
    f = s
    s = fib
    print("\t",fib,end="")