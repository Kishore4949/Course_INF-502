
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
        print("Below symbols are present in file.json")
        for i in periodic.keys():
            print(i)
    if user_in==2:
        print(" Please select one from name, number, row and column")
        try:
            type_key=input()

            for i in periodic.keys():
                print(periodic[i][type_key])
        except KeyError:
            print("Please enter name, number, row and column ")

    if user_in==3:

        symbol=input("Enter Symbol of an elemnet: ")
        name=input("Enter name of the Element: ")
        number=input("enter a number of an elemnet: ")
        row=input("enter row number: ")
        column=input("enter column number: ")
        k={}
        k["name"]=name
        k["number"]=number
        k["row"]=row
        k["column"]=column
        periodic[symbol]=k
        print(periodic)
    if user_in==4:
        symbol=input("Please enter the symbol of an element: ")
        print("Modifying all properties of the given symbol ")
        periodic[symbol]["name"]=input("enter the name of the element: ")
        periodic[symbol]["number"]=int(input("enter the number of the element: "))
        periodic[symbol]["row"]=int(input("enter the row number: "))
        periodic[symbol]["column"]=int(input("enter the column number: "))
        print("modified periodic table is: ",periodic)
    if user_in==5:
        with open(user, 'w') as f:
            f.write(str(periodic))
        print(periodic)
    if user_in==6:
        user=input("Enter the Name of Json File: ")
        if not user.endswith('.json'):
            user+='.json'
        try:
            with open(user,'r') as f:
                periodic=f.read()
                periodic = eval(periodic)
                print(user+" file is Loaded Successfully ")
        except FileNotFoundError:
            print("Given "+user+" file is not found")
    if user_in==7:
        print("Exit")
        break
