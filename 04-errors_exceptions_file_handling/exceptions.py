#The two types of errors: 
#Syntax errors - which are caused by human error.
#Exception - known errors that need to be handled. 

#Exception errors happen during code execution and they can easily go unnoticed.
#Exception Handling: 


def divide_by(a, b):
    return a / b 

try:
    ans = divide_by(40, 0)
except Exception as e: 
    print("Something went wrong!", e)
    print(e.__class__)

#print(divide_by(40, 0))

#output: Something went wrong! division by zero


#write out a simple math function
#allow the function to accept two parameters, a and b.
#the purpose of this function to return the value of the division of both numbers. 
#inside the print statement, i add a new set of parentheses with a value of 40 and 4. 
#if you divide 40 by 0, you'll get an error because you can't divide a number by zero. 

#how can you handle errors in a user friendly way?
#you do this by using python's try and except statements. 

#the try statement will try and execute that you added inside it. 
#if an exception occurs, it will trigger the except line and execute any code underneath the except statement.

#python allows you to make the except statement more specific. 
#if you want to trap the exception itself you could add the base class exception right after the except. 
#the base class exception is used for all exceptions that are written within python. 

#you can gain access to the exception information by using the an 'as e' exception. 
#the e variable acts as an alias for the exception.
#you can use e to print out the exception in the print statement. 

#in python, you can also get access to the actual type of class or exception that's occurred. 
#to do this, you can add another print statement of e._class_  

#you can add more specific feedback to the end user by replacing the base class exception with the actual error that was printed out - ZeroDivisionError
#changing the print statement so that it first prints the actual error by adding e at the start of this statement. 


def divide_by(a, b):
    return a / b 

try:
    ans = divide_by(40, 0)
except ZeroDivisionError as e: 
    print("we cannot divide by zero")
except Exception as e:
    print(e, "something went wrong!")

#you can handle more than one exception without knowing what they are ahead of time by chaining the except statement and adding another except statement. 
#you can add another except statement that tests for a generic exception. 



    