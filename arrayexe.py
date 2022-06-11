student=[['Smith',68],['Jackson',48],['Alia',75],['David',87]]
print('***************Student Score****************')
print(student)

for i in range(len(student)):
    if student[i][1]>=50:
        print(student[i][0],student[i][1])