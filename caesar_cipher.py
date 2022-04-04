#Caesar Cipher
#secret Code


def caesar_cipher(s,n):
    """s for the string input and n is for the number of steps"""
    code = [] #counts and accumulates the values later
    for c in s:
        res = ord(c) + n #converts string character into numeric codes.
        res2 = chr(res) #converts numeric codes into characters.
        code.append(res2) #append all the needed characters.
    return ''.join(code) #returns the new string.


print ("This program demonstrates the 'Caesar Cypher' which is a form of encryption.")
print ("Please provide the needed inputs to run the program without error." )
input1 = str(input("Input the word or words you want to know the caesar cypher value: "))
input2 =int(input("Which the value you want your letter to move? "))
print ("The caesar cypher code of ", input1 ,"is:", caesar_cipher(input1,input2))



