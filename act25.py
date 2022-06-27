#save highscore
highscore = [['Arial',100],['Becky',200],['Ducky',300],['Chris',400],['Jack',500]]
save = open('save.txt','w')
for i in range(len(highscore)):
    save.write(highscore[i][0]+',')
    new = str(highscore[i][1])
    save.write(new+',')
save.close()

#open again
data = open('save.txt','r')
score = data.read().split(',')
data.close()

scores = []
for i in range(0, len(highscore) - 1, 2):
    scores.append([highscore[i],highscore[i+1]])
print(scores)