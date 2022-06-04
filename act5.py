age = int(input("Enter Learner's Age: "))
if age > 18:
    lesson = 20 + ((age - 18) * 2)
else:
    lesson = 20
print("Total Lessons Require:",lesson)
