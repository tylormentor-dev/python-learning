#1. Local scope

#Local scope refers to a variable that are declared inside a function. For example, in the code below, the variable total is only available to the code within the get_total() function. Anything outside of this function will not have access to it.

def get_total(a, b):
    #local variable declared inside a function
    total = a + b;
    return total

print(get_total(5, 2))
#7

# Accessing variable outside of the function:
#print(total)
#NameError: name 'total' is not defined
#When you attempt to access total outside of the function, Python raises a NameError because the variable is out of scope.

#2. Enclosing scope

#Enclosing scope refers to a function inside another function or what is commonly called a nested function. 
#In the code below, I added a nested function called double_it to the get_total function. 

#As double_it() is inside the scope of the get_total() function, it can access the variable total declared in the enclosing function.
#However, the local variable double, defined inside double_it(), cannot be accessed from inside the get_total() function.
#The function double_it() is also called the inner function.

def get_total(a, b):
    #enclosed variable declared inside a function
    total = a + b

    def double_it():
        #local variable
        double = total * 2
        print(double)

    double_it()
    #double variable will not be accessible
    #print(double)

    return total

#3. Global scope

#Global scope is when a variable is declared outside of a function. This means it can be accessed from anywhere.
#In the code below, I added a global variable called special. This can then be accessed from both functions get_total() and double_it():

special = 5

def get_total(a, b):
    #enclosed scope variable declared inside a function
    total = a + b
    print(special)

    def double_it():
        #local variable
        double = total * 2
        print(special)

    double_it()

    return total

#The global variable special is declared outside of any function and can be accessed from any part of the program, including inside both get_total() and double_it().
#The variable total is enclosed within get_total(), and double is local to double_it().

#4. Built-in scope

#Built-in scope includes built-in functions and objects (like print(), len(), etc.), but not reserved keywords (like def, for, if, etc.).


