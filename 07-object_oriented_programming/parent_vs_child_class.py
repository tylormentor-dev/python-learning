#Inheritance is a core concept ​in object-oriented programming generally, ​and in particular, in Python, ​and it's a major part of code reusability. ​
#It specifically means that every class in Python ​inherits from a built-in base class called objects, ​which is found in built-ins dot objects. 
#a class declaration ​such as Someclass with ​empty parentheses implies some class ​with object as its arguments. ​When speaking of class derivation, ​the originating class is known as the parent class, ​super class, or base class.
#When speaking of class derivation the originating class is known as the parent class, ​super class, or base class. 


#The class which inherits from it is the child class, ​subclass, or derived class. ​Any named pairing is acceptable. ​
# ​But the important thing to know is that the child class ​extends the attributes and behaviors of its parent class.

#This allows you to do two things. ​You can add new properties to the child class and you can ​modify inherited properties in ​the child class without affecting the parents. 

#Parent Class 
class P:
    def __init__(self):
        self.a =7 

class C(P):
    pass

c = C() #Instance of the child class
print(c.a)

#7

#Here you have a parent class P, ​which holds the variable a with a value of seven. 
#Then there is the empty child class C, ​in which class P is passed as an argument.
#Finally, a c represents an instance of child class ​C. If you write a print statement ​for c.a and run the code, ​the output is seven.
#Even though C itself is empty, ​it still holds the attributes inherited from P. Keep in ​mind that any changes in ​the parent class will also affect any child classes. 

class Employees:
    def __init__(self, name, last) -> None:
        self.name = name 
        self.last = last

class Supervisors(Employees):
    def __init__(self, name, last, password) -> None:
        super().__init__(name, last)
        self.password = password

class Chefs(Employees):
    def leave_request(self, days):
        return "May I take a leave for " + str(days) + "days"


adrian = Supervisors("Adrian", "A", "apple")

emily = Chefs("Emily", "E")
adrian = Chefs("Juno", "J")

print(emily.leave_request(3))
print(adrian.password)
print(emily.name)

#my first step is to create a parent class called ​employees where I'll define ​two variables for first and last names.
#on a new line, ​def__init to trigger and ​select the init method suggestion.\
#For the first variable, ​I type self.name equals name on a new line, ​and for the second, I advance another line ​and type self.last equals last.

#I then add name and last to ​the init argument on line 2 after the word self. ​Next, I'll create two child classes that ​both extends the Employee class. ​The first one I create is supervisors. 
#I then need to modify the init method of ​the Supervisors class so that I can ​add another variable named password.
#I trigger and selects the init method, ​but this time, it already ​includes the name and last variables. ​By calling the Employees class, ​the super method has automatically been applied to access ​the variables there and ​initialize them within the Supervisors class.

#adding the third variable, ​password, inside of the init method. ​I then make it an instance variable with the ​line self.password equals password.
#add another child class called Chefs. 
#The purpose of the leave_request function is to return ​a line that specifies the number of days requested.

#Now that I have all the classes, I can create a few instances from these classes
#One for a supervisor and two others for chefs.






