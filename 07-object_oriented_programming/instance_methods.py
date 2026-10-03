#Imagine you are managing a restaurant with many employees, and you want to keep track of their payment status easily.
#Instead of writing separate notes for each employee, you create a special form (a class) called "PaySlips." 
#This form has fields like the employee's name, whether they have been paid, and the amount they should receive. Each employee gets their own copy of this form, called an "instance," where you fill in their specific details.

#Now, you also have two handy buttons (methods) on this form: one to mark the employee as paid and another to check their payment status. 
#When you press the "pay" button for one employee, it updates only their form without affecting others. 
#This way, you can quickly see who has been paid and who hasn't, without any confusion or extra work. 
#This is how instance variables (the fields) and instance methods (the buttons) work together to manage individual objects separately but using the same blueprint.

#Instance Variables and Initialization
'''A class called PaySlips is created with instance variables: name, pay status, and amount, initialized via the init method.'''

'''Each instance of the class (e.g., Nathan and Roger) holds its own unique data for these variables.'''

#Instance Methods for State Management
'''Two methods are defined: one to update the payment status (pay) and another to display the current payment status (status).'''

'''Calling the pay method on an instance changes only that instance's payment status without affecting others.'''

#Practical Application and Behavior
'''The example simulates a restaurant manager automating wage payments, reducing manual updates and communication.'''

'''When the pay method is called for Nathan, only Nathan's payment status changes, illustrating how instance methods affect individual objects independently.'''

