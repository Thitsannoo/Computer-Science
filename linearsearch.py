list = [2,4,6,8,10,12,14,16,18]
found = False
key = int(input("Enter Search Key: "))
for i in range (len(list)):
    if key == list[i]:
        found = True
        position = i

if found==True:
    print('Key is found at',position+1)
else:
    print("Key not found!!")