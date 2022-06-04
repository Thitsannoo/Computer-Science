fruit=["apple","grapes","banana","mango","orange"]
stationary=[]
number=[]
for i in range(len(fruit)):
    print(fruit[i])

for j in range(5):
    sta=input("Enter Stationary: ")
    stationary.append(sta)

for k in range(len(stationary)):
    print(stationary[k])

num = int(input('Enter Number: '))
i = 0
while(num!=-1):
    number.append(num)
    num=int(input('Enter Number: '))

for i in range(len(number)):
    print(number[i])
