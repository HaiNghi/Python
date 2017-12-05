mylist=[1,2,3]
print(mylist)

list2=['abc',1,2,3,3.2,'def',[1,2,3]]
print(list2)
print(len(list2))
print(list2[1:3])
mylist.append("nickie") #them phan tu
mylist.extend(list2) # noi 2 list
# print(mylist)
item=mylist.pop()
item1=mylist.pop(0)
print(item1)
mylist.reverse() #dao list
mylist.sort() #sap xep
print(mylist)

#LIST COMPREHENSION
matrix=[[1,2,3],[4,5,6],[7,8,9]]
first_rol=[row[0] for row in matrix] 
print(first_rol)