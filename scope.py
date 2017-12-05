x=25

def my_func():
    x=50
    return x
print(my_func())


name="this is a global name!"
def greet():
    name="Nickie"
    def hello():
        print("hello "+ name)
    hello()

greet()

y=50
def func(y):
    print ("y is ",y)
    y=10000
    print("local y changed to :",y)
func(y)


x=50
def func():
    global x
    x=1000

func()
print(x)
