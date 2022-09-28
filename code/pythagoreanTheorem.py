import math

def pythagoreanTheorem(length_a, length_b):
    # using math.sqrt function for Square root and math.pow to get element with power 2
    return math.sqrt(math.pow(length_a,2)+math.pow(length_b,2))

length_a=int(input("lenth of the base:"))
length_b=int(input("height of the triangle:"))
print(pythagoreanTheorem(length_a, length_b))