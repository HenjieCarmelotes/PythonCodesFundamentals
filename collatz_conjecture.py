#Collatz Conjecture
#Credits: This program takes a simple modification from Allen Downey's book, Think Python 2 (2015)

def collatz(val):
    import math
    while val != 1: #condition of this while loop
        print (val) #start by printing the input value
        if val % 2 == 0: #when even value is evaluated.
            val = math.floor(val/2)
        else:
            val = val*3 + 1 #when odd value is evaluated



print ("This program will show the sequence of numbers from collatz conjecture")
value = int(input("What is the number? "))
print ("The collatz sequence are the following: ")
collatz(value)
print (1)

#This program displays the sequence of values from Collatz Conjecture by which,
#this time has no one been able to prove or disprove whether the sequence ends for all positive integers.
#at least as of now when this program has been written.
#for example 5 has collatz sequence of: 5, 16, 8, 4, 2 (and 1 from the condition itself since 2/2 is 1).
#The expression is evaluated as follows:
#1. The given value 5 is printed, followed by executing the other expression.
#2. 5 * 3 + 1 = 16 (since its even)
#3. 16/2 = 8 (since its even)
#4. 8/2 = 4 (since its even)
#5. 4/2 = 2
#6. 2/2 = 1 (1 is actually included in the sequence, however, since 1 is the main condition the will set the program to loop, then it becomes false and stop.)
