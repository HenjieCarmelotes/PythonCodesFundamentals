#This program is in referenced to the activities in Allen Downey's book, Think Python 2nd Edition (2015).
#Checking whether the 3 arguments can form a triangle.
#Checking and calculating whether it is a right-angled triangle or not.


import math

def is_triangle(x,y,z):
    if z > (x + y): #False when this side is much longer than the sum of the two sides.
        return "No, these values cannot form a triangle."
    else:
        return "Yes, these values can form a triangle."

def pyth_calc(x,y,z):
    res1 = x**2 + y**2 
    res2 = math.sqrt(res1) #sum of 2 squared sides.
    res3 = math.sqrt(z**2)
    if res2 == res3:
        print ('This is a right-angled triangle! a + b is', res2, 'and is equal to c which is', res3, '(Pythagorean Theorem).')
    else:
        print ('However, this is not a right-angled triangle because a + b is ', res2 ,'and is not equal to c which is ', res3, '(Pythagorean Theorem).')


def main():
    print ("This program will help you identify whether 3 given numbers can form triangles. Also, we will check if it is a right triangle or not! ")
    input1 = int(input("What is the value of the first number? "))
    input2 = int(input("What is the value of the second number? "))
    input3 = int(input("What is the value of the third number? "))
    print (is_triangle(input1,input2,input3))
    if input3 > (input1 + input2): 
        return None #stops when the condition of is_triangle has not been met.
    else:
        return pyth_calc(input1,input2,input3) #calculation continues when it is_triangle.


main()
