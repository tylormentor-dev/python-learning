#Imagine you are trying to come up with a name for your new dog. You're really unsure of what you'd like to call the dog, so you decide to use your Python skills to help you decide.
#You start by accessing a file with a shortlist of names you'd like to use for your new pet.
#The file is named petnames.txt, and has the following content:

#Ace
#Atlas
#Bailey
#Bear
#Blaze
#Boomer
#Buddy
#Coco
#Cooper
#Duke
#Dozer
#Echo
#Gizmo
#Harley
#Mac
#Max
#Milo
#Oscar
#Rex
#Rocky
#Rocket
#Wolfie

#Now that you have the file petnames.txt, you'd like to use this file inside your Python program to randomly pick a single pet name.

#To do this, you'll need to have a Python file into which you'll be importing the petnames.txt file, as follows:
f = open("petnames.txt", "r")

#The open() function reads in a file outside of the program itself.
#The open() function accepts two parameters:
#1. The path and the filename in the form of a string.
#2. The import mode (the default being "r" - which means "read")

#In the line above, I am importing the file at the root of the project. I am only specifying the filename, without the path. I I am also using the default "r" mode to read in the file. I am saving the imported file into a variable named f.
#Next, I'm going to add another variable, f_content, and I'm assigning to it the result of reading the f file.
#On the third line, I'm printing the f_content variable.

#The print(f_content) line returns the exact content of the file, as is:

Ace
Atlas
Bailey
Bear
Blaze
Boomer
Buddy
Coco
Cooper
Duke
Dozer
Echo
Gizmo
Harley
Mac
Max
Milo
Oscar
Rex
Rocky
Rocket
Wolfie

#Now that I've confirmed that I'm successfully reading in the file, it would not be useful to keep printing out the file's contents, so I can comment out the print(f_content) line.
#Additionally, I can get the f_content variable into a list. The string "\n" is used to split the text where a new line is found.

f_content_list = f_content.split("\n")
#Now I'm ready to print the f_content_list variable, as follows:

print(f_content_list)
#This time, the output is as follows:
['Ace', 'Atlas', 'Bailey', 'Bear', 'Blaze', 'Boomer', 'Buddy', 'Coco', 'Cooper', 'Duke', 'Dozer', 'Echo', 'Gizmo', 'Harley', 'Mac', 'Max', 'Milo', 'Oscar', 'Rex', 'Rocky', 'Rocket', 'Wolfie']

#Here's my complete code up to this point, with the redundant print() calls deleted.
f = open("petnames.txt", "r")
f_content = f.read()
f_content_list = f_content.split("\n")
f.close()

#Now that I have all my potential pet names in a list, I can randomly pick a name from the f_content_list of names.
#To do this, I'll need to import the random module at the top of my code: import random
#Now I can use the random module's choice() function: random.choice().
#The choice() function accepts a sequence parameter. A list is one of its accepted values. This means that I can now add another line of code at the very bottom of my program:
print(random.choice(f_content_list))

#Running the code now will output a random pet name. The first time I ran it, I got the name "Milo", and the second time I ran it, I got the name "Dozer". It's always good to double-check your programs like this by running them multiple times as a quick way to confirm that they behave as intended.

#Here's the full code of my program now (including the commented-out lines of code):
import random
f = open("petnames.txt", "r")
f_content = f.read()
f_content_list = f_content.split("\n")
f.close()
print(random.choice(f_content_list))

#Finally, If I had multiple files in my folder, I could allow myself to pick a file from which to read in a list of names.
#Here's how that would work:

import random
f_name = input('Type the file name: ')
f = open(f_name) # "r" omitted as it's the default
f_content = f.read()
f_content_list = f_content.split("\n")
f.close()
print(random.choice(f_content_list))

#The only difference between this improvement and the previous program is that now I'm saving the f_name variable as the result of user-provided input. Once I have the f_name variable, I'm running the open() function on it and then proceeding with other steps as already explained. Finally, the file is closed with the f.close() statement. 