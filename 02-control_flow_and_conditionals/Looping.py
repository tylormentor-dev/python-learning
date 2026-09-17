#Looping is used to iterate through the sequence and access each item inside the sequence. 

#First you declare a variable called str
str = 'Looping'

for item in str:    # iterate
    print(item)

#A string in Python is a sequence which means you can iterate over each character in the string. 
#The variable 'item' is a placeholder that will store the current letter in the sequence (str:)

#When the code is run, the output will be the letters of the word, looping, each letter on it's own line. 


#To declare a For loop, i used the 'for' keyword. 
# I use in the keyword to specify where i want to loop over. 
# 'i' is the variable that the value goes into. 
# I add a new function called range to specify the number of items in a range. 

for i in range(10):
    print('Looping ..', i)


favorites = ['creme brulee' , 'apple pie' , 'churros' , 'Tiramisu' , 'chcocolate cake']

for item in  favorites:
    print('I like this dessert', item)

count = 0 

while count < len(favorites): #The loop will run while the count is less than the length of favorites. In other words, keep running if it's less than 5. 
       print('I like this dessert', favorites[count]) #The key difference here is that i need to use the index to access the items within the favorite array. To do this, i add count to represent the index. 
       count += 1   #The key difference here is that i need to use the index to access the items within the favorite array. To do this, i add count to represent the index. 


#it's impotant to increment count.. to match the loop statement.
#if you do not increment count, you'll end up with an infinite loop, which keeps looping until the compiler stops it from running out of memory. 



