def grade_calc(grades_in, to_drop):
    # first step is i am sorting the list into descending order
    grades_in.sort()
    # here iterating loop till all required minimum elements dropped
    for i in range(to_drop):
        # poping each element
        grades_in.pop(0)
    # after dropping the minimum elements, i am calculating average using sum/len formula
    average=sum(grades_in)/len(grades_in)
    # using nested if else statement for finding better grade
    if average>90:
        return "A"
    elif average > 80:
        return "B"
    elif average > 70:
        return "C"
    elif average > 60:
        return "D"
    else:
        return "F"
print(grade_calc([100, 90, 80, 95], 2))
print(grade_calc([100, 90, 80, 95], 3))
print(grade_calc([100, 90, 80, 95, 40, 85], 2))
print(grade_calc([100, 90, 80, 95, 100,100], 2))