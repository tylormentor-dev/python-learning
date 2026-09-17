#Nested loops in python is used to solve more complex problems. 
#The nested for loop is written by indentation inside the outer loop. 

#First, the outer loop will start and then step into the inner loop. 
#Then inner loop will run until it's range limit is met. 

#outer loop
for x in range(10): #The 10 indicates how many times the loop will iterate or repeat. 
    print(x)
#inner loop
for y in range(10):
    print(y)

#once the inner loop completes, it will come back to the outer loop for the iteration and then step into the inner loop again. 
#this will happen until the outer loop reaches it's limits. 

list1 = [1,2,3,4,5,6,7,8,9]
list2 = [1,2,3,4,5,6,7,8,9]

count = 0 
#outer loop
for x in list1:     #the outer loop runs a total of 9 times. 
    count += 1 
    #inner loop 
    for y in list2:  #the inner loop runs a total of 9 multiplied by 9 which 81 times. 
        count += 1                       # 9 + 81 = 90

print(count)
#the number of times the loop is run is based on the size of the list. 
