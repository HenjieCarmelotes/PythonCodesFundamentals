#This modification is taken from Allen Downey's book: Think Python 2nd Edition (2015)
#application of recursion while identifying factorials that can be used for debugging.


def factorial_flow(num):
    indent = '>' * (4 * num)
    print (indent, 'factorial', num)
    if num == 0:
        print (indent, 'returning 1')
        return 1
    else:
        repeat = factorial_flow(num-1)
        result = num * repeat
        print (indent, 'returning', result)
        return result

def factorial_pure(n):
    if n == 0:
        return 1
    else:
        recurse = factorial_pure(n-1) #starts from n and then recurse itself until it reaches 0. then it returns all the values and its product.
        result = n * recurse
        return result

def main():
    print ('This program will help in debugging recursive calls especially factorial of a certain number. ')
    input1 = str(input('What do you want to execute? Pure factorial, Factorial flow, or Both? '))
    input2 = int(input('What is the number? '))
    if input1 ==('Pure factorial'):
        print ('The factorial of ', input2 ,' is: ', factorial_pure(input2))
    elif input1 ==('Factorial flow'):
                   return factorial_flow(input2)
    elif input1 =='Both':
        print ('The factorial of ',input2 ,' is: ', factorial_pure(input2))
        print ('[ This is the actual flow of execution which helps in debugging. ]')
        return factorial_flow(input2)
    else:
        print ('Sorry, there must be something wrong with your inputs! This program is case sensitive. Make sure you write the correct options. ')


main()
