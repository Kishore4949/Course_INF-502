# Programming Assignment 1
### file input is seperated characters with space
### Here I am taking .txt file as extension.
### input is A G T A G T A

```python
def remove1(k1,k2,t,m):
    # here k1 is first sequence
    # k2 is second sequence
    # t is max key of m
    # m is dict
    for i in range(m[t]+1):# adding "-" beging and ending of the sequences
        k1.insert(0,"-")
        k2.append("-")
    # printing sequence1 and sequence2
    s=""
    s1=""
    for i in range(len(k1)):
        s+=k1[i]
        s1+=k2[i]
    print("sequence 1 is: ",s)
    print("sequence 2 is: ",s1)
    print("max macthing of the sequence is: ", t)

# remove2 is function same as remove1
def remove2(k1,k2,t,m):
    for i in range(m[t]+1):
        k1.append("-")
        k2.insert(0,"-")
    s = ""
    s1 = ""
    for i in range(len(k1)):
        s += k1[i]
        s1 += k2[i]
    print("sequence 1 is: ", s)
    print("sequence 2 is: ", s1)
    print("max macthing of the sequence is: ",t)
def DNA(x,y,z):
    count=0 # intially count is 0
    k={}

    # iterating for loop throughout the sequence
    # checking letters are same or not, by using if statement

    for i in range(len(x)-1):
        if x[i]==y[i]:
            count+=1 # if two elements are same count is incremented by 1
    k[z] = count
    # returning dictionary
    return k

def DNA1(x,y,z):
    count1=1
    maxim=0
    for i in range(len(x) - 1):
        if x[i] == y[i]:
            if x[i + 1] == y[i + 1]:
                count1 += 1
        if maxim < count1:
            maxim = count1
    # returning dictionary
    return maxim


# reading first sequence from fileinput1.txt
# I'm reading letters in order, separated by spaces.
# for Example:
# sequence 1: A B C D E F G H

file1=input("Please enter first sequence file name: ")
if not file1.endswith(".txt"):
    file1+=".txt"
file2=input("Please enter second sequence file name: ")
if not file2.endswith(".txt"):
    file2+=".txt"
f=None
fp=None
try:
    with open(file1) as f:
        contents = f.read()
        # sequence 1 is stored in the variable list1
        list1=list(map(str,contents.split(" ")))
    # reading second sequence from fileinput2.txt
    # I'm reading letters in order, separated by spaces.
    # for Example:
    # sequence 2: A B C D E F G H
    with open(file2) as fp:
        contents = fp.read()
        # sequence 2 is stored in the variable list2
        list2=list(map(str,contents.split(" ")))

except FileNotFoundError:
    raise FileNotFoundError("Given file is not found")

allowed = "AGCT"
if not (all(ch in allowed for ch in list1)):
    raise ValueError("file 1 should not contains other than specified character 'A' 'G' 'C' 'T'")
if not (all(ch in allowed for ch in list2)):
    raise ValueError("file 2 should not contains other than specified character 'A' 'G' 'C' 'T'")


# target variable input for storing Maximum Shifts, taking from the user
while True:
    try:
        target=int(input("Enter maximum shifts:"))
        type1 = int(input("Please enter integer 1 or 2\n"
                          " 1.number of matches \n"
                          " 2.maximum chain\n"
                          " : "))
        break
    except TypeError:
        raise TypeError("type error")
    except ValueError:
        raise ValueError("value error")

# copying sequence 1 in list3 variable
list3=[i for i in list1]
# copying sequence 2 in list4 variable
list4=[i for i in list2]
# copying sequence 1 again in list5 variable
list5=[i for i in list1]
# copying sequence 2 again in list6 variable
list6=[i for i in list2]
# after every shift result is stored in first, dictionary
# here, keys are shifts, integer
# values are score of the two sequences
# second dictionary same like first
first={}
second={}
# taking two empty dictionaries m and m1
m={}
m1={}
max_chain=[]
# iterating the loop, till maximum shifts reached
def remove4(list5, list6,max_chain):
    f = max_chain.index(max(max_chain))
    # below for loop is to add "-" starting and ending
    for i in range(f+1):
        list5.append("-")
        list6.insert(0,"-")
    i = 0
    count=0
    # below while is to check starting index of continuous char
    while i < len(list5):
        if list5[i] == list6[i]:
            count+=1
        if count == max(max_chain):
            break
        i += 1
    s = ""
    s1 = ""
    # below for loop is used to append all characters from list to a single string
    for j in range(len(list5)):
        s += list5[j]
        s1 += list6[j]
    print("two sequences of maximum chain are given below")
    print("Sequence 1 is: ",s)
    print("Sequence 2 is: ",s1)
    print("maximum contiguous chain starts from: ",i )
def remove3(list5,list6,max_chain):
    f=max_chain.index(max(max_chain))
    # below for loop is to add "-" starting and ending
    for i in range(f+1):
        list5.insert(0,"-")
        list6.append("-")
    count = 0
    # below while is to check starting index of continuous char
    while i < len(list5):
        if list5[i] == list6[i]:
            count += 1
        if count == max(max_chain):
            break
        i += 1
    s = ""
    s1 = ""
    # below for loop is used to append all characters from list to a single string
    for j in range(len(list5)):
        s += list5[j]
        s1 += list6[j]

    print("two sequences of maximum chain are given below")
    print("Sequence 1 is: ",s)
    print("Sequence 2 is: ",s1)
    print("maximum contiguous cain starts from position: ",i)



if type1==1:
    for i in range(target):
        # To ensure that two sequences are the same length, I am adding "-" at the beginning and end of sequence
        # firstly, I am inserting "-" in the beginning of the first sequence
        list1.insert(0,"-")
        # secondly, I am inserting "-" at the end of second sequence
        list2.append("-")
        # I am calling DNA function with three variables
        # sequence 1 is stored in first variable
        # Sequence 2 is stored in second variable
        # integer is stored in third variable
        # and storing in dictionary, first
        first.update(DNA(list1,list2,i))
        # Here I am inserting "-" in the beginning of the second sequence
        list4.insert(0, "-")
        # inserting "-" at the end of the sequence 1
        list3.append("-")
        # calling DNA Sequence with three variables
        # sequence 2 is stored in first variable
        # Sequence 1 is stored in second variable
        # integer is stored in third variable
        # and storing the result in dictionary, first
        second.update(DNA(list4,list3,i))
    o = list(first.values())
    # storing all keys of first as a list in p
    p = list(first.keys())
    # storing all values of second as a list in o1
    o1 = list(second.values())
    # storing all keys of second as alist in p1
    p1 = list(second.keys())
    # here I am taking maximum value of o as a key in m and maximum value of o,index of p as value
    m[max(o)] = p[o.index(max(o))]
    # same as m
    m1[max(o1)] = p1[o1.index(max(o1))]
    # storing m1 in m
    m.update(m1)
    # maximum key is stored in t
    t = max(m.keys())

    # checking t is in 0 index or at 1 index
    if list(m.keys()).index(t) == 0:
        # if t is in 0 index it goes to if part
        # calling remove1 function
        remove1(list5, list6, t, m)
    else:
        # if t is in 1 index it goes to else part
        # calling remove2 function
        remove2(list5, list6, t, m)
elif type1==2:
    for i in range(target):
        # To ensure that two sequences are the same length, I am adding "-" at the beginning and end of sequence
        # firstly, I am inserting "-" in the beginning of the first sequence
        list1.insert(0, "-")
        # secondly, I am inserting "-" at the end of second sequence
        list2.append("-")
        # I am calling DNA function with three variables
        # sequence 1 is stored in first variable
        # Sequence 2 is stored in second variable
        # integer is stored in third variable
        # and storing in dictionary, first
        max_chain.append(DNA1(list1, list2, i))
        # Here I am inserting "-" in the beginning of the second sequence
        list4.insert(0, "-")
        # inserting "-" at the end of the sequence 1
        list3.append("-")
        # calling DNA Sequence with three variables
        # sequence 2 is stored in first variable
        # Sequence 1 is stored in second variable
        # integer is stored in third variable
        # and storing the result in dictionary, first
        # calling DNA1 function
        max_chain.append(DNA1(list4, list3, i))
    # checking index of max value in max_chain is even or odd
    if max_chain.index(max(max_chain))%2==0:
        max_chain1 = []
        # appending all values with even index
        for i in range(0,len(max_chain), 2):
            max_chain1.append(max_chain[i])
        # calling remove3 function
        remove3(list5,list6,max_chain1)
    else:
        max_chain1=[]
        # appending all values withh odd index
        for i in range(1,len(max_chain),2):
            max_chain1.append(max_chain[i])
        # calling remove4 function
        remove4(list5,list6,max_chain1)
else:
    print("Please enter 1 or 2")

```
## Sample Output is given below:
```
Please enter first sequence file name: fileinput1
Please enter second sequence file name: fileinput2
Enter maximum shifts:4
Please enter integer 1 or 2
 1.number of matches 
 2.maximum chain
 : 1
sequence 1 is:  --TTAGCTCGA
sequence 2 is:  ACTGATCAC--
max macthing of the sequence is:  4

Please enter first sequence file name: fileinput1
Please enter second sequence file name: fileinput2
Enter maximum shifts:4
Please enter integer 1 or 2
 1.number of matches 
 2.maximum chain
 : 2
two sequences of maximum chain are given below
Sequence 1 is:  TTAGCTCGA---
Sequence 2 is:  ---ACTGATCAC
maximum contiguous chain starts from the index:  5
```

