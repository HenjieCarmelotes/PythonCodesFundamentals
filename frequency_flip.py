#this program can flip the given frequency from numbers to letters
#Credits: This program is a modification taken from Allen Downey's book: Think Python 2


def frequency(string):
    """This function acts like a counter of character
in a given inputs."""
    dictionary = {} #initialize the counting as empty.
    for char in string: #evaluating each character in given string
        if char in dictionary:
            dictionary[char] += 1 #evaluates and add the character everytime it encounters it in dictionary.
        else:
            dictionary[char] =1 #evaluates and return 1 since it is unique.
    return dictionary

#you need the frequency function to run the flip function since the string indices must be integers.

def flip_dictionary(string):  
    flip = {} #initialize the counting as empty.
    for char in string: #char gets key from d
        value = string[char] #value gets value from preceeding statement.
        if value in flip:
            flip[value].append(char) #appending it since it occurs more than nth times already.
        else: 
            flip[value] = [char] #creates a new item and initialize it with singleton.
    return flip




print("This program can count each number of occurence in the given word/s." )
input1 = str(input("Input the text you want me to count: "))
print ("This is the frequency of your input. ")
print (frequency(input1))
print ("This is the flipped value and letters. ")
print(flip_dictionary(frequency(input1)))
