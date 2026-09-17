#Strings are a sequence of characters. In Python, strings are enclosed in either single quotes (' ') or double quotes (" ").

#Single line
varA = 'Hello, World!'

#Multi line
varB = "This is to \
     big to fit \
      on a single line so \
       you multi-line it."

#when you run print(varB), all those strings will be combined and appear on one line. 

#--------------
#Reassigning a string value
#--------------

name = "Tylor"
print(name)

#reassign the value of Paul
name = "Paul"
print(name)
#the output will now be Paul instead of Tylor because we reassigned the value of the variable name to Paul.

#Each character in a string can be accessed by its index. 
name = "Tylor"
print(name[0])  # Output: T
print(name[1])  # Output: y
print(name[2])  # Output: l
print(name[3])  # Output: o
print(name[4])  # Output: r

#Checking the length of a string
name = "Tylor"
len(name)  # Output: 5

 #Concatenation of strings
 #Adding two strings together using the + operator is called concatenation.
a = "Hello"
b = "World"

print(a + " " + b)  # Output: Hello World

