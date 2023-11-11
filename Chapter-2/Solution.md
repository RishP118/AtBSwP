## 1. What are the two values of the Boolean data type? How do you write them?


:  True and False. We write them as True and False.


## 2. What are the three Boolean operators?


:  or, and, not.


## 3. Write out the truth tables of each Boolean operator (that is, every possible combination of Boolean values for the operator and what they evaluate to).


:  = **OR Table**
   a. True  or True  = True        
   b. True  or False = True        
   c. False or True  = True        
   d. False or False = False       

 
   =  **AND Table**                 
   a. True  and True  = True        
   b. True  and False = False       
   c. False and True  = False       
   d. False and False = False       


   =  **NOT Table**        
   a. not True  = False          
   b. not False = True


## 4. What do the following expressions evaluate to?


:  False   
   False   
   True    
   False   
   False   
   True    

 
## 5. What are the six comparison operators?


:   > , >= , < , <= , == , != 


## 6. What is the difference between the equal to operator and the assignment operator?


: The equal to operator (==) is used to compare whether two values are the same or not and it is a comparison operator.

  While, the assignment operator (=) is used to assign a value to a variable.


## 7. Explain what a condition is and where you would use one.


:  A condition is a type of statement which is used to check whether the statement is True or False.


## 8. Identify the three blocks in this code:

: a. print('eggs')
  
  b. print('bacon')
  
  c. print('ham')

## 9. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.


spam=int(input())
if spam==1:
	print("Hello")
elif spam==2:
	print("Howdy")
else:
	print("Greetings!")


## 10. What keys can you press if your program is stuck in an infinite loop?

:  We can press Ctrl+C if you are stuck in an infinite loop.

## 11. What is the difference between break and continue?

:  Break = break is used to exiting the entire loop. 

   Continue = continue is used to stop a current iteration and goes to the next iteration.

## 12. What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?

:  range(10) prints all the numbers between 0 and 10, including 0.
   range(0,10) prints all the numbers between and including 0 and 9.
   range(0,10,1) prints all numbers between 1 and 10 with intervals of 1.

## 13. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

**for**

for i in range(1,11):
	print(i)

**while**

i=1
while i<11:
	print(i)
	i=i+1

## 14. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?

:  from spam import * bacon()

