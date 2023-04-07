import cv2
import math
import time
from random import *
import numpy as np
from PIL import Image
from array import *


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


def concatArr(arr, i, j, size):
    str_con = ""
    for row in range(i, i+size):
        for column in range(j, j+size):
            if int(arr[row][column]/100) !=0:
                num_str = str(arr[row][column])
            elif int(arr[row][column]/100) ==0 and int(arr[row][column]/10) !=0:
                num_str = "0"+str(arr[row][column])
            else:
                num_str = "00"+str(arr[row][column])
            str_con = str_con + num_str
    return int(str_con)

def digits(num):
    count=0
    while(num!=0):
        num //= 10
        count += 1
    return count


if __name__ == "__main__":
    n = cv2.imread("image3.png", 0)
    Row = len(n)
    Column = len(n[0])
    matrix = []
    print("The program starts ")
    print("The size of image is ", Row, "X", Column, " pixels")
    p = 999998999999
    g = 2585
    x = 47
    r = 65
    # defines the size of the block (size*size)
    size=2

    # Dummy
    np.save('dummy.npy', n)
    dummy_matrix = np.load('dummy.npy')
    dum = Image.fromarray(dummy_matrix, "L")
    dum.save('dummy.png')

    # original matrix
    print(n)

    # preparing the original array concatenation
    original_concat=[]
    for row in range(0,Row,size):
        for column in range(0,Column,size):
            original_con=concatArr(n,row,column,size)
            original_concat.append(original_con)
    print(original_concat)

    # Key generation
    t1 = time.time()
    mody = modulo(g, x, p)  # a=2585,b=47
    t2 = time.time()
    time_taken = t2 - t1
    print("The key generation task took", time_taken, "seconds to execute")
    # Public key (p,g,mody)

    # Encryption
    modc11 = []
    modc1 = modulo(g, r, p)
    enc_concat=[]
    enc = n
    t1 = time.time()

    # encrypting the block matrix
    for row in range(len(original_concat)):
        r = randint(1, p-2)
        modc2 = modulo(g, r, p)
        enc_con=modulo((original_concat[row]+1)*modulo(mody, r, p), 1, p)
        if digits(enc_con)==size*size*3:
            enc_concat.append(enc_con)
        else:
            enc_con_str=str(enc_con)
            while(digits(int(enc_con_str))!=size*size*3):
                enc_con_str=str(enc_con)+"0"
            enc_concat.append(int(enc_con_str))
        modc11.append(modc2)
    print(enc_concat)

    t2 = time.time()
    time_taken = t2 - t1
    print("The encryption tasks took", time_taken, "seconds to execute")


    # homomorphic multiplication
    # num = 3
    # Nmodc1 = modulo(g, r, p)
    # print("The value of c1 is :", Nmodc1, "mod", p)
    # Nmodc2 = modulo(num*modulo(mody, r, p), 1, p)
    # print("The value of c2 is :", Nmodc2, "mod", p)
    # # encrpyted value of num is stored in Nmodc2
    # for row in range(Row):
    #     for column in range(Column):
    #         modc11[row][column] = Nmodc1*modc11[row][column]
    #         enc1[row][column] = Nmodc2 * enc1[row][column]

    # matrix2=np.array(matrix)
    # encrypted matrix
    # print(matrix2)

    # np.save('image1_encrypted.npy', enc)
    # encrypted_matrix = np.load('image1_encrypted.npy')
    # encrypted_image = Image.fromarray(encrypted_matrix, "L")
    # encrypted_image.save('encrypted_image.png')

    # Decryption

    # decrypt=[]
    # Row=len(matrix2)
    # Column=len(matrix2[0])
    dec = n
    dec_concat=[]
    t1 = time.time()
    # block decryption
    for row in range(len(original_concat)):
        c3 = revModulo(modc11[row], x, p)
        dec_con=modulo(enc_concat[row] * c3, 1, p)-1
        dec_concat.append(dec_con)
    print(dec_concat)

    t2 = time.time()
    time_taken = t2 - t1
    print("The decryption tasks took", time_taken, "seconds to execute")
    # decrypt2=np.array(n)
    # decrypted matrix
    print(dec)
    np.save('image1_decrypted.npy', dec)
    decrypted_matrix = np.load('image1_decrypted.npy')
    decrypted_image = Image.fromarray(decrypted_matrix, "L")
    decrypted_image.save('decrypted_image.png')
