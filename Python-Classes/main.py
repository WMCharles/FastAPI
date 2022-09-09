class MyClass(): # class 
    x = 10 #property

p1 = MyClass() #creating an object

print(p1.x)

## The above are classes in their simplest form
## They are not useful in real life in that form

# all classes in python have an __init__() function in them 
# the __init__() function is used to assign values to object properties
# Below is an example

# Declare class function
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

## Creating objects and assigning values to properties 
p1 = Person("Charles", 25)
print(p1.name, p1.age)

## Methods
# Object Methods are functions that belong to the object

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def SayHello(self): #method
        print("Hello " + self.name)

p1 = Person("Caren", 28)
p1.age = 26
del p1.age
print(p1.age)