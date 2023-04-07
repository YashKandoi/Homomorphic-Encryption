#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>
#include<math.h>
#include<time.h>
#include<string.h>

// To find gcd of two numbers
int gcd(int a, int b){
    int l,s,g;
    if(a>b){
        l=a;
        s=b;
    }
    else{
        l=b;
        s=a;
    }
    while(s>0){
        if(a%s==0 && b%s ==0){
            g=s;
            break;
        }
        s--;
    }
    return g;
}

// Bob generates public and private keys: 
// Bob chooses a very large number q and a cyclic group G.
// From the cyclic group G, he choose any element g and
// an element x such that gcd(x, q) = 1.
// Then he computes y = g^x.
// Bob publishes y and  G,q,g as his public key and retains x as private key.

int keyGeneration(int q){
    int key = (rand()%(int)(pow(10,20))) + q;
    while(gcd(q,key)!=1){
        key = (rand() % (int)(pow(10, 20))) + q;
    }
    return key;
}

int modulo(int a, int b, int c){
    return ((int)pow(a,b)) %c;
}

// Alice encrypts data using Bob’s public key : 
// Alice selects an element r from cyclic group G 
// such that gcd(r, q) = 1.
// Then she computes c1 = g^r and s = y^r.
// She multiples s with M and stores it in c2.
// Then she sends (c1,c2) to Alice.

void encrypt(char* message,int *en_msg, int q, int y, int g){
    int r = keyGeneration(q);
    int s = modulo(y, r, q);
    int c1 = modulo(g, r, q);
    printf("g^r used : %d\n y^r used : %d\n", c1, s);
    for (int i = 0; message[i]; i++){
        en_msg[i] = s * (int)message[i]; // use similar to c2
    }
}

// Bob decrypts the message : 
// Bob calculates t = c1^x .
// He divides c2 by t to obtain M.

void decrypt(int *en_msg, char *dr_msg, int c1, int key, int q){
    int t = modulo(c1, key, q);
    int i;
    for ( i = 0; en_msg[i]; i++){
        // c1=en_msg[i];
        // t= modulo(c1, key, q);
        dr_msg[i] = (char)((int)(en_msg[i] / t));
    }
    dr_msg[i]='\0';
    // dr_msg = strcat(" ",dr_msg);
}

int main(){

    srand(time(0));
    char msg[] = "encryption", dr_msg[100];
    printf("Original message: %s\n",msg);
    int q = (rand() % (int)(pow(10, 20))) + (int)(pow(10, 50));
    int g = (rand() % (q - 2)) + 2;
    int key = keyGeneration(q);                 // basically x
    int y = modulo(g, key, q);
    int en_msg[100];
    printf("Original Message : %s\ng used : %d\ng^x used : %d\n", msg, g, y);
    encrypt(msg, en_msg, q, y, g);
    int p = en_msg[0];
    decrypt(en_msg, dr_msg, p, key, q);
    printf("Decrypted Message : %s\n", dr_msg);
    return 0;
}