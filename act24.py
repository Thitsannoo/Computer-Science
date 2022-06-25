#save highscore
highscore = [100,200,150,300,500]
save = open('save.txt','w')
for i in range(len(highscore)):
    save.write(str(highscore[i])+',')
save.close()

#open again
data = open('save.txt','r')
score = data.read().split(',')
data.close()
print(score)