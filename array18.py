game=[['Alexis',1,19],['Seema',1,29],['Seema',2,44],['Lois',1,10],['Alexis',2,17],['Alexis',3,36],['Dion',1,23],['Emma',1,27],['Emma',2,48]]
L1highest = 0
L1player = ''
L2highest = 0
L2player = ''
L3highest = 0
L3player = ''

for i in game:
    player = i[0]
    level =  i[1]
    score = i[2]

if level == 1 and score>L1highest:
    L1highest = score
    L1player = player
elif level == 2 and score>L2highest:
    L2highest = score
    L2player = player
elif level == 3 and score>L3highest:
    L3highest = score
    L3player = player

print('**************SCOREBOARD****************')
print('Level 1:',L1player,'with',L1highest)
print('Level 2:',L2player,'with',L2highest)
print('Level 3:',L3player,'with',L3highest)