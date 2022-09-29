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
print(odd_even_filter([2, 4, 6, 8]))
print(odd_even_filter([1, 3, 5, 7, 9]))
print(odd_even_filter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))