evensum = 0
oddsum = 0
n = int(input('How Many Numbers?'))
for i in range(n):
    num = int(input('Enter Number:'))
    if num % 2 == 0:
        evensum = evensum + num
    else:
        oddsum = oddsum + num

print('Even Number is:',evensum)
print('Odd Number is:', oddsum)