scores = [['Thiha',15],['Thit sann oo',16],['Thit lwin oo',17],['Yethiha',18],['kyi phyu',19]]
myfile = open('scores.txt','w')
for i in range(len(scores)):
    myfile.write(scores[i][0] + ',')
    new = str(scores[i][1])
    myfile.write(new + ',')
myfile.close()

newscores=[]
myfile = open('scores.txt','r')
newscores = myfile.read().split(',')
myfile.close()

lastscores=[]
for i in range(0,len(newscores)-1,2):
    lastscores.append([newscores[i],newscores[i+1]])

print(lastscores)