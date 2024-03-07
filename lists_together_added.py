list1=input("1. lista: ")
list1=list1.split()
list2=input("2. lista: ")
list2=list2.split()

lists=[]
for i in list1:
    for j in list2:
        lists.append((i,j))