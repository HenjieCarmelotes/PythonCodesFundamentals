#This program selects lowercase and uppercase in a given string.


def select_upper(s):
    upper = [] #initializes an empty list.
    for c in s:
        if c.isupper(): #method invoked for uppercase.
            upper.append(c) #selects the uppercase and appends them together.
    return upper




def select_lower(s):
    lower = [] #initializes an empty list.
    for c in s:
        if c.islower(): #method invoked for lowercase.
            lower.append(c) #selects lowercase
    return lower




print ("Let's select any alphabet case letters in a given word/sentence.")
input1 = str(input("Write the word or sentences you want to select the case? "))
input2 = str(input("In which case you want it to see? lower or upper? "))
if input2 == "lower":
    print (select_lower(input1))
if input2 == "upper":
    print (select_upper(input1))


