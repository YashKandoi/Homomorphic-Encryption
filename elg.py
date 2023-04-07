import math
import time
from random import *


def modulo(a, b, p):
    c = 1
    d = a
    while (b > 0):
        if (b % 2 != 0):
            c = (c*d) % p
        d = (d*d) % p
        if (d > (p/2)):
            d = d-p
        b //= 2
    if (c < 0):
        c = c+p
    return c % p


def revModulo(a, b, p):
    z = modulo(a, b, p)
    t1 = 0
    t2 = 1
    t = 0
    quotient = 0
    remainder = 0
    A = 0
    B = 0
    if (z > p):
        A = z
        B = p
    else:
        A = p
        B = z
    while (B != 0):
        quotient = A//B
        remainder = A % B
        t = t1-(quotient*t2)
        A = B
        B = remainder
        t1 = t2
        t2 = t
    return t1


if __name__ == "__main__":
    print("The program starts ")
    p = 257
    g = 2585
    x = 47
    message = '169'
    m = int(message)
    r = 65
    # r=randint(1,p-2)
    

    print("The message is", m)
    # to compute y= g^x = 2585^47(mod 2879) = 2826(mod 2879)

    # Key generation
    t1 = time.time()
    mody = modulo(g, x, p)  # a=2585,b=47
    print("The value of y is :", mody, "mod", p)
    t2 = time.time()
    time_taken = t2 - t1
    print("The tasks took", time_taken, "seconds to execute")
    # print("y= g^x is %d mod %d" % (mody,p))

    # Encryption
    t1 = time.time()
    modc1 = modulo(g, r, p)
    print("The value of c1 is :", modc1, "mod", p)
    modc2 = modulo(m*modulo(mody, r, p), 1, p)
    print("The value of c2 is :", modc2, "mod", p)
    t2 = time.time()
    time_taken = t2 - t1
    print("The tasks took", time_taken, "seconds to execute")

    # Decryption
    t1 = time.time()
    c3 = revModulo(modc1, x, p)
    print("The value of revModulo is:", c3)
    m2 = modulo(modc2 * c3, 1, p)  # decrypted message
    print("The value of decrypted message is :", m2)
    t2 = time.time()
    time_taken = t2 - t1
    print("The tasks took", time_taken, "seconds to execute")

    
   
