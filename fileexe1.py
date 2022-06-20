demo=open('demo.txt','r')
print(demo.read())
newfile=open('newfile.txt','w')
newfile.write(demo.read())
newfile.close()

newfile=open('newfile.txt','r')
print(newfile.read())
