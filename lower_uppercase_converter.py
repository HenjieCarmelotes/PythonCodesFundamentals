#This program converts any case into a specific case (lower or upper) of characters.


def all_upper(s):
    upper = []
    for c in s:
        upper.append(c.upper())
        delimiter = '' 
        res = delimiter.join(upper) #not joining the characters will return lists of characters.
    return res


def all_lower(s):
    lower = []
    for c in s:
        lower.append(c.lower())
        delimiter = ''
        res = delimiter.join(lower)
    return res


print ("Let's convert any alphabet letters into upper or lowe case.")
input1 = str(input("Write the word or sentences you want to covert? "))
input2 = str(input("In which form you want it to be converted? lower or upper? "))
if input2 == "lower":
    print (all_lower(input1))
if input2 == "upper":
    print (all_upper(input1))

