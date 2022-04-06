#search the first occurence of character

def search(char,string):
    length = len(string)
    index = 0
    while index < length:
        if string[index] == char:
            print ("The first occurence of this letter is in the index number: " , index)
        index = index + 1
    return "Sorry we could not find any letter in the string"




print("This program will search and return the first index that occur appear in a given string. ")
input1 =str(input("What letter are you looking for? "))
input2 =str(input("Write the text you want to find the letter for. "))
search(input1,input2)
