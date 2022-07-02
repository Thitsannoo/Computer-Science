#Subprograms
def newUser():
    user1=input('Enter Username: ')
    pass1=input('Enter Password: ')
    print("New User Registered!!")

def login():
    user2 = input('Enter Username: ')
    pass2 = input('Enter Password: ')
    secpass = input('Enter Password Again: ')
    if pass2 == secpass:
        print("Successfully logged in!!")
    else:
        print("Incorrect Username or Password!!")

def changePassword():
    user3 = input('Enter Username: ')
    pass3 = input('Enter New Password to change: ')
    print('New Password Changed Successfully!')

def exit2():
    print('Exitting......')
    exit()


#Main Program
print ("1. Register as a new user")
print ("2. Login.")
print ("3. Change your password.")
print ("4. Exit.")
choice = int(input('Please select a menu option: '))
if choice == 1:
    newUser()
elif choice == 2:
    login()
elif choice == 3:
    changePassword()
elif choice == 4:
    exit2()
else:
    print('Incorrect option. Try again.')
