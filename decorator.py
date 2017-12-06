# def hello(name="nickie"):
#     print("Hello. The function Hello() Has Been Run")
#     def greet():
#         print("this is inside the greet function")
#     def welcome():
#         print("this is inside the welcome function")
#     print(greet())
#     print(welcome())
#     print("end of the function")
#     if(name=="nickie"):
#         return greet
#     else:
#         return welcome
# # welcome()

# x=hello()
# print(x())

# def hello():
#     return "Hi Nickie!"
# def other(func):
#     print("Hello!")
#     print(func())

# other(hello)

def new_decorator(func):
    def wrap_func():
        print("BEFORE EXECUTING FUNC")
        func()
        print("AFTER EXECUTING FUNC")
    return wrap_func


@new_decorator
def func_needs_decorator():
    print("THIS FUNCTION IS IN NEED OF DECORATION!")



# x=new_decorator(func_needs_decorator)
# x()


func_needs_decorator()
