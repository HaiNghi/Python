#!/usr/bin/python3

t=(1,2,3)
print(t[0])

x= set()
x.add(1)
x.add(2)
x.add(4)
print(x)

converted= set([1,2,3,3,3,3,3])
print(converted)


x=[1,2,3,4]
out=[]
for i in x:
    out.append(i)
print(out)

out=[num**2 for num in x]
print(out)