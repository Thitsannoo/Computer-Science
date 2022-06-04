mark1 = int(input("Enter First Mark: "))
mark2 = int(input("Enter Second Mark: "))
mark3 = int(input("Enter Third Mark: "))
if mark1 > mark2 and mark1 > mark3:
    max = mark1
elif mark2 > mark3 and mark2 > mark1:
    max = mark2
elif mark3 > mark1 and mark3 > mark2:
    max = mark3
print('The Maximum Mark is',max)