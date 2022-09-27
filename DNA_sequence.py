def remove1(k1,k2,t,m):
    for i in range(m[t]+1):
        k1.insert(0,"-")
        k2.append("-")
    print(k1)
    print(k2)
    print("max macthing of the sequence is: ", t)
def remove2(k1,k2,t,m):
    for i in range(m[t]+1):
        k1.append("-")
        k2.insert(0,"-")
    print(k1)
    print(k2)
    print("max macthing of the sequence is: ",t)
def DNA(x,y,z):
    count=0
    k={}
    for i in range(len(x)):
        if x[i]==y[i]:
            count+=1
    k[z]=count
    return k
with open('fileinput1.txt') as f:
    contents = f.read()
    list1=list(map(str,contents.split(" ")))
with open('fileinput2.txt') as f:
    contents = f.read()
    list2=list(map(str,contents.split(" ")))


print(list1)
print(list2)
#list2=list(map(str,input().split()))
target=int(input("maximum shifts:"))
list3=[i for i in list1]
list4=[i for i in list2]
list5=[i for i in list1]
list6=[i for i in list2]
first={}
second={}
m={}
m1={}
for i in range(target):
    list1.insert(0,"-")
    list2.append("-")
    first.update(DNA(list1,list2,i))
    list4.insert(0, "-")
    list3.append("-")
    second.update(DNA(list4,list3,i))
o=list(first.values())
p=list(first.keys())
o1=list(second.values())
p1=list(second.keys())
m[max(o)]=p[o.index(max(o))]
m1[max(o1)]=p1[o1.index(max(o1))]
m.update(m1)
t=max(m.keys())

if list(m.keys()).index(t) == 0:
    remove1(list5,list6,t,m)
else:
    remove2(list5,list6,t,m)