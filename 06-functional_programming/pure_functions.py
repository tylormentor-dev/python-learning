#A pure function is a function that does not change or have any effect on a variable, data, list, or sets beyond it's own scope.
#A pure function cannot add something to a list or alter it in any way.
#In order to change a function to a pure function, you need to extend the function to accept a list as an argument and the item to the list without modifying the original list.
#The solution is to copy or clone the data from the original list.

#With pure functions, you always know what the outcome will be.
#Pure functions are consistent snippets of code that do exactly what they are intended to do.
#Pure functions include the ability to cache since you know the return is always going to be the same.
#Pure functions lend themselves well to a multi-threaded program.

#In multi-threaded programs, more than one process can run concurrently,which creates many threads of data. 
#Pure Functions will help prevent changes on the global scope ensuring data stays reliable.

#Not a pure function: 

my_list = [1,2,3]

def add_to_list(item): #this function will return my_list and append the new item that is being passed through. 
    return my_list.append(item)

add_to_list(4)

print(my_list)
#This function is not pure because the data has been manipulated at the global scope.

#A pure function:
#we will change the way the function is being called. 
#i need to pass in a new argument.

def add_to_list(lst, item): #change the append statement to lst
    nl = lst.copy()         #this time i create a new_list by creating a copy. in the function, i add the name of the new_list. instead of putting the past values into the lst, i'll put it into the copy.  
    nl.append(item)
    return nl

new_list = add_to_list(my_list, 4)

print(my_list)
print(new_list)
#add a simple append to my_list, which is going to take in the item variable. 
#this second print statement for new_list includes the values of 1 to 4.
#This is a pure function because it adds value to a list but it doesn't manipulate the original list outside the function.


