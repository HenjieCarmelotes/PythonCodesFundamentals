#guess the word game.


def guess():
    while True:
        print ('The word starts with b, it gives your body energy, and it makes you healthy')
        prompt = input('What is the word? ')
        if prompt == 'banana':
            print ('Congratulations! you found the word!')
            break
        else:
            print (prompt, 'is a good guess, but its wrong! take another guess!')



guess()


#This program emphasized the break statement when you do not know when something is going to end.
