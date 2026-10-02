#Classes have the ability to combine data and functionality.
#Attributes refer to variables declared in a class.
#Behaviors are associated with the methods in the class.

#everything in python is an object or derived from the object class.

class MyClass:
    a = 5
    #print("Hello") 

    def hello(self):
        print("hello")


myc = MyClass()  #this is an instance of the class.
print(myc.a)  #this is how you access the attribute of the class.
print(myc.hello())

#I used the same name for the class and it's object but the object name can be anything you want it to be. 
#For example, if i could change the object name to myc, it will execute the same as before. Everything you type is part of the instantiation process in python which involves three key steps: 
#1. class definition
#2. creating a new instance of the class
#3. initializing the new instance

#There is a third type of object called the method object, which you can use to call a method whenever it's needed.
#Classes mainly perform two kinds of operations: attribute references and instantiation. 

#First, i create a variable a for the class object and assign it a value of five. 
#Tp print out this value, i first need to refer to the class.
#Under the instance object, i print out MyClass.a.

#What happens when you reference a instance object?
#when i replace MyClass with myc.a, i got 5, which shows that attribute reference still works with instance objects. 

#Creating a method inside a class. 
#create a keyword self within the parentheses of the method as defined in the class. 
#the output will be 5, hello and None. None is given because there's no return value from the given function. 