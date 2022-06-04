from unittest import result
#function
def add(num1,num2):
    result = num1 + num2
    print('Answer:',result)
def sub(num1,num2):
    result = num1 - num2
    print('Answer:',result)
def mul(num1,num2):
    result = num1 * num2
    print('Answer:',result)
def div(num1,num2):
    result = num1 / num2
    print('Answer:',result)  
ans = 'y'  
while(ans=='y' or ans=='Y'):
#display option
    print('1: Addition +')
    print('2: Subtraction -')
    print('3: Multiplication x')
    print('4: Divison /')
    print()
    option = int(input('******** Choose Option (1/2/3/4) *********'))
#validation
    while(option!=1 and option!=2 and option!=3 and option!=4):
        option = int(input('Wrong!!Enter Again: '))

#ask two numbers
    print()
    num1 = int(input('Enter First Number: '))
    num2 = int(input('Enter Second Number: '))

#addition
    if option==1:
        add(num1,num2)

#subtract
    elif option==2:
        sub(num1,num2)

#multiple
    elif option == 3:
        mul(num1,num2)

#divide
    elif option == 4:
        div(num1,num2)

#repeat again
    ans = input('Do You Want To Calculate Again?(Y/N)')