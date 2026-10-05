#Let’s say there are two classes, namely class A and class B. If you have to perform simple inheritance, it can be done as follows:

class A:
    pass
class B(A):
    pass

#If class A is the parent class and class B is inheriting from it, then class A is passed inside class B as a parameter. This will allow class B to directly access the attributes and methods inside class A.

#Multiple inheritance
#Here is a simple example:

# Example 1
class A:
   a = 1
   
class B:
   b = 2
   
class C(A, B):
   pass

c = C()
print(c.a, c.b)

#The output is: 1 2

#First, two classes called A and B are created and then variables a and b respectively are initialized with values. 
#A new class C is then defined and classes A and B are passed to it.
#This is how multiple inheritance is done in Python
#The order of classes is important, but not in this specific example. 
# I then instantiate an object ‘c’ of class C.
#The values of the a and b variables are printed over the object c of class C even though a and b are not present inside class C.

#Multi-level inheritance

class A:
   a = 1

class B(A):
   a = 2

class C(B):
   pass

c = C()
print(c.a)

#The output is 2 because C derives from the immediate super class of C, and that's B.
#Even though class A is the top-level base class, class C does not directly inherit from A but instead inherits the attribute a from B and B has the attribute value of its member a = 2.
#The class B is in turn a derived class of base class A.
#Class B here is an intermediate derived class.
#There are three levels of inheritance in this case, but it could be extended to many levels, though it may become impractical after a while.

#Built-in functions
#There are two built-in functions that can come in handy when trying to find the relationship between different classes and objects: issubclass() and isinstance().
#The first one, issubclass() is demonstrated below.

#issubclass(class A, class B)

#Two classes are passed as arguments to this function and a Boolean result is returned. The above example can be extended as follows. 
print(issubclass(A,B))
print(issubclass(B,A))

#The output is: 
# False
# True

#This illustrates how the child class is passed as the first argument.

#Another built-in function similar to this one is isinstance() that determines if some object is an instance of some class. So if I write:

class A:
	pass
class B(A):
	pass

b = B()
print(isinstance(b,B))
print(isinstance(b,A))

#The output that I will get is "True".

#The super() function is a built-in function that can be called inside the derived class and gives access to the methods and variables of the parent classes or sibling classes.
#Sibling classes are the classes that share the same parent class. When you call the super() function, you get an object that represents the parent class in return.

#The super() function plays an important role in multiple inheritance and helps drive the flow of the code execution. It helps in managing or determining the control of from where I can draw the values of my desired functions and variables.
#If you change anything inside the parent class, there is a direct retrieval of changes inside the derived class. This is mainly used in places where you need to initialize the functionalities present inside the parent class in the child class as well. You can then add additional code in the child class.

class Fruit():
    def __init__(self, fruit):
        print('Fruit type: ', fruit)


class FruitFlavour(Fruit):
    def __init__(self):
        super().__init__('Apple')
        print('Apple is sweet')

apple = FruitFlavour()

#The output is:
#Fruit type:  Apple
#Apple is sweet

#In the code above, if I had commented out the line for super() function, the output is: 
#Apple is sweet





