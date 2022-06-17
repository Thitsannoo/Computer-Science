record=[['Night Call','Years & Years','2022','Pop'],['Greenfields','Barry Gibb','2021','Country'],['Demidevil','Ashnikko','2021','Pop'],['All Monsters Are Human','K. Michelle','2020','R&B'],['Treat Myself','Meghan Trainor','2020','Funk']]
Title = input('Enter new album name: ')
Name = input('Enter Artist Name: ')
Year = int(input('Enter Year Released: '))
Genre = input('Enter Genre: ')
new =[Title,Name,Year,Genre]
record.append(new)
for i in range(len(record)):
    print(record[i])

search=input('What do you want to search?: ')
for i in range(len(record)):
    if search == record[i][0]:
        print('The Album is found in',record[i])
        found = True
    else:
        found = False

if found == False:
    print('Album not found')



