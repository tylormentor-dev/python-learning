#Functional programming is particularly adept at processing large amounts of data at high speeds.

#What is the role of a function?
#functions take some input, process it and then produce some outputs. 

#There are two types of functions, traditional and pure. 
#Pure functions will always do the same thing and return the same results no matter how many times they are called. 
#There are several differences between traditional and pure: 
#Traditional functions can access and modify variables on the global state, but pure functions cannot, both traditional functions and pure functions can access variables in the local state. 

#Traditional functions can change args, whereas pure functions cannot.
#The outputs of traditional functions does not depend on inputs. However, the output of pure functions does depend on input. 

#Functional programming in essence is a programming paradigm that utilizes functions for clean, consistent and maintainable code. 
#Functional programming differs from Object orientated programming by design. 
#the data outside the scope of the function does not change. This simply means that the function should avoid modifying the input data or arguments being passed, instead it should only return the completed result of the intended function being called. 

#Functions are considered standalone or independent and this aids the clean and elegant nature of the code.
#The language itself needs to allow function to be passed as an argument and also return a function to it's caller. 

#In python function are what is known as first class citizens, which essentially means they have the same level of strings and numbers, they can be assigned to a variable, passed as an argument or returned to it's caller.
#One of pythons function is a sorted function that accepts a list of items and returns that list in a sorted order. 

