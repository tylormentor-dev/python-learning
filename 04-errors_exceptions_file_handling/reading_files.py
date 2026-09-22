#The three functions used to read files are: read(), readline(), and readlines().

#read() - returns the entire contents of the file as a string that will contain all the characters.
#you can also pass in an integer to return only the specified number of characters in the file. 
with open('sample.txt', 'r') as file:
   print(file.read())

#readline() - returns a single line as a string
#if you have a file that contains two files, the read line function will return as the output only the first line of text.

#File content: 
#This is the first line. 
#This is the second line. 

with open('testing.txt', 'r') as file:
    print(file.readline(10))

#output: This is the first line.
#the readline function can also include an integer argument for returning specified number of characters on a single line. 
#let's say you use the same testing file, but pass an integer of 10, your output will be the first 10 characters of the first line

#readlines() - reads the entire contents of the file and then returns it in an ordered list.
#this allows you to iterate over the list or pick out specific lines based on a condition. 

#Files are stored in dictionaries and they have paths. 
#Absolute and Relative paths. 

#Absolute paths contain leading forward/, or drive label. 
#eg. /user/local/etc/somefile.txt or C:\users\system\somefile.txt.
#Absolute files contain all the information you need to locate a file, whether you are in that files directory or not. 

#Relative paths don't contain any reference to the root directory and are normally relative to the calling file. 
#it contains all the work you need in your current directory. 
#'somefile.text' or './somefile.txt

with open('sample.txt', 'r') as file:
    print(file.read(44 ))
#I can pass in a parameter to the read function which tells the function to read in the 44 characters

with open('sample.txt', 'r') as file:
    print(file.readline()) #this function will only take the very first line from the file. 

#the readlines function will return a list of lines.
#you have list so you can assign it to a variable.
data = file.readlines()
for x in data:
    print(x)

