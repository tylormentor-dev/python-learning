#Python has several built in functions to create and manipulate files. 
#File Handling includes opening, reading and writing files amongst other operations. 

#There are two file handling functions in python, open and close. 
#The open function is used for reading, writing and creating files. 
#The open function accepts two arguments, the first is the file name and/or the file location and the second argument is the mode.

#The mode indicates what action is required such as reading, writing or creating. 
#It also specifies if you want the file output in text or binary format. 

#MODES: 
#r - r is used open and read a file in text format.
#rb - rb opens and reads a files in binary format.
#r - opens the file for both reading and writing
#w - opens the file for writing. note, w will overwrite the existing file. 
#a - open(<FILE_NAME>, a) opens the file for editing or appending data. 
#close() - used for closing the open file connection and it does not take any arguments. 
#with open function - with open('testing.txt', 'r') as file:, closes and opens a file but the advantage of using it is that it closes the file automatically.

#The text format is more user friendly because humans can read it.
#Humans cannot read the binary format but it's much more compact and therefore result in better performance. 
#Python uses text as the default file handling. 

#To set the file handling to binary, you need to pass the letter b along with either the read or write option. 




