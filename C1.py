data =[['user','email'],['John','john@gmail.com'],['Leo','leo@gmail.com']]
again = "Y"
while again == "Y":
    search = input('Enter Name to Search: ')
    for i in range(len(data)):
        if search == data[i][0]:
            print("User Found!")
            print("Email:",data[i][1])
            found = True
        else:
            found = False

    if found == False:
        print("User Not Found!")

    again = input("Do You Want To Search Again?(Y or N): ")