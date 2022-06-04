x = "yes"
while x == "yes" and "Yes":
 n = int(input('How Many Tickets Do You Want To Buy?'))
 while n > 25:
    print('No More Than 25 Tickets')
    n = int(input('Enter Ticket Again:'))
 if n < 10:
    cost = 20 * n
 elif n < 20:
    cost = (20 * n)-(20 * n * 0.1)
 elif n <= 25:
    cost = (20 * n)-(20 * n * 0.2)
 print('Total Cost:', cost)
 x = input('Do You Want to Buy More Tickets? Yes or No:')
    