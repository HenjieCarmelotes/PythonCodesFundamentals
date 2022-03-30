#Fermat's Last theorem.
#This activity is the solution from the activity...
#taken from Allen Downey's book, Think Python 2nd Edition 2015.

def check_fermat(a,b,c,n):
    """a,b,and c are all positive integers and n is the exponent."""
    if n > 2:
        res1 = c**n
        res2 = a**n + (b**n)
        if res1 == res2:
            print ('Holy smoke, Fermat was wrong!')
        elif res1 != res2:
            print ("Fermat's Last Theorem is correct!")
    else:
        print ('No, that value violates the rule of this theorem! ')

        

        
def main():
    print ("This activity will ask you to input values to prove Fermat's last theorem")
    print ("Rule: We only allow values for a,b,and c to be positive integers. Also, n should be greater than 2!")
    val_a = int(input("what is the value of a? "))
    val_b = int(input("what is the value of b? "))
    val_c = int(input("what is the value of c? "))
    val_n = int(input("what is the value of n? "))
    return check_fermat(val_a, val_b, val_c, val_n)


main()
