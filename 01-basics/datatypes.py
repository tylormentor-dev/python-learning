#A data type is an attribute associated with a piece of data that tells a computer system how to interpret its value. 
#Knowing what data types to use ensures that the data is collected in the preferred format.

# -----------------------
#Python data types
#------------------------

#1. Numeric data types: int, float, complex number
#2. Sequence data types: strings, list, tuple, range
#3. Dictionary data type: dict
#4. Boolean data type: bool
#5. Set

#strings are a sequence of characters enclosed in single or double quotes.
#strings are represented by the str class in Python.
name = "Tylor"
type(name) #this will return <class 'str'>

#list are essentially arrays that hold any type inside square brackets. Lists are mutable, meaning they can be changed after creation.
example_list = [1,'Hello', 3,8, "A"]
type(example_list) #this will return <class 'list'>

#tuple are similar to lists but are immutable, meaning they cannot be changed after creation. Tuples are defined by enclosing the elements in parentheses.
example_tuple = (1, 'hello', 3, 8, "A")
print(example_tuple[1])#this will return 'hello'


#   Dictionary store data in a key value objet system.
#   Each value can be accessed directly by its key. 

ed = {'a': 22, 'b': 44.7}
#a is the key and 22 is the value.
ed['a']   #outputs 22 by accessing the key, 'a'.

#Booleans are used to check whether a condition is true or false. 
type(True) #this will return <class 'bool'>

#A set is an unordered and non-indexed collection of non-repeating values. 
example_set = {1, 'hello', 3, 8, "A"}
type(example_set) #this will return <class 'set'>

#i checked the type of the value in the example set variable by passind it a type function. 

