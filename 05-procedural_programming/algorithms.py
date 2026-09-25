#An algorithms is series of steps to complete a given task or solve a problem. 
#Algorithms are used to solve a multitude of problems that range from simple to complex.


def isPalindrome(str):
    startIndex = 0
    endIndex = len(str) - 1

    for x in str:
      if str[startIndex] != str[endIndex]:
        return False
    return True

print(isPalindrome('racecar'))

#Say you want to create an algorithm to determine how many food order tickets are in the queue to the kitchen on the rail board in a restaurant. 
#f you had to do it without a computer you would just count the number of slips and get the total number of tickets. In code, it can be quite similar. 

#let T = 0

#for each ticket on rail
   #Set T = T + 1

#Return T

#The pseudocode starts at 0 and then it checks to see how many tickets are on the rail. If a ticket is found it will then increase the counter by 1. And finally, it will return the total count.
#One aspect of writing an algorithm is how efficient it is. This is referred to as optimizing the code. If I want to optimize the code above I need to look at how I can make it get to the answer faster. In the physical world, I could instead of counting one by one, count two tickets at a time. How can I represent this in my pseudocode? I just have to change the increment from 1 to 2.

#let T = 0

#for each pair of ticket on rail
    #Set T = T + 2

#Return T

#Tickets = 0

#Each pair = 1

#Increment counter by 2

#Return 2

#This code is buggy. It does not account for the single ticket on the rail and only returns 2. I can fix the code by adding a condition to handle this edge case.

  #let T = 0

  #for each pair of ticket on rail
  #Set T = T + 2
    
  #if 1 ticket remains then
    #Set T = T + 1
    
  #Return T

#Recursion refers to a method or a function that will call itself. 
#It is used to resolve problems by breaking the problem down into sub-problems.

#Divide and conquer
#This consists of two parts. The first is breaking the problem down into smaller sub-problems and the second is solving the final solution.

#Dynamic programming
#This is mainly used for optimization problems. It is similar to the divide and conquer algorithm in that it splits the problems into sub-problems  
#Dynamic programming is an algorithmic technique used mainly for optimization problems.
#It works by breaking a problem into smaller, overlapping subproblems, solving each subproblem once, and storing the results for reuse.
#This avoids repeated calculations and makes the solution more efficient. 
#wo key properties that make dynamic programming applicable are overlapping subproblems (the same smaller problems are solved multiple times) and optimal substructure (the optimal solution of the main problem can be constructed from optimal solutions of its subproblems).
#Common examples include the Fibonacci sequence, shortest path algorithms (like Bellman-Ford), and the Knapsack problem.

#Greedy algorithm
#A greedy algorithm builds up a solution piece by piece, always choosing the option that looks best at the current step. 
#It makes locally optimal choices in the hope that they lead to a globally optimal solution. Greedy algorithms are simple and efficient, but they only work correctly when the problem has the greedy-choice property (a global optimum can be reached by choosing local optima) and optimal substructure. 
#Examples include activity selection, Huffman coding, Kruskal’s and Prim’s algorithms for minimum spanning trees, and Dijkstra’s algorithm for shortest paths. 



