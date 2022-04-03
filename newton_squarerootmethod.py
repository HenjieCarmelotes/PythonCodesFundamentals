#Newton's Method of finding square root of a given number using estimation.
#Credits: This program is a modification from Allen Downey's book: Think Python 2 (2015).


def newton_squaremeth(square,est):
    while True:
        print (est) #this is the estimate number
        root = (est + square/est) / 2
        if root == est:
            return est
        est = root

    
print ("This program uses Newton's method to find the square root of a given number using estimation. ")
input1 = int(input("What is the number you want to know the square root of? " ))
input2 = int(input("What is your closest estimate ?"))
newton_squaremeth(input1,input2)


#This program exhibits an iterative nature of improving it.
#from the given value and its end result.
