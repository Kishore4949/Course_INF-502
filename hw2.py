import math

def pythagoreanTheorem(length_a, length_b):
    # using math.sqrt function for Square root and math.pow to get element with power 2
    return math.sqrt(math.pow(length_a,2)+math.pow(length_b,2))
def list_mangler(list_in):
    # used for loop to iterate throughout the list
    for i in range(len(list_in)):
        # checking the element is even or odd
        # if the element is odd multiplying with 2
        # if it is even i am multiplying with 3
        if list_in[i]%2==0:
            list_in[i]=2*list_in[i]
        else:
            list_in[i]=3*list_in[i]
    # returning result
    return list_in

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
def odd_even_filter(numbers):
    # to store even numbers in a list,I created a new list named even
    # to store odd numbers in a list,I created a new list named odd
    even=[]
    odd=[]
    # here, used for loop to iterate throughout the numbers list
    for i in range(len(numbers)):
        # checking the each number, whether number is even or odd
        # if the number is even, it is stored in even list
        # if the number is odd, it is stored in odd list
        if numbers[i]%2==0:
            even.append(numbers[i])
        else:
            odd.append(numbers[i])
    k=[]
    # after done with the loop here i am appending in k list, odd list along with even list
    k.append(even)
    k.append(odd)
    # returning the new list
    return k

length_a=int(input("lenth of the base:"))
length_b=int(input("height of the triangle:"))
print(pythagoreanTheorem(length_a, length_b))
print(list_mangler([1, 2, 3, 4]))
print(grade_calc([100, 90, 80, 95], 2)) # drops the 2 lowest grades (80 and 90)
print(odd_even_filter([1, 2, 3, 4, 5, 6, 7, 8, 9]))


