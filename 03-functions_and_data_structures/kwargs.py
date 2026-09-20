#*args and **kwargs allow functions to accept a unknown number of arguments.

#If you do not know how many arguments will be passed into your function, add a * before the parameter name.

#This way, the function will receive a tuple of arguments and can access the items accordingly.
#The *args parameter allows a function to accept any number of positional arguments.

#def sum_of(a, b): 
    #return a + b 

#print(sum_of(4, 5, 6)) #this will return an error, 'TypeError: sum_of() takes 2 positional arguments but 3 were given'.

def sum_of(*args):
    sum = 0 #to calculate the total sum, i'll have a variable called sum.
    for x in args: #create a for loop that loops through the argument parameters that's passed in. 
        sum += x        #add in all the values that come in as part of args, which is assigned to the x variable using += and returning the value of sum. 
    return sum

print(sum_of(4, 5, 6,)) 
#output: 15


#kwargs
def sum_of(**kwargs):
    sum = 0
    for k, v in kwargs.items():
        sum += v
    return round(sum, 2)

print(sum_of(coffee=2.99, cake=4.55, juice=2.99))

#1. change the for loop, change the argument to kwargs but adding another star. 
#2. update the variable in for loop
#3. get the key in the value, then extend the kwargs with the item's function.
#4. change the sum to add all the items that are passed through on the value, because adding the key makes no sense. 
#output: 10.53 



