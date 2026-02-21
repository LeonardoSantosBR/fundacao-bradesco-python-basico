gradeOne = int(input("your first grade: "))
gradeSecond = int(input("your second grade: "))

average = (gradeOne + gradeSecond) / 2

if(average >= 6):
    print("Approved your average grade was higher or equal than 6: ", average)
else:
    print("Failed  your average grade was lower than 6: ", average)