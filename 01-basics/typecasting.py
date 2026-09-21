#Type casting is the process of converting one data type to another. 
#Python has two types of conversion : 
#1. Implicit 
#2. Explicit

#Implicit is performed automatically by pythons compiler to prevent data loss. 
#Python only converts values if the data types are compatible. 

#int and float are compatible data types.
#strings are int are not compatible data types.

#Explicit is used by using python functions. 
#str(), Int(), float(). 

#str() is used convert any data type to a string.
str(11)  # Output: '11'
int('11.5')  # Output: 11
float('50.5')  # Output: 50.5

#more functions. 
ord() #returns an integer representing a unicode character. 
hex() #converts an integer to a hexadecimal string.
oct() #converts an integer to an octal number string.
