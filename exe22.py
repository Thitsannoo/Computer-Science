num = int(input('Enter Number:'))
max = num
min = num
sum = 0
for i in range(9):
    num = int(input('Enter Next Number:'))
    if num > max:
        max = num
    elif num < min:
        min = num
    sum = sum + num
avg = sum/10
print('Average is:',avg)
print('Maximum Number is:',max)
print('Minimum Number is:',min)