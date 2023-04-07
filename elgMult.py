import math
import time


def modulo(a, b, p):
    c = 1
    d = a
    while (b > 0):
        if (b % 2 != 0):
            c = (c*d) % p
        d = (d*d) % p
        if (d > (p/2)):
            d = d-p
        b //=2
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
    message = '11'
    m = int(message)
    r = 65

    print("The message is", m)
    # to compute y= g^x = 2585^47(mod 2879) = 2826(mod 2879)
    mody = modulo(g, x, p)  # a=2585,b=47
    # print("y= g^x is %d mod %d" % (mody,p))
    modc1 = modulo(g, r, p)
    print("The value of c1 is :", modc1, "mod", p)
    modc2 = modulo(m*modulo(mody, r, p), 1, p)
    print("The value of c2 is :", modc2, "mod", p)
    c3 = revModulo(modc1, x, p)
    print("The value of revModulo is:", c3)
    m2 = modulo(modc2 * c3, 1, p)  # decrypted message
    print("The value of decrypted message is :", m2)

    # p = 107
    # g = 2
    # x = 67
    # m = 13
    # r = 45

    p = 257
    g = 2585
    x = 47
    message = '7'
    m = int(message)
    r = 65
    print("The message is", m)
    # to compute y= g^x = 2585^47(mod 2879) = 2826(mod 2879)

    mody = modulo(g, x, p)  # a=2585,b=47
    # print("y= g^x is %d mod %d\n",mody,p);
    modc11 = modulo(g, r, p)
    print("The value of c1 is :", modc11, "mod", p)
    modc22 = modulo(m*modulo(mody, r, p), 1, p)
    print("The value of c2 is :", modc22, "mod", p)
    c3 = revModulo(modc11, x, p)
    print("The value of revModulo is:", c3)
    m2 = modulo(modc22 * c3, 1, p)  # decrypted message
    print("The value of decrypted message is :", m2)

    # Multiplication
    t1 = time.time()
    c1mult = modulo(modc1*modc11, 1, p)
    c2mult = modulo(modc2*modc22, 1, p)
    print("The result of multiplication are:")
    print("The value of c1mult is :", c1mult, "mod", p)
    print("The value of c2mult is :", c2mult, "mod", p)
    c3 = revModulo(c1mult, x, p)
    print("The value of revModulo is:", c3)
    m2 = modulo(c2mult * c3, 1, p)  # decrypted message
    print("The value of decrypted message is :", m2)

    t2 = time.time()
    time_taken = t2 - t1
    print("The tasks took", time_taken, "seconds to execute")