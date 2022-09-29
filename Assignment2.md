# Assignment 2: Python Basics

* **INDIVIDUAL ASSIGNMENT**
* **Deadline**: Sept-27th 11:59PM
* **Value**: 100 points counted towards Homework category
* 
* **How to submit**: In your GitHub repository called *INF502* (same used for the Assignment 1) create a file called *"Assignment2.md"* with the following content:
  1. The problem's specification (as provided below in this file);
  2. A solution for each problem (in Python). Use the tag ```code``` to write the code along with the explanation.
  3. Explanation about the code (comments on variables and their meanings, explanation on why you used one or another approach, logical reasoning). The explanation can be either comments inside the code or text as a response to the problem in the markdown file.
  4. Create a folder called `code` and add the Python files (.py) with the solution. Link these files in your answer for each problem.
  Please remember to check if you invited me to see your repository (do so if you did not do for Assignment 1). I will evaluate the latest commit before 11:59PM (Sept-27th)

## Problems

**1. Write a function with the following signature:** `pythagoreanTheorem(length_a, length_b)`.

The function returns the length of the hypotenuse assuming that `length_a` and `length_b` are the lengths of the two legs of a right triangle (the legs that form the triangle's right angle). Hint: the `math` module might have useful functions to use.


```
import math

def pythagoreanTheorem(length_a, length_b):
    # using math.sqrt function for Square root and math.pow to get element with power 2
    return math.sqrt(math.pow(length_a,2)+math.pow(length_b,2))
print(pythagoreanTheorem(2, 2))
2.8284271247461903
print(pythagoreanTheorem(2, 3))
3.605551275463989
```
[Link to the problem](https://github.com/Kishore4949/INF-502/blob/main/code/pythagoreanTheorem.py)

In your solution markdown, please provide: a link to the .py file, a commented code, the output of a few examples (3-4).

**2. Write a function with the following signature:** `list_mangler(list_in)`.

The function assumes that `list_in` is a list of integers, and returns a new list containing transformed elements of `list_in`. If the element is even, it's doubled. If the element is odd, it's tripled.

```
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
    
print(list_mangler([1, 2, 3, 4]))
[3, 4, 9, 8]
```
[Link to the problem](https://github.com/Kishore4949/INF-502/blob/main/code/list_mangler.py)

In your solution markdown, please provide: a link to the .py file, a commented code, the output of a few examples (3-4).

**3. Write a function with the following signature:** `grade_calc(grades_in, to_drop)`.

The function accepts a list `grades_in` containing integer grades, drops the `to_drop` lowest grades (so, for `to_drop` equal to 2, the function should drop the 2 lowest grades), calculates the average of the grades left, and returns the letter grade this average corresponds to according to the letter grade scale for this course.



```

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
print(grade_calc([100, 90, 80, 95], 2)) # drops the 2 lowest grades (80 and 90)
print(grade_calc([100, 90, 80, 95], 3))
print(grade_calc([100, 90, 80, 95, 40, 85], 2))
print(grade_calc([100, 90, 80, 95, 100,100], 2))
'A'
'A'
'A'
'A'
```
[Link to the Problem](https://github.com/Kishore4949/INF-502/blob/main/code/grade_calc.py)

In your solution markdown, please provide: a link to the .py file, a commented code, the output of a few examples (3-4).


**4. Write a function with the following signature:** `odd_even_filter(numbers)`.

The function accepts an input list of integers and returns a list with two sublists. The first sublist contains all even numbers in the input list and the second sublist contains all odd numbers.


```
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
print(odd_even_filter([1, 2, 3, 4, 5, 6, 7, 8, 9]))
[[2, 4, 6, 8], [1, 3, 5, 7, 9]]
print(odd_even_filter([3, 9, 43, 7]))
[[], [3, 9, 43, 7]]
print(odd_even_filter([71, 39, 98, 79, 5, 89, 50, 90, 2, 56]))
[[98, 50, 90, 2, 56], [71, 39, 79, 5, 89]]
```
[Link to the Problem](https://github.com/Kishore4949/INF-502/blob/main/code/odd_even_filter.py)

In your solution markdown, please provide: a link to the .py file, a commented code, the output of a few examples (3-4).
