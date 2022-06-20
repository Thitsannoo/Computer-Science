myfile=open('color.txt','w')
myfile.write('Hello')
myfile.write('\nStudents')
myfile.close()

myfile=open('color.txt','r')
print(myfile.read())