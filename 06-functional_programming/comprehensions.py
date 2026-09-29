#Comprehensions in Python are a way to create a new sequence from an already existing sequence.

#There are four main types of comprehensions in Python: 
#List comprehension
#Dictionary comprehension
#Set comprehension 
#Generator comprehension

#LIST COMPREHENSION
#The syntax for list comprehension is:
#[ <expression> for x in <sequence> if <condition>]

data = [2,3,5,7,11,13,17,19,23,29,31]

# Ex1: List comprehension: updating the same list
data = [x+3 for x in data]
print("Updating the list: ", data)

# Ex2: List comprehension: creating a different list with updated values
new_data = [x*2 for x in data]
print("Creating new list: ", new_data)

# Ex3: With an if-condition: Multiples of four:
fourx = [x for x in new_data if x%4 == 0 ]
print("Divisible by four", fourx)

# Ex4: Alternatively, we can update the list with the if condition as well
fourxsub = [x-1 for x in new_data if x%4 == 0 ]
print("Divisible by four minus one: ", fourxsub)

# Ex5: Using range function:
nines = [x for x in range(100) if x%9 == 0]
print("Nines: ", nines)

#The output is:
#Updating the list:  [5, 6, 8, 10, 14, 16, 20, 22, 26, 32, 34]
#Creating new list:  [10, 12, 16, 20, 28, 32, 40, 44, 52, 64, 68]
#Divisible by four [12, 16, 20, 28, 32, 40, 44, 52, 64, 68]
#Divisible by four minus one:  [11, 15, 19, 27, 31, 39, 43, 51, 63, 67]
#Nines:  [0, 9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99]

#Comprehensions provide a short-hand and elegant way of updating sequences. As may be evident, the same code can be written using the conventional for loop and if else conditions.

#For instance, in the case of example 1:
# List comprehension:
data = [x+3 for x in data]

# Regular for loop:
for x in range(len(data)):
    data[x] = data[x] + 3

#DICTIONARY COMPREHENSION 
#The syntax for dictionary comprehension is:
#dict = { key:value for key, value in <sequence> if <condition> }

#Dictionary comprehension takes one or two lists as input and creates a dictionary out of it.

# Using range() function and no input list
usingrange = {x:x*2 for x in range(12)}
print("Using range(): ",usingrange)

# Lists
months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
number = [1,2,3,4,5,6,7,8,9,10,11,12]

# Using one input list
numdict = {x:x**2 for x in number}
print("Using one input list to create dict: ", numdict)

# Using two input lists
months_dict = {key:value for (key, value) in zip(number, months)}
print("Using two lists: ", months_dict)

#The output is:
#Using range():  {0: 0, 1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12, 7: 14, 8: 16, 9: 18, 10: 20, 11: 22}
#Using one input list to create dict:  {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144}
#Using two lists:  {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'June', 7: 'July', 8: 'Aug', 9: 'Sept', 10: 'Oct', 11: 'Nov', 12: 'Dec'}


#new_dict ={key:value for (key, value) in zip(list1, list2)}
#I used the zip function that combines the two lists. When the two lists are of unequal length, the length of the shorter list is the length of the dictionary.

#SET COMPREHENSION
#The set comprehension deals with the set data type and it's very similar to list comprehension. The only key difference is the use of curly brackets for sets instead of square brackets as in lists. For example:

set_a = {x for x in range(10,20) if x not in [12,14,16]}
print(set_a)

#The output is:
#{10, 11, 13, 15, 17, 18, 19}

#GENERATOR COMPREHENSION
#Generator comprehensions are also very similar to lists with the variation of using curved brackets instead of square brackets. 
#They are also more memory efficient as compared to list comprehensions. For example:

data = [2,3,5,7,11,13,17,19,23,29,31]
gen_obj = (x for x in data)
print(gen_obj)
print(type(gen_obj))
for items in gen_obj:
    print(items, end = " ")

#The output is:
#<generator object <genexpr> at 0x102a87d60> 
#<class 'generator'> 
#2 3 5 7 11 13 17 19 23 29 31

#The elements in this iterator object cannot be directly accessed and need the help of a for loop and as such, I iterate over these elements and print them.

#Here is the difference between map() function and list comprehensions:
#newdata = map(square, data)
#newdata = [x + 3 for x in data]

#both map() functions and list comprehension effectively do the same job of modifying iterator sequences such as the list.
#List comprehensions also provide direct return of a list as compared to map() function that returns a map object.
