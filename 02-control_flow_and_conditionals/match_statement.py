#Conditional statements like if and else work well over a small number of conditions but over a large number of conditions, your code can get complex and messy. 
#We can use a match statement to achieve the same result that is much cleaner and readable. 

#You can combine several conditions by using the 'or' operator. 
#The default is essentially the final outcome if nothing is found in the case check. 

#Comparing the if and else statement with the match statement. 

http_status = 501

if http_status == 200 or http_status == 201:
    print('Success')
elif http_status == 400:
    print('Bad request')
elif http_status == 404: 
    print('Not Found')
elif http_status == 500 or http_status == 501:
    print('Server Error')
else: 
    print('Unknown')


#Match statement 
match http_status: 
    case 200 | 201:              #case is equivalent to the word if. # | is the 'or' operator.  
        print('Success')
    case 400:
        print('Bad request')
    case 404:
        print('Not found')
    case 500 | 501:
        print('Server Error')
    case _:
        print('Unknown')         #case _: is equivalent to the else statement.


#A match statement compares a value to several different conditions until one is met. 

