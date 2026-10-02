class Recipe():
    def __new__(cls: type[Self]) -> Self:
        pass

    def __init__(self) -> None:
        pass


#New method: responsible for creating and returning a new empty object.
#To write it, i start with the def keyword, followed by double underscore new.
#The cls is not a keyword but a convention.It acts as a placeholder for passing the class as it's first argument which will be used for creating the new empty object. 

#init method: known as a constructor in other programming languages.
#It takes the objects created using the new method with other arguments to initialize the new object being created.
#this is written with def double underscore init.
#the init method takes the new object as it's first argument. The self keyword here is another convention. It has no function itself but serves as a placeholder for self-reference by the instance object.


#How to use the state of the object to your advantage: 

class Recipe():
    def __init__(self, dish, items, time) -> None:
        self.dish = self.dish
        self.items = items
        self.time = time

#check the the arguments in the initializer will match the instances.
#To do so, i add dish, items, and time after self. 

#If a restaurant chef wants information about the recipes they have been using, we can write a class that will help.

def contents(self):
    print("The " + self.dish + " has " + str(self.items) + \
            " and takes " + str(self.time) + " min to prepare.")

pizza = Recipe("Pizza", ["cheese", "bread", "tomato"], 45)
pasta = Recipe("Pasta", ["penne", "sauce"], 55)

print(pizza.items)
print(pasta.items)    
#when i run this code, i find that despite that passing the same function and variable items, the two instances produce different contents.

print(pizza.contents())

#for this to print correctly, i need to convert the self.items and self.time references to strings by appending str() to them.
#after the class setup, we'll use it to create a pizza instance. 
#45 and 55 represents the preparation time.
#after, we create a pasta object. now we have a class and two instances. 

