#calculating circumference using the math modules.

import math

#function that calculates radius.
def circumfr(r):
    c = 2* (math.pi * r) #use math modules to calculate circumference.
    return c


#function that calculates diameter.
def circumfd(d):
    c = d * math.pi
    return c



def circumf():
    num1 = eval(input("If the radius is given, write the radius. If not, write 0 ! ")) #eval ensures that the input is an integer.
    if isinstance(num1, str):
        print ('Sorry, please write the number in figure!')
        return None #none ensures that the error won't be printed.
    if num1 > 0:
        print ('The circumference of the circle is:', circumfr(num1))
    elif num1 == 0:
        num2 = int(input('What is the diameter? '))
        print ('The circumference of the circle is: ', circumfd(num2))
    elif num1 < 0:
        print ('Use the absolute number instead! ')
        

circumf()
