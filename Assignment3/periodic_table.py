
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
    print("modified periodic_data data is: ", periodic)
def option_4(periodic):
    symbol = input("Please enter the symbol of an element: ")
    print("Modifying all properties of the given symbol ")
    periodic[symbol]["name"] = input("enter the name of the element: ")
    periodic[symbol]["number"] = int(input("enter the number of the element: "))
    periodic[symbol]["row"] = int(input("enter the row number: "))
    periodic[symbol]["column"] = int(input("enter the column number: "))
    print("modified periodic_data table is: ", periodic)


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
5.Export periodic_data table as a JSON file
6.Load periodic_data table from JSON file
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
