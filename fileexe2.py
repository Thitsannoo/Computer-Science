demo=open('demo.txt','r')
print('*******************Data in old file*********************')
print(demo.read())



demo=open('demo.txt','w')
demo.write('Hi everyone, I hope you are doing good.')
demo.write('\nWelcome to PythonLobby Tutorials.')
demo.write('\nLearn by code')
demo.write('\nMachine Learning')
demo.write('\nData Analysis')
demo.write('\nwww.pythonlobby.com')
demo.close()


demo=open('demo.txt','r')
line = demo.readlines()
length = len(line)
print('****************Data in new file*****************')
print(length)
for i in range(length):
    if i == 4:
        pass
    else:
        print(line[i])


