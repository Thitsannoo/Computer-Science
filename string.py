string = 'Computer Science'
length = len(string)
print(length)

animalname = 'Monkey'
for i in range (0,len(animalname)):
    print(animalname[i],"   ",end="  ")

print()
print(string[2])

print()
print(string.lower())

print()
print(string.upper())

print()
substring=string[12:16]
print(substring)

print()
present = 'put' in string
print(present)

print()
pre = 'PUT' in string
print(pre)

print()
name=input('Enter your name:')
age=int(input('Enter your age'))
print('hello  '+name)
print('Your age is  ',age)