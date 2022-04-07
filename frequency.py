#Counting the frequency of the occurence of character.
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



print("This program can count each number of occurence in the given word/s." )
input1 = str(input("Input the text you want me to count: "))
print ("This is the frequency of your input. ")
print (frequency(input1))



