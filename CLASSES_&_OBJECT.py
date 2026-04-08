# CLASSES AND OBJECT:-   
 
# Encapsulation: An act of combining properties and methods related same object is known a encapsulation.
 
# CLASS: is a way to implement encapsulation.
    # Is a description of an object.          

# Attributes: are member variables and member functions.

# OBJECT: is an instance of a class.
        # Types: 
               # 1. Class object
               # 2. Instance object
# t1 = Test()
# t2 = Test() 

# Here t1, t2 are instance object of Test class.

# NOTE: In python there is no use of {new} keyword for making object.

class Test:
    s= 22   # Class object variable
    def f1():
        print("S")

t1 = Test()
t2 = Test()

# __init__ Method: 
class Test1:
    def __init__(self,s):
        self.a = 13
        self.s = 22
        self.s= s  # here s is local variable and self.s is instance object variable.
# a and s are instance object variables.
x = Test1(13)
print(x.s)

# METHODS TYPE: 
           # STATIC
           # INSTANCE 
           # CLASS

class S:
    def f1(self):
        pass
    @staticmethod
    def f2():
        pass
    @classmethod
    def f3(cls):
        pass


# Ques: Create a class employee with attribute empid, name , salary and
#  also define methods to access properties of employee.
class Employee:
    def __init__ (self,empid = None, name = None, salary = None):
        self.empid = empid
        self.name = name 
        self.salary = salary
    def setEmpid(self,empid):
        self.empid = empid
    def setName(self,name):
        self.name = name
    def setSalary(self,salary):
        self.salary = salary
    def getEmpId(self):
        return self.empid
    def getName(self):
        return self.name
    def getSalary(self):
        return self.salary

e1 = Employee()
e2 = Employee(1,"AARAV",100000)
e1.setEmpid(2)
e1.setSalary(1000000)
e1.setName("tmatr_saabh")

print(e1.getEmpId(),e1.getName(),e1.getSalary())
print(e2.getEmpId(),e2.getName(),e2.getSalary())


         

            
        