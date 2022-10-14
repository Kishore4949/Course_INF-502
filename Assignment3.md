## Problem 1: Wallets

Write a Python program that request a user to provide numbers representing the value in cash for different wallets. Your program should store these values in a list. The user should be able to add as many values as they want. One example of a filled `wallets` list (in this example, with 5 wallets) would be:

```
print(wallets)

Output: [1023, 984, 192, 1842, 12]
```

After the user adds the values for the wallets, your application should provide the following information:
* The fattest wallet has `$value` in it.
* The skinniest wallet has `$value` in it.
* All together, these wallets have `$value` in them.
* All together, the total value of these wallets is worth `$value` dimes.

Please try to think about different functions to complete your work.
  
 ```
# Each number is seperated by ",".
# Example:
# input is: 1,2,3,4,5,6
def fattest(list1):
    return max(list1)

def skinniest(list1):
    return min(list1)

def totalvalue(list1):
    return sum(list1)

def dimes(list1):
    return sum(list1)*10


given_list=list(map(int,input().split(",")))
print("fattest value in wallet is",fattest(given_list))
print("skinniest value in wallet is",skinniest(given_list))
print("Total value of the given wallet is: ",sum(given_list))
print("The total value of these wallets in dimes is: ",sum(given_list)*10)
 ```
## Outputs
### inputs are splitting with ","

input: 1023,984,192,1842,12

fattest value in wallet is 1842

skinniest value in wallet is 12

Total value of the given wallet is:  4053

The total value of these wallets in dimes is:  40530

input: 1,2,3,4,5,6,7

fattest value in wallet is 7

skinniest value in wallet is 1

Total value of the given wallet is:  28

The total value of these wallets in dimes is:  280



