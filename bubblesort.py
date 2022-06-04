num=[]
n = int(input('How many numbers do you want to sort?'))
for i in range(n):
    number=int(input('Enter Number: '))
    num.append(number)
    
for i in range(len(num)):
    for j in range(len(num)-1):
        if num[j]< num [j+1]:
            temp = num[j]
            num[j]= num[j+1]
            num[j+1] = temp

for i in range (len(num)):
    print(num[i]," ",end="")