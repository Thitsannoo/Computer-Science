print('1.Mexico')
print('2.India')
print('3.New Zealand')
country = int(input('Choose Your Country:'))
hour = int(input('Enter Hours:'))
mins = int(input('Enter Minutes:'))

if country == 1:
    fhour = hour - 7
    fmins = mins

if country == 2:
    fhour = hour + 4
    fmins = mins + 30

if country == 3:
    fhour = hour + 11
    fmins = mins

print(fhour,"Hours",fmins,"Minutes")



