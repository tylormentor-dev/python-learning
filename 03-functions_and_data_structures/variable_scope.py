#The concept of scoping in python allows for greater control over elements in your code which reduces the chances of accidental or unwanted changes. 

#The four scopes:
#Local, enclosing, global and built-in. 
#Together they referred to as LEGB

#Variables within the built-in and global scope are accessible from anywhere in the code. 

#If there's a variable 'a' in the global scope, it can be encode at a local level. 

#The purpose of a scope is to protect the variable so that it does not get changed by other parts of the code. 
#Global scpope is generally discouraged in applications because it increases the possibility of mistakes in outputs. 

#global scope

#my_global = 10

#def fn1():
    #local_v = 5
    #print('Access to global', my_global)

#fn1()

#I declared a variable called my_global and gave it a value of 10. 
#Next, i declared a function and called it fn1. 
#Inside that function i declared another variable called local_v and gave it a value of 5. 

#To show that my global variable is accessible from anywhere, i did a print statement and print out the value of the my_global variable. 
#If i want to run that function, i have to specifically call it. (fn1())

#If i try and print out the local variable outside fn1, it will return an error because it's only accessible in the local scope of the function fn1. 


#enclosing scope

#we declare a second function inside fn1, called fn2
#We then declare an enclosed variable, which we call an enclosed_v and assign it the value of 8. 
#The local v will be local to the fn2.

my_global = 10

def fn1():
    
    enclosed_v = 8
    
    def fn2():
      local_v = 5
    print('Access to global', my_global)
    print('Access to enclosed', enclosed_v)
    fn2()

fn1()

#Within fn2, i've got access to the enclosed_v, which i can demonstrate by doing another print statement printing out the enclosed_v variable. 
#To test if it works, we call the fn1 function and call our fn2 inside fn1. 

#The way scoping works is that the innermost function has access to almost everything from the outside. 
#The nested items have access to both the global and the enclosed, but from the outside, it can't be accessed from a nested or an enclosed scope, both the local and enclosed. 

#Built-in scope

#Built-in scope is referred to what's called the 'reserve keywords' such as print or dev. 
#Buit-in scope covers all the language of python, which means you can access it from the outermost scopes or the innermost scopes in the function classes.
 