[Link to the problem](https://github.com/Kishore4949/INF-502/blob/main/Assignment3/wallets.py)
## Problem 2: Periodic Table 

The Periodic Table of the Elements was developed to organize information about the elements that make up the Universe.
Write a terminal application that lets you enter information about each element in the periodic table.
Make sure you include the following information:
* symbol, name, atomic number, row, and column

You must save the elements in a dictionary where the `symbol` is the key and the other attributes are nested inside `symbol`. The nested keys are `name`, `number`, `row`, `column`.

To populate your dictionary with data, provide a menu of options to the users:

1. Search the element by symbol (see all the details).
2. Search by a property (`name`, `number`, `row`, `column`) and see the values for that property for all the elements in the table.
3. Enter a new element manually (type the information for each property)
4. Change the properties of an element (by symbol)
5. Export periodic table as a JSON file
6. Load periodic table from JSON file
7. Exit the program

Make sure you do the appropriate communication with the user to get the necessary information to complete each step.
                      
```
# I am using file.json as file to load the periodic data
# name of the json file is "file"

periodic={
    "H":{
        "name":"Hydrogen",
        "number":1,
        "row":1,
        "column":1},
    "He":{
        "name":"Helium",
        "number":2,
        "row":1,
        "column":18
    }
}

def option_1(periodic):
    print("Below symbols are present in file.json")
    for i in periodic.keys():
        print(i)
def option_2(periodic):
    print(" Please select one from name, number, row and column")
    try:
        type_key = input()

        for i in periodic.keys():
            print(periodic[i][type_key])
    except KeyError:
        print("Please give name, number, row and column ")
def option_3(periodic):
    symbol = input("Enter Symbol of an elemnet: ")
    name = input("Enter name of the Element: ")
    number = input("enter a number of an elemnet: ")
    row = input("enter row number: ")
    column = input("enter column number: ")
    k = {}
    k["name"] = name
    k["number"] = number
    k["row"] = row
    k["column"] = column
    periodic[symbol] = k
    print("modified periodic data is: ", periodic)
def option_4(periodic):
    symbol = input("Please enter the symbol of an element: ")
    print("Modifying all properties of the given symbol ")
    periodic[symbol]["name"] = input("enter the name of the element: ")
    periodic[symbol]["number"] = int(input("enter the number of the element: "))
    periodic[symbol]["row"] = int(input("enter the row number: "))
    periodic[symbol]["column"] = int(input("enter the column number: "))
    print("modified periodic table is: ", periodic)


def option_5(user, periodic):
    with open(user, 'w') as f:
        f.write(str(periodic))
    print(periodic)


def option_6(user, periodic):
    try:
        with open(user, 'r') as f:
            periodic = f.read()
        periodic = eval(periodic)
        print(user + " file is Loaded Successfully ")
    except FileNotFoundError:
        print("Given " + user + " file is not found")

print('''                   ###MENU###
1.Search the element by symbol (see all the details).
2.Search by a property (name, number, row, column) and see the values for that property for all the elements in the table.
3.Enter a new element manually (type the information for each property)
4.Change the properties of an element (by symbol)
5.Export periodic table as a JSON file
6.Load periodic table from JSON file
7.Exit the program
''')
user_in=0

while user_in!=7:
    user_in = int(input("Please enter a integer: "))
    if user_in==1:
        option_1(periodic)
    if user_in==2:
        option_2(periodic)
    if user_in==3:
        option_3(periodic)
    if user_in==4:
        option_4(periodic)
    if user_in==5:
        user = input("Enter the Name of Json File: ")
        if not user.endswith('.json'):
            user += '.json'
        option_5(user,periodic)

    if user_in==6:
        user=input("Enter the Name of Json File: ")
        if not user.endswith('.json'):
            user+='.json'
        option_6(user,periodic)
    if user_in==7:
        print("Exit")
        break


```
```
#outputs

# I am using file.json file to load data.
                   ###MENU###
1.Search the element by symbol (see all the details).
2.Search by a property (name, number, row, column) and see the values for that property for all the elements in the table.
3.Enter a new element manually (type the information for each property)
4.Change the properties of an element (by symbol)
5.Export periodic table as a JSON file
6.Load periodic table from JSON file
7.Exit the program

Please enter a integer: 6
Enter the Name of Json File: 1
Given 1.json file is not found
Please enter a integer: 6
Enter the Name of Json File: file.json
file.json file is Loaded Successfully 
Please enter a integer: 1
Below symbols are present in file.json
H
He
Please enter a integer: 2
 Please select one from name, number, row and column
name
Hydrogen
Helium
Please enter a integer: 2
 Please select one from name, number, row and column
number
1
2
Please enter a integer: 2
 Please select one from name, number, row and column
row
1
1
Please enter a integer: 2
 Please select one from name, number, row and column
column
1
18
Please enter a integer: 2
 Please select one from name, number, row and column
sdgh
Please give name, number, row and column 
Please enter a integer: 3
Enter Symbol of an elemnet: Li
Enter name of the Element: Lithium
enter a number of an elemnet: 3
enter row number: 2
enter column number: 1
modified periodic data is:  {'H': {'name': 'Hydrogen', 'number': 1, 'row': 1, 'column': 1}, 'He': {'name': 'Helium', 'number': 2, 'row': 1, 'column': 18}, 'Li': {'name': 'Lithium', 'number': '3', 'row': '2', 'column': '1'}}
Please enter a integer: 4
Please enter the symbol of an element: Li
Modifying all properties of the given symbol 
enter the name of the element: Lithium
enter the number of the element: 3
enter the row number: 2
enter the column number: 1
modified periodic table is:  {'H': {'name': 'Hydrogen', 'number': 1, 'row': 1, 'column': 1}, 'He': {'name': 'Helium', 'number': 2, 'row': 1, 'column': 18}, 'Li': {'name': 'Lithium', 'number': 3, 'row': 2, 'column': 1}}
Please enter a integer: 5
Enter the Name of Json File: file
{'H': {'name': 'Hydrogen', 'number': 1, 'row': 1, 'column': 1}, 'He': {'name': 'Helium', 'number': 2, 'row': 1, 'column': 18}, 'Li': {'name': 'Lithium', 'number': 3, 'row': 2, 'column': 1}}
Please enter a integer: 6
Enter the Name of Json File: file
file.json file is Loaded Successfully 
Please enter a integer: 7
Exit
```
[Link to the Problem](https://github.com/Kishore4949/INF-502/blob/main/Assignment3/periodic_table.py)
