import random
again = 'y'
locRow = random.randint(1, 4)
locCol = random.randint(1, 4)
while again == 'y' or again == 'Y':
    print('The treasure map consists of a grid of four rows and four columns')
    guessRow = int( input('Enter a row:'))
    guessCol = int(input('Enter a column:'))
    print(guessRow, guessCol)
    if guessRow == locRow and guessCol == locCol:
        print("You've found the treasure.")
        break
    elif guessRow == locRow:
        print('Right row, wrong column. Try again.')
    elif guessCol == locCol:
        print('Right column, wrong row. Try again')
    else:
        print('Nowhere near. Try again.')
    again = input('Do you wanna try again?: ')