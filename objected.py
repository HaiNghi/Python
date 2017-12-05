# class Person():
#     species="mamal"
#     def __init__(self,yell):
#         self.yell=yell
        
# iam=Person("ah")
# Person.species="Monkey"
# print(Person.species)

# test = ['abc', 'abc']
# print('.'.join(test))


# class MyClassOne:
#     def __init__(self):
#         self.country = "Spain"
#         self.city = "Barcelona"
#         self.things = []


# class MyClassTwo:
#     country = "Spain"
#     city = "Barcelona"
#     things = []

# def information(obj):
#     print "I'm from {0}, ({1}). I own: {2}".format(
#     obj.city, obj.country, ','.join(obj.things))


# # foo1 = MyClassOne()
# # bar1 = MyClassOne()

# foo1 = MyClassTwo()
# bar1 = MyClassTwo()

# foo1.city = "Milan"
# foo1.country = "Italy"
# foo1.things.append("Something")

# information(bar1)

#Circle

# class Circle():
#     pi=3.14
#     def __init__(self,radius):
#         self.radius=radius
#     def  area (self):
#         return Circle.pi*self.radius*self.radius

#     def set_new_r(self,new_r):
#         self.radius=new_r

# myCircle= Circle(3)
# myCircle.set_new_r(4)
# print(myCircle.area())

#inheritance
# class Animal():
#     def __init__(self):
#         print("ANIMAL CREATED")
#     def whoAmI(self):
#         print("ANIMAL")
#     def eat(self):
#         print("EATING")

# class Dog(Animal):
#     def __init__(self):
#         print("DOG CREATED")

# mydog= Dog()
# mydog.eat()
# mydog.whoAmI()

class Book():
    def __init__(self,title,author,page):
        self.title=title
        self.author=author
        self.page=page
    def __str__(self):
        return "title: {}, author: {}, page:{} ".format(self.title,self.author,self.page)

    def __len__(self):
        return self.page

    def __del__(self):
        print "This is destroyed!"

b=Book("abc","bce",200)
# print(len(b))

del b