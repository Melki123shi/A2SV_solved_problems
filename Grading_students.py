def gradingStudents(grades):
    # Write your code here
    gra = []
    for grade in grades:
        if grade not in range(101):
            raise "this grade is not valid, please input  valid grade"
        elif grade < 38:
            gra.append(str(grade))
        elif (5-(grade%5)) < 3:
            gra.append(str(grade + (5-(grade%5))))
        else:
            gra.append(str(grade))
    return gra
    
