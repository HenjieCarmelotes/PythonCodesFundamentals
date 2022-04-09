#program that implements common operation between 2 inputs.

def add(num1,num2):
    return num1 + num2 #to add 2 variables assigned

def sub(num1, num2):
    return num1 - num2 #to subtract 2 variables assigned

def mul(num1, num2):
    return num1 * num2 #to multipy 2 variables assigned

def div(num1, num2):
    return num1 / num2 #to divide 2 variables assigned

def main():
    num1 = int(input ('Display your first favourite number.'))
    num2 = int(input ('Display your second favourite number.'))
    operation = input ('What do you want to do? (add, subtract, multiply, or divide?')
    if (operation == 'add'):
        print (add(num1,num2))
    elif(operation == 'subtract'):
        print (sub(num1, num2))
    elif(operation == 'multiply'):
        print (mul(num1, num2))
    elif (operation == 'divide'):
        print (div(num1, num2))
    else:
        print ("Something is not right with your command, check if you've met the options!")



main()
