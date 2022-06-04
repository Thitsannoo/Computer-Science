n = int(input("How Many Times?: "))
total = 0
for i in range(1,n+1):
    total =  total + int('2' * i)
print("Total is",total)