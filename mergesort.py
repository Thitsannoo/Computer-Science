def merge_sort(num):
    if len(num)>1:
        mid = len(num)//2
        left_num=num[:mid]
        right_num=num[mid:]
        merge_sort(left_num)
        merge_sort(right_num)
        i = 0 #left
        j = 0 #right
        k = 0 #middle

        while len(left_num)>i and len(right_num)>j:
            if(left_num[i]>right_num[j]):
                num[k]=left_num[i]
                i+=1 #i=i+1
            else:
                num[k] = right_num[j]
                j+=1
            k = k+1 #k+=1
        
        while i<len(left_num):
            num[k] = left_num[i]
            i+=1
            k+=1

        while j<len(right_num):
            num[k] = right_num[j]
            j+=1
            k+=1
num = []
n = int(input('How Many Numbers?'))
for i in range(n):
    add = int(input("Enter Number:"))
    num.append(add)
merge_sort(num)
print('Sorted List: ',num)