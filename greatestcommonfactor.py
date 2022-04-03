#Greatest Common Factor

def gcf(a,b):
    if b==0: #base case
        return a
    else:
        return gcf(b,a%b) #recursive case

print ("Let's find out the greatest common factor of 2 numbers. ")
input1 = int(input("What is the first number? "))
input2 = int(input("What is the second number? "))
print ("The Greatest Common Factor of",input1, 'and', input2, 'is:', gcf(input1,input2))


#this algorithm is using the Euclidian algorithm in finding the greatest common factor of a number.
#for example: a = 126 and b = 96
#firstly, the left side of expression should be a = b * quotient + remainder
#128 = 96 * 1 + 30 (How many instances does right side will become equal to the left side.)
#secondly, the left side is destroyed and replaced by the current value of b. so a = b.
#b -> a such that:
#96 = 30 * 3 remainder 6
#subsequently, the left side is always destroyed and replaced by the value of b.
#30 = 6 * 5 remainder 0
#6 = 0
#for b that will be a (b1 *b2), always take the biggest factor from the 2 number.
#when the right reaches 0, the one on the left is the gcf of the 2 numbers.
#Hence, if b==0, return a. 




 
