#function that refers to multiple functions like a domino effect.



def b(z):
    prod = a(z,z)
    print (z,prod)
    return prod


def a(x,y):
    x = x + 1
    return x * y

def c(x,y,z):
    total = x + y + z
    square = b(total) **2
    return square

def d(w,x,y,z):
    product = w * x * y * z
    call = c(x,y*product,z+1)
    return call

def e(v,w,x,y,z):
    mdas = v * w / x + y - z
    call = d(w*2,x*3,y+5,z*mdas)
    return call



x = 1
y = x + 1


print (e(x+x,x+1,x,y+3,x+y))



#credit: These functions are modifications on an example from Allen Downey's Book: Think Python 2(2015).
#Function call explanation:
#first, it evaluates the precondition (parameter). Then, it evaluates the statement of mdas.
#the mdas variables have been updated in the passed parameters. The new equivalent of v and w is v = x+x, w =x+1.
#mdas = 6.0 (becomes float because of division).
#function e refers to d. d referes to c, c refers to b, and b refers to a.
#This is the result:
#21622.0 467532506.0
#2.1858664416664003e+17
