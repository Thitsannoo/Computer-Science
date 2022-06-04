total = 0
n = int(input("How many times?: "))
for i in range(1,n+1):
    total = total + (1 / i)

print("Total is", total)