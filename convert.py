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
    n=cv2.imread("image2.png",0)
    Row=len(n)
    Column=len(n[0])
    matrix=[]
    print("The program starts ")
    p = 337
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
    mody = modulo(g, x, p)  # a=2585,b=47
    # Public key (p,g,mody)

    # Encryption
    modc1 = modulo(g, r, p)
    enc=n
    # for loop matrix
    for row in range(Row):
        # a=[]
        for column in range(Column):
            enc[row][column] = modulo(n[row][column]*modulo(mody, r, p), 1, p)
            # a.append(modc2)
        # matrix.append(a)
    
    # encrypted matrix
    print(enc)

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
    c3 = revModulo(modc1, x, p)
    # loop
    for row in range(Row):
        # a=[]
        for column in range(Column):
            dec[row][column] = modulo(n[row][column] * c3, 1, p)
            # a.append(m2)
        # decrypt.append(a)
    
    # decrypt2=np.array(n)
    #decrypted matrix
    print(dec)
    np.save('image1_decrypted.npy', dec)
    decrypted_matrix = np.load('image1_decrypted.npy')
    decrypted_image = Image.fromarray(decrypted_matrix,"L")
    decrypted_image.save('decrypted_image.png')
