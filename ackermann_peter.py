#ackerman function
#credit: Allen Downey in his book: Think Python 2 (2015).


def ackermann_peter(m,n):
    if m == 0:
        return n+1
    elif m > 0 and n == 0:
        return ackermann_peter(m-1,1)
    elif m > 0 and n > 0:
        return ackermann_peter(m-1, ackermann_peter(m, n-1))


try:
    print (ackermann_peter(5,8))
except:
    print ('Something went wrong! Too much recursive calls.')
