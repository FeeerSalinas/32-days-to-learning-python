def gradeControl(number):
    grade = [0] * number
    total = 0
    for i in range(number):
        grade[i] = int(input(f"Enter the {i+1} grade: "))
        total += grade[i]
    finalGrade = total/number

    return f"Your average is: {finalGrade}: "
    
number = int(input("Enter the number of grades: "))
print(gradeControl(number))
