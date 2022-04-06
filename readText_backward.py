#Program that displays the given string backwards.

def backward_string(s):
    """Function that can read text backward"""
    length = len(s) #evaluates the length of the string.
    index = 0 #condition that is True at the beginnning.
    while index < length:
        last = s[length-1] #access the last index of the string (character - 1)
        print(last, end = '') #prints the return value into one line.
        length = length - 1 #updates the length while in the loop until it becomes false.


print ("This program can print text in backward form. ")
input1 = str(input("What is the word/words you want to be printed backward? "))
print ("This is the backward form of your input." )
backward_string(input1)
