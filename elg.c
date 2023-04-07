#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>
#include<math.h>
#include<time.h>

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

void encrypt(int message,int en_msg, int q, int y, int g){
    int r = keyGeneration(q);
    int s = modulo(y, r, q);
    int c1 = modulo(g, r, q);
    printf("g^r used : %d\n y^r used : %d\n", c1, s);
    // for (int i = 0; message[i]; i++){
        en_msg = s * message; // use similar to c2
    // }
}

// Bob decrypts the message : 
// Bob calculates t = c1^x .
// He divides c2 by t to obtain M.

void decrypt(int en_msg, int dr_msg, int c1, int key, int q){
    int t = modulo(c1, key, q);
    int i;
    // for ( i = 0; en_msg; i++){
        // c1=en_msg[i];
        // t= modulo(c1, key, q);
        dr_msg = ((int)(en_msg/ t));
    // }
    // dr_msg[i]='\0';
}

int main(){

    srand(time(0));
    int msg = 77, dr_msg;
    printf("Original message: %d\n",msg);
    int q = (rand() % (int)(pow(10, 20))) + (int)(pow(10, 50));
    int g = (rand() % (q - 2)) + 2;
    int key = keyGeneration(q);                 // basically x
    int y = modulo(g, key, q);
    int en_msg;
    printf("Original Message : %d\ng used : %d\ng^x used : %d\n", msg, g, y);
    encrypt(msg, en_msg, q, y, g);
    int p = en_msg;
    decrypt(en_msg, dr_msg, p, key, q);
    printf("Decrypted Message : %d\n", dr_msg);
    return 0;
}

//     // 1. Key Generation
//     int p=2789; //any large prime number 
//     int g= 2585; //Any random generator between 1 and p-1
//     int x= 47; //private key randomly chosen by Alice
//     long long int y=  pow(g,x);
//     int ymod= (long long int)pow(g,x)%p;
//     // To send (p,g,y)
//     printf("The set (p,g,y) is : (%d,%d,%lld)\n",p,g,y);
//     printf("The value of y is: %d(mod %d)\n",ymod,p);

// // 2. Encryption algorithm
//     int message = 77;
//     int r=66;   //Random value
//     long long int c1= pow(g,r);
//     long long int c2= message*pow(y,r);
//     //To send (c1,c2)
//     printf("The set (c1,c2) is : (%lld,%lld)\n",c1,c2);

// // 3. Decryption Algorithm
//     long long int t = pow(c1,x);
//     int message2 = c2/t;
//     int mmod = message2%p;
//     printf("%d(mod %d)\n",mmod,p);