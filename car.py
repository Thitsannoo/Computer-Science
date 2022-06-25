carA = ['BMW','Toyota','Audi','Renault','Rover','Mercedes']
car = open('car.txt','w')
for i in range(len(carA)):
    car.write((carA[i])+',')
car.close()

carB = []
car2 = open('car.txt','r')
carB = car2.read().split(',')
car2.close()
print(carB)
data = open('car.txt','r')
print(data.read())