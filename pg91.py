from statistics import mode
from statistics import median
#subprogram
def mean():
    total = 0
    for i in range(number):
        num = int(input('Enter Number: '))
        total = total + num
    mean = total/number
    print("Mean Number:",mean)

def mode2():
    data = []
    for i in range(number):
        num = int(input('Enter Number: '))
        data.append(num)
    modenum = mode(data)
    print('Mode Number:',modenum)

def medium():
    data = []
    for i in range(number):
        num = int(input('Enter Number: '))
        data.append(num)
    med = median(data)
    print('Median Number:',med)
    
#main program
number =int(input('How Many Numbers Do You Want to Input: '))
print('1.Mean')
print('2.Mode')
print('3.Median')
choice = int(input('Select a function: '))
if choice == 1:
    mean()
elif choice == 2:
    mode2()
elif choice == 3:
    medium()
else:
    print('Incorrect function. Try again.')
    