total = 0
start = int(input("Enter Start Number: "))
end = int(input("Enter End Number: "))
for start in range(start,end+1):
    total = total + start
print(total)