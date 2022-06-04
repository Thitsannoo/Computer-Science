list = [3,9,13,15,21,24,27,30,36,39,42,54,69]
list.sort()
print(list)
ans = 'Yes'
while ans == 'Yes':
    key = int(input('Enter Your Search Key: '))
    start = 0 
    end = len(list)-1
    found = False

    while(start<=end and found==False):
        mid=(start+end)//2
        if key==list[mid]:
            found = True
        elif key<list[mid]:
            end = mid-1
        elif key>list[mid]:
            start = mid+1

    if found==True:
        print('Key is Found !!')
    else: print('Key is not Found !!')
    start = 0
    end = len(list)-1
    found = False
    ans = input('Do you want to find more? (Yes or No):')