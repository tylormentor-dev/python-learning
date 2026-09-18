#A python function is a modular piece of code that can be re-used repeatedly.
#At the most basic level, you can think of functions as a set of instructions that take an input and return an output. 
#The primary task of a function is to print a value. 
#The value is printed to the screen and it's passed as an argument. 

#The string 'hello world' is the value passed into the print function.

#A function is declared using the 'def' keyword, followed by the name and task to complete.

#Optional parameters can also be added (<params>) after the function name, within a pair of parentheses. 

#def sum(x, y):
    #return x + y

bill = 175.00

tax_rate = 15  #percentage tax rate that will be applied to the bill. 

total_tax = (bill * tax_rate) / 100.00  #here, you'll calculate the amount of tax for the bill. Multiple by 100 to get a dollar amount 
print('Total tax', total_tax)

#The bill value will be different for each customer and the tax rates may also change so we'll use a resusable function so that we don't have to update each variable every time. 

def calculate_tax(bill, tax_rate):  #With functions, you can pass an argument to make it more dynamic. So i'll take in the bill, which will be the total value of the bill itself and a tax_rate. 
    return (bill * tax_rate) / 100.00

print('Total Tax:', calculate_tax(175.00, 15))



