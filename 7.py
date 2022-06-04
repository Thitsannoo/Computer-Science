low = int(input("Enter Lowest Number: "))
high = int(input("Enter Highest Number: "))
for i in range(low,high + 1):  
   sum = 0  
   temp = i  
   while temp > 0:  
       digit = temp % 10  
       sum = sum + digit ** 3  
       temp = temp // 10  
       if i == sum:  
            print(i)  
