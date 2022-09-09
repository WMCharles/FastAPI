class Person():
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname 

    def printname(self):
        print(self.firstname, self.lastname)

p1 = Person("Charles", "Wafula")
p1.printname()

# Inheritance - Is where by a class uses the properties and methods of another class
# Parent class - class whose properties and methods are used with another class, Child class.
# Here we will create a class - Student - it will inherit the properties of the previous class 

class Student(Person):
    pass

# In the event that you define __init__() function in the child function, the child will not inherit the __init__() function of the parent class
# The function overwrites __init__() function of the parent class
# However you can still inherit the __init__() function from the parent

class Student(Person):
    def __init__(self, fname, lname):

        # Keeping the __init__() function of the parent class
        Person.__init__(fname, lname)

# Person  can be replaced by super()
# You can also add other parameters in the child class once you have declared its __init__() function
# Additionally, you can also add additional methods
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationYear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "from Class of ", self.graduationYear)

champe = Student("Charles", "Wafula", 2023)
champe.welcome()
champe.printname()
