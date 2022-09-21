import math

def pythagoreanTheorem(length_a, length_b):
    return math.sqrt(math.pow(length_a,2)+math.pow(length_b,2))
def list_mangler(list_in):
    for i in range(len(list_in)):
        if list_in[i]%2==0:
            list_in[i]=2*list_in[i]
        else:
            list_in[i]=3*list_in[i]
    return list_in

def grade_calc(grades_in, to_drop):
    grades_in.sort()
    for i in range(to_drop):
        grades_in.pop(0)
    average=sum(grades_in)/len(grades_in)
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
def odd_even_filter(numbers):
    even=[]
    odd=[]
    for i in range(len(numbers)):
        if numbers[i]%2==0:
            even.append(numbers[i])
        else:
            odd.append(numbers[i])
    k=[]
    k.append(even)
    k.append(odd)
    return k

length_a=int(input("lenth of the base:"))
length_b=int(input("height of the triangle:"))
print(pythagoreanTheorem(length_a, length_b))
print(list_mangler([1, 2, 3, 4]))
print(grade_calc([100, 90, 80, 95], 2)) # drops the 2 lowest grades (80 and 90)
print(odd_even_filter([1, 2, 3, 4, 5, 6, 7, 8, 9]))


