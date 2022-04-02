#recursive calls using fibonacci sequence.
#This is a simple modification from Allen Downey's book, Think Python 2 (2015).


def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)


def main():
    print('This program will identify the fibonacci value of a given sequence.' )
    input1= int(input('What is the number? '))
    print ('That place number',input1, ' has value of', fibonacci(input1), ' in fibonacci sequence. ')



main()
