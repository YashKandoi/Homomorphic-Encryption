import cv2
import math
import time
from random import *
import numpy as np
from PIL import Image



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
    n=cv2.imread("image7.jpeg",0)
    Row=len(n)
    Column=len(n[0])
    matrix=[]
    print("The program starts ")
    print("The size of image is ",Row,"X",Column," pixels")
    p = 349
    g = 2585
    x = 47
    r = 65

    # Dummy
    np.save('dummy.npy', n)
    dummy_matrix = np.load('dummy.npy')
    dum = Image.fromarray(dummy_matrix,"L")
    dum.save('dummy.png')

    # original matrix
    print(n)

    # Key generation
    t1 = time.time()
    mody = modulo(g, x, p)  # a=2585,b=47
    t2 = time.time()
    time_taken = t2 - t1
    print("The key generation task took", time_taken, "seconds to execute")
    # Public key (p,g,mody)

    # Encryption
    modc11=[]
    modc1 = modulo(g, r, p)
    enc=n
    enc1=[]
    t1 = time.time()
    # for loop matrix
    for row in range(Row):
        a=[]
        b=[]
        for column in range(Column):
            r=randint(1,p-2)
            modc2 = modulo(g, r, p)
            b1=modulo((n[row][column]+1)*modulo(mody, r, p), 1, p)
            enc[row][column] = modulo((n[row][column]+1)*modulo(mody, r, p), 1, p)
            b.append(b1)
            a.append(modc2)
        modc11.append(a)
        enc1.append(b)
    
    t2 = time.time()
    time_taken = t2 - t1
    print("The encryption tasks took", time_taken, "seconds to execute")

    # encrypted matrix
    # enc is just for representation(mod by 256 already done)
    # enc1 contains actual encrypted values
    print(enc)
    enc1=np.array(enc1)
    print(enc1)

    #homomorphic multiplication
    num=3
    Nmodc1 = modulo(g, r, p)
    print("The value of c1 is :", Nmodc1, "mod", p)
    Nmodc2 = modulo(num*modulo(mody, r, p), 1, p)
    print("The value of c2 is :", Nmodc2, "mod", p)
    # encrpyted value of num is stored in Nmodc2
    for row in range(Row):
        for column in range(Column):
            modc11[row][column]=Nmodc1*modc11[row][column]
            enc1[row][column]= Nmodc2 * enc1[row][column]


    # matrix2=np.array(matrix)
    # encrypted matrix
    # print(matrix2)
    np.save('image1_encrypted.npy', enc)
    encrypted_matrix = np.load('image1_encrypted.npy')
    encrypted_image = Image.fromarray(encrypted_matrix,"L")
    encrypted_image.save('encrypted_image.png')

    # Decryption

    # decrypt=[]
    # Row=len(matrix2)
    # Column=len(matrix2[0])
    dec=n
    
    t1 = time.time()
    # loop
    for row in range(Row):
        # a=[]
        for column in range(Column):
            c3 = revModulo(modc11[row][column], x, p)
            dec[row][column] = modulo(enc1[row][column] * c3, 1, p)-num
        #     a.append(m2)
        # decrypt.append(a)
    
    t2 = time.time()
    time_taken = t2 - t1
    print("The decryption tasks took", time_taken, "seconds to execute")
    # decrypt2=np.array(n)
    #decrypted matrix
    print(dec)
    np.save('image1_decrypted.npy', dec)
    decrypted_matrix = np.load('image1_decrypted.npy')
    decrypted_image = Image.fromarray(decrypted_matrix,"L")
    decrypted_image.save('decrypted_image.png')
