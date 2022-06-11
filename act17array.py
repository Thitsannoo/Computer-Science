marks=[[80,59,34,89],[31,11,47,64],[29,56,13,91],[55,61,48,0],[75,78,81,91]]
highest=0
lowest=0
total=0
count=0
for i in range(len(marks)):
    print(marks[i])

for i in range(len(marks)):
    for j in range(4):
        total= total + marks[i][j]
        count = count + 1
        if marks[i][j]>highest:
            highest=marks[i][j]
        elif marks[i][j]<lowest:
            lowest=marks[i][j]

print('Highest Marks: ',highest)
print('Lowest Marks: ',lowest)
print('Average Marks: ', total/count)