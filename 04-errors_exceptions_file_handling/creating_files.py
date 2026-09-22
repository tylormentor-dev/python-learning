#Files are used to permanently store data. 
#Anything stored in the variables of your code exists in random access memory or RAM. 
#Since RAM loses it's data when the computer is turned off, it's important to be able to create files for future use or as a permanent record. 

#In python, we can create files using the open function and enabling the write mode. 
try:
 with open('newfile.txt', mode='a') as file: 
    #file.write("This is the a new file created")

#when i click run, newfile.txt has been generated as a  new file. 
#The file will now display the same content - This is the a new file created

#If you choose to write multiple lines of content, you should use the writelines function
#the writelines function accepts a list.

  file.writelines(["\nThis is the a new file created", "\nAnother line is added to the file"])
except FileNotFoundError as e:
 print("Error", e)

#you add a \n for the second sentence to appear on a new line.
#whenever you run the script, it's replacing the current file.

#instead of replacing the file each time, you need to change the action of mode by replacing the w and using 'a'which stands for append.
#with open('newfile.txt', mode='a') as file:
#when i ran this in the terminal three times, the contents have been added and now has multiple lines.
#you can add \n before the first sentence
#Since i need to replace the file, i changed to the mode back to w to ensure i'm overriding the last file. 
#I want to add the file again so i change the mode back to a and run the terminal 4 times. the file now contains the new lines that are appended each time.

#The final part of the code will be to trap exceptions.
#we always deal with an exception by using the try and accept statement.

#you add the try at the top of your code and an except at the end.
#I created an error by adding sample/ for the code to read sample\newfile.txt
#output in the terminal: Error [Errno 2] No such file or directory: 'sample/newfile.txt'
