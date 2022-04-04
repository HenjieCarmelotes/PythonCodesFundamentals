#random name generator using 5 stringed-charaters

pref = "bcdfghjklmnpqrstvwxyz"
def name_generator(pref,suf1, suf2):
    for c in pref:
        print (c + suf1 + suf2 )

print("Are you having a problem naming your pet? ")
print("Dont Worry, we got you!")
print("This random name generator will help you choose the name of your pet. " )
input2 = str(input("Please provide 1 vowel letter and one consonant letter in any order. "))
input3 = str(input("Please provide another 1 vowel letter and one consonant letter in any order. "))
print ("These are our suggested names of your pet. ")
name_generator(pref,input2,input3)
print ("Please run the program again in case you did not find what you want!" )
