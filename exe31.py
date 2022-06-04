import random
guess = random.randint(0,20)
ans = int(input('Enter Guess Number:'))
while guess!=ans:
    if ans > guess:
        print('Too High, try again!')
    elif ans < guess:
        print('Too Low, Try Again!')
    ans = int(input('Enter Next Guess:'))
print('Congratulations!! Your Guess is Correct')