class House:
    '''
    This is a stub for a class representing a house that can be used to create objects and evaluate different metrics that we may require in constructing it.
    '''
    num_rooms = 5
    bathrooms = 2
    def cost_evaluation(self):
        print(self.num_rooms)
        pass
        # Functionality to calculate the costs from the area of the house

'''The code above starts with a class definition.'''
#Then you start with a multiline comment, which alternatively can also be called a docstring (''' enclosed comments ''' ).
#in the next line you have a couple of data members or attributes: num_rooms and bathrooms.
#This is then followed by a function definition, which is empty except for the pass keyword that basically signals Python to continue execution without throwing an error. 

#The code completely defines the class and functions present inside it, but it is effectively not useful unless you call or instantiate it.
#I can do this by one of the two ways: Calling the class directly instantiating an object of that class.

house = House()
print(house.num_rooms)
print(House.num_rooms)

#I can add a few lines of code that will call the variable num_rooms on the house object and the House class after we create a house object from House class.
#output:
#5
#5

house.num_rooms = 7
print(house.num_rooms)
print(House.num_rooms)

#output:
#5
#5
#7
#5

#What has happened in the code above is, an instance was created of a class called house and then modified the attribute for that instance with a value of 7. 
#It updates the value of the instance attribute, but not the class attribute.
#So the num_rooms attribute of the class remains unchanged as 5, but the instance attribute associated with house object changes to 7.

#instead of an instance attribute, you can modify the class attribute by directly calling it over the class as follows:

House.num_rooms = 7
print(house.num_rooms)
print(House.num_rooms)

#output:
#5
#5
#7
#7

#Changes to a class attribute will affect all instances of the class, as they share the same class attribute unless overridden by an instance attribute.
#the use of the keyword self  in this example. self is a convention in Python, and you can use any other word in its place.
#self here is passed inside the method cost_evaluation() as it is an instance method and facilitates the method to point to any instance of the House when that method is called. 

#It should be noted how any number of parameters can be passed to these instance methods but the first one is always the reference to the instance of that class.

class House:
    '''
    This is a stub for a class representing a house that can be used to create objects and evaluate different metrics that we may require in constructing it.
    '''
    num_rooms = 5
    bathrooms = 2

    def cost_evaluation(self, rate):
        # Functionality to calculate the costs from the area of the house
        cost = rate * self.num_rooms
        return cost

ouse = House()
print(house.num_rooms)
print(House.num_rooms)
house.num_rooms = 7
# House.num_rooms = 7
print(house.num_rooms)
print(House.num_rooms)