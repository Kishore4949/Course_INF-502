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