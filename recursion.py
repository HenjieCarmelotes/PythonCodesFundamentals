#Modified recursion example from the book of Allen Downey: Think Python Second Edition.
#Reference:
#Allen Downey (2015). Think Python 2

#Meaningful Program
#Celebrating life existence!

def countback(num):
    if num <=0:
        print ('You must have gone through a lot of difficult times, Congratulations on reaching that age!' )
    else:
        print (num)
        countback(num-1)

def display_txt(txt, num):
    if num <=0:
        print ('Saying this quote at least 3 times in a day will make you more happy! ')
    else:
        print (txt)
        display_txt(txt, num-1)



def main():
    name = input('What is your name? ')
    print ("Hey " + name+ ', nice to meet you! ' )
    subject = input ('What is your favourite subject ' + name + '? ')
    print ("Oh! I like " + subject +" too!")
    food = input ('How about your favorite food? ')
    print ('Aha! that ' + food + ' must be so yummy :)')
    motiv = input ('Please write your best motivational quote here: ' )
    repeat = 3
    age = eval (input ('That is a wonderful quote '+ name + " . I'm just curious, how old are you by the way? " ))
    print ("Excellent!, This is the sequence of the number of your years of existence here on Earth! " )
    if age >0:
        return countback(age), display_txt(motiv, repeat)

main()
