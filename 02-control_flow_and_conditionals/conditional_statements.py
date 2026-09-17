#Control flow refers to the order in which the instructions in a program are executed. 

#In Python, there are two types of control flows. 
#1. Conditional - if, else, elif(else if)
#2. Loops - for loop, while loop. 

#if - if the condition proves to be true, a function is performed. 
#else - catches anything that isn't caught by the preceding conditions.
#elif(else if) - if the previous conditions were not true, then try this condition. 

#for loop - checks for specific conditions and then repeatedly executes a block of code as long as those conditions are met. 
#while loop - repeats a specific block of code an unknown number of times until a condition is met. 

bill_total = 210

discount1 = 10
discount2 = 20

if bill_total > 100 and bill_total < 200: 
    print("Bill is greater than 100!")
    bill_total = bill_total - discount1
elif bill_total > 200:
    print("Bill is greater than 200!")
    bill_total = bill_total - discount2
else: 
    print("Bill is less than 100!")


#Outside the if statement, I'll print out what the value of the total bill is and convert int to str
print("Total bill: " + str(bill_total))


#Output: Bill is greater than 200
#Total bill: 190 

#The first condition was not met so the code went to the second condition \
# where the value of the bill total was compared to 200. 
#Since it was greater than 200, the statement 'bill is greater than 200' was printed. 

# The code proceeded past the else condition because the previous elif condition was true. 