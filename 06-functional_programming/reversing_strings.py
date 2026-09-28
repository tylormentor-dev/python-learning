#we can reverse a string by using the slice function
#a slice function always starts with the name of a string. 

# str[start:stop:step]

trial = "reversal"
new_trial = trial[::-1] #the negative value of the step parameter indicates that the string needs to be traversed from the right one index position at a time.
print(new_trial)
#the entire string is printed out from right to left.

#you can use the slice function to manipulate the same variable. 


#Using recursion
def string_reverse(str):  #this function will act as a conditional if statement
    if len(str) == 0:
        return str
    else:
        return string_reverse(str[1:]) + str[0]

str = "reverse"
#create a second variable that will store the value of the return string. 
reverse = string_reverse(str)
print(reverse)


#the else statement will be recursive. we call the slice function but with a modified string every time.

