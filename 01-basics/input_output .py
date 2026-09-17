#The input() function is used to get data from a source of input. 
#One example is getting data that the user types into the console.

email = input("Enter your email: ")
#if you run this code, the user will be prompted to enter their email address. The input() function will then capture the user's input and store it in the variable 'email'.

#Print function is used to display the output on the console.
#It can be used to print all sorts of data and allows for complex formatting. 
#It accepts any number of arguments and can be used to print multiple items at once.  

#objects = values that are printed on screen
#sep = defines how the object is printed or separated.
#end = defines what is printed at the end of the output. 
#file = defines where the output is sent. By default, it is sent to sys.stdout (the console).
#flush = a boolean expression to flush the buffer which means to move the data to temporary storage to the computers permanent storage.

input('Please enter you name: ')
#this will prompt the user to enter their name and wait for the input. 

#If i want to get the value of the input, I'll assign a variable to the input function like this:
num = input('Please enter a number: ')
#this will prompt the user to enter a number and store the input in the variable. 

print(num)

num1 = input('Please enter the first number: ')
num2 = input('Please enter the second number: ')

print(num1 + num2) #this will concatenate the two numbers as strings, not add them as integers.
#input: 2
#input: 5
#final output will be 25

#If you want to do the arithmetic operation, you have to convert the number to an int first. 

print(int(num1) + int(num2))
#the output will now be 7 

