firstNames = ['Ashura','Bryn','Eloise','Mei','James','Irena']
searchName = input("Enter Search Name: ")
found = False
i = 0
while found == False and i <= (len(firstNames) - 1):
    if searchName == firstNames[i]:
        found = True
    i = i + 1

if found == True:
    print(searchName,'is at position',i,'in the list')
else:
    print(searchName,'is not in the list')