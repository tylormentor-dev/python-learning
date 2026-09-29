#Processing a list with the map and filter function. 

menu = ["expresso", "mocha", "cappuccino", "latte", "cortado", "americano"]

#let's say you want to print out all coffees that start with the letter C.
#you do this my creating a function that will pass the list to compare it to the letter C.

def find_coffee(coffee):
    if coffee[0] == 'c':
        return coffee

map_coffee = map(find_coffee, menu) #define the arguments. the map function accepts two arguments. the first argument is an actual function that you use to match values based on a condition. 
      #The second argument is the articles that will passed through that function
print(map_coffee)  #in the terminal, i receive a map object as output. the next step is to iterate though the map object.
for x in map_coffee:
    print(x)  #now you get the output as a map. A list appears with a lot of values that are 'None', except for cappuccino and cortado because those are the two matches for the letter C in the function. 

#with the map function, you don't have to create a for loop to go through the list.
#the map function takes the argument as an argument and passes the menu list values into the function one by one. 

#the filter function works similar to the map function.

filter_coffee = filter(find_coffee, menu)
print(filter_coffee)
print(x)  #this time, only cappuccino and cortado are returned. 

#the map takes all objects in the list and allows you to apply a function to it. 
#the filter also allows you to in the list but takes the results and creates a new list with only the true values. 



