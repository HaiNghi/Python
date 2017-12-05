def my_func(param1='default'):
    print("my first python function: {}".format(param1))

my_func()

def addNum(num1,num2):
    if(type(num1)==type(num2)==type(10)):
        return num1+num2
    else:
        return "Sorry, I need Integers!"

print(addNum("2","3"))

lis=[1,2,3,4,5]

#C1
def even_bool(num):
    return num%2==0

evens= filter (even_bool,lis) #print(list(evens))
print(filter(even_bool, lis))

#C2

print(filter(lambda num: num%2==0,lis)) #tra ve list so chan
print(map(lambda num: num**2,lis)) # tra ve list binh phuong cac phan tu
# print(reduce(lambda num,num1: num+num1,lis)) #tinh tong list


#chuoi nay la ket thuc cua chuoi kia
def end_other(a,b):
    a=a.lower()
    b=b.lower()
    # return (b.endswith(a) or a.endswith(b))
    return a[-(len(b)):]==b or a==b[-(len(a)):]
print(end_other('abc','bc'))

#neu nam trong khoang nay thi tra ve 0
def fix_code(n):
    if n in lis: #if n [1,2,3,4,5]:
        return 0
    return n
print(3)

def arrayCheck(array):
    for i in range(len(array)-2):
        if(array[i]==1) and (array[i+1]==2) and (array[i+2]==3):
            return True
    return False
test=[1,2,4,4]
print(arrayCheck(test))



