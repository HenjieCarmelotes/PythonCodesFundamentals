#fibonacci sequence using memos to reinforce normal recursion.
#This program is a modification from Allen Downey's book: Think Python 2

identified = {0:0, 1:1} #a dictionary that keeps track of the fibonacci sequence with initialization...
#the key 0 maps to value 0 and 1 to 1.

def fibonacci_memos(num):
    if num in identified: #returns the known values given num as the key.
        return identified[num] 
    else: #when not in present in the identified values, it computes and add it to the dictionary.
        result = fibonacci_memos(num-1) + fibonacci_memos(num-2) 
        identified[num] = result 
        return result

def main():
    print('This program will identify the fibonacci value of a given sequence faster than the normal recursion.' )
    input1= int(input('What is the number? '))
    print ('That place number',input1, ' has value of', fibonacci_memos(input1), ' in fibonacci sequence. ')



main()