## Description

1. Intially I am reading input from two different files(with extension .txt) 
2. Reading the maximum shifts from user
3. After that, I present two choices.1.number of matches and 2.maximum chain. One will be selected respectively
4. I am using DNA function for number of matches 
5. In DNA function, I am using for loop to check both sequences.
6. remove1 and remove2 are two different funtions which are called, according to the index of max element in m
7. remove 1 or remove 2 function is used to print the sequence in a string
8. used DNA1 function to find the maximium continuous sequence 
9. here, used remove 3 and remove 4 functions to find the starting index of continuous sequence and printed the sequence in a string
10. finaly, if the user gives 1 for number of matches, it checks with if loop and goes for below functions:
* DNA function 
* remove 1 
* remove 2 functions
11. if the user gives 2 for maximum continuous sequence, it checks with loop and goes for below functions: 
* DNA1 function
* remove 3
* remove 4 functions
12. files used: fileinput1.txt and fileinput2.txt were used.
 
 ## Hurdles and Benefits
 
 1. while I am running the problem, I encountered different issues and errors 
 2. for Number of matches approach, some times I got list index out range error and some types type error 
 3. after debugging the solution I can understand the error and resolved it.
 4. for Maximum continuous Sequence I got different wrong outputs and it is very difficult to find the starting index of the continuous sequence.
 5. I resolved it by using while loop to find the index.
 6. below is the logic for finding starting index of continuous sequence
 ```
    count=0
    i=0
    while i < len(list5):
        if sequence1[i] == sequence2[i]:
            count+=1    
        if count == max(max_chain):
            break 
        i += 1
 ```    
    where i is starting index of the continuous sequence
  ### Benefits
  1. I got these two approaches and I can use these approaches where ever needed.
  2. I learnt different logics and functions by solving this question.

* [link to the problem](https://github.com/Kishore4949/INF-502/blob/main/DNA_sequence.py)
* [link to the file 1](https://github.com/Kishore4949/INF-502/blob/main/fileinput1.txt)
* [link to the file 2](https://github.com/Kishore4949/INF-502/blob/main/fileinput2.txt)
