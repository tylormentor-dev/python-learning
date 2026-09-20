#A data structure allows you to organize and arrange your data to perform operations on them.
#Python has the following built-in data structures: List, dictionary, tuple and set.
#These are all considered non-primitive data structures, meaning they are classed as objects.

#Along with the built-in data structures, Python allows users to create their own.
#Data structures such as Stacks, Queues and Trees can all be created by the user. 

#Each data structure can be designed to solve a particular problem or optimize a current solution to make it much more performant.

#Mutability and Immutability

#Data Structures can be mutable or immutable.
# what is mutability? Mutability refers to data inside the data structure that can be modified.
# you can either change, update, or delete the data when needed. A list is an example of a mutable data structure.

#The opposite of mutable is immutable.
#An immutable data structure will not allow modification once the data has been set.
# The tuple is an example of an immutable data structure.


# LIST
#A list is a dynamic array that can hold any datatype.
#List are always based on an index. 
#A nested list :
list1 = [1,[2,3,4], 5, 6 ]

#To print out a list, it can be done in a couple of ways. 

list2 = [1, 2, 3, 4, 5, 6]
print(*list2) #the star sign 

print(list2, sep = " ") #use the print statement type, put in a seperator  

#Using the insert function
list1.insert(len(list1, 7))    #it looks for the index of where to insert to. i used the len() function to the length of list1 and put in what the next value should be. 
print(list1, sep = " ")        #adds 7 to the list.


#The append function 
#Instead of having to specify the index, or where the items should be placed, i can just put in the append keyword. 
list1.append(7)  

#The extend function
#adding one or more functions to the list
list2 = ([7, 8, 9, 10])

#To remove a something a list, we have different options we can use. 
#using pop:

list1.pop(4) #specify the index or location which item i want to remove. 
#the fifth number will be removed

#using del 
del list1[2]

#One of the main reasons we use lists is to iterate through the values and gain access to large amounts of data. 
#To iterate, i can use a for loop. 

for x in list1:
    print('Value:', x) #this will print out all the values in the list. 


#TUPLES
#Tuples can be used to store different types of data. 
#They're used as data structures and help to create solid, well performing code. 

#To declare a tuple, i declare a simple variable. 
my_tuple = (1, 'string', 4.5, True)  #to declare the tuple itself, i use parentheses.
print(my_tuple[1])

#A tuple can accept any mix of data types.
#to access any of items in the list, you can use an index. 
#you can use the 'type' function to determine the type of tuple. 

print(type(my_tuple))

#Tuples also provide a method of 'count' and index. 
print(my_tuple.count('strings'))   #count looks for the number of occurrences of the value within the tuple.

#the index method would give me back the index of where the value lies in the tuple. 

print(my_tuple.index('4.5'))

#You can also do a loop on a tuple, that is, iterate through values and print them out. 

for x in my_tuple():
    print(x)

#all the values in the tuple will be printed. 
#the one key difference of a tuple over a list is that tuple values called called immutable, which means that they cannot be changed. 

my_tuple[0] = 5 
#in the terminal, you'll receive an error stating that 'tuple object does not support item assignment'

#SETS
#Sets help with storing certain types of data in different types of formats. 

set_a = {1, 2, 3, 4, 5} #using curly braces to define the set itself.
set_a.add(6) 
set_a.remove(2)   #set_a.discard(2) also removes a value from the list. 
  
print(set_a)

#sets do not allow duplicate values. 
#sets also have methods that you can use, like adding new content. 

#mathematical operators. 
set_b = {5, 6, 7, 8, 9, 10} #for a union join, it joins two sets together minus the duplicate values.

print(set_a.union(set_b))

print(set_a.intersection(set_b)) #intersection gives you the items that match in both set a and set b. 
#you use the ampersand '&' as well instead of the wor intersection. 
print(set_a & set_b)

print(set_a.difference.set_b)
#'difference gives you all the elements that are only in set_a and not in set_b. 
#you can also represent difference by the minus symbol.
print(set_a - set_b)

print(set_a.symmetric_difference(set_b))
#when you click run, you'll get back 12346789 and 10, becuase it shows you all the elemts present in set_a or set_b but not in both sets. 
#symmetric difference can also be represented by the carrot operator. '^'

print(set_a ^ set_b)

#A set is a collection with no duplicares but it's also a collection of unaltered items. 



