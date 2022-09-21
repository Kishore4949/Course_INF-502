


x=input()
y=[]
while x.isdigit()==True:
    y.append(int(x))
    x=input()
print("count:",len(y))
print("Average:",sum(y)/len(y))
print("sum:",sum(y))