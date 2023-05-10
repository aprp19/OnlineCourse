def gradingStudents(grades):
    for i in range(len(grades)):
        if grades[i] >= 38:
            if grades[i] % 5 > 2:
                grades[i] += 5 - (grades[i] % 5)
    return grades


print(gradingStudents([37,39]))
