list = [10,20,30,40,50,60,70,80,90,100]
list.sort()
print(list)
key = int(input('Enter Search Key: '))
start = 0
end = len(list)-1
found = False

while(start<=end and found==False):
    mid = (start+end)//2
    if key==list[mid]:
        found = True

    elif key < list[mid]:
        end = mid -1

    elif key > list[mid]:
        start = mid+1

if found == True:
    print('Key is found!')
else:
    print('Key is not found!')