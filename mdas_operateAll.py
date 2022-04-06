#Evaluate all the items using MDAS operation.

def multiply_all(*prod):
    product = 1 #intiates the multplication base of n * 1
    for n in prod: #access all the items in the list.
        product *= n #multiply the first index to the initiator 1 and use the result to continue to the next index.
    return product #returns the product of all values.


def add_all(*tot):
    total = 0 #intiates the addition base of n + 0
    for n in tot: #access all the items in the list.
        total += n #add the first index to the initiator 0 and use the result to continue to the next index.
    return total #returns the product of all values.


def subtract_all(*diff): 
    item_1 = diff[0] #intiates the subtraction starting from the first item in the list. (minuend)
    item_2 = diff[1:] #subtrahend reference.
    for n in item_2: #access all the items in the subtrahend.
        item_1 -= n #minuend - subtrahend
    return item_1 #returns the product of all values.

def divide_all(*quot):
    item_1 = quot[0] #initiates the division starting from the first item. (dividend)
    item_2 = quot[1:] #divisor reference
    for n in item_2: #access all the items in the divisor.
        item_1 /= n #dividend - divisor
    return item_1 #returns the quotient of all the values.





print ("Welcome to the program that can operate all the values in one go! ")
print ("All the given values will be operated with a single operation from the first item until the last one. Use comma to separate the items")


