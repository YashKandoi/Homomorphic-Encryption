#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <math.h>
#include <sys/time.h>

struct timeval t1, t2;
double time_taken;

int modulo(int a, int b, int p)
{
    int c=1;
    int d=a;
    while(b>0){
        if(b%2!=0)
            c=(c*d)%p;
        d=(d*d)%p;
        if(d>(p/2)){
            d=d-p;
        }
        b/=2;
    }
    if(c<0){
        c=c+p;
    }
    return c%p;
}
int revModulo(int a, int b, int p)
{
    int z = modulo(a, b, p);
    int t1 = 0;
    int t2 = 1;
    int t;
    int quotient, remainder;
    int A, B;
    if (z > p)
    {
        A = z;
        B = p;
    }
    else
    {
        A = p;
        B = z;
    }
    while(B!=0){
        quotient=A/B;
        remainder=A%B;
        t=t1-(quotient*t2);
        A=B;
        B=remainder;
        t1=t2;
        t2=t;
    }
    return t1;
}

int main()
{
    gettimeofday(&t1, NULL);
    printf("The program starts \n");
    int p = 2879;
    int g = 2585;
    int x = 47;
    int m = 10;
    int r = 65;

    printf("The message is %d\n",m);
    // to compute y= g^x = 2585^47(mod 2879) = 2826(mod 2879)
    
    int mody = modulo(g, x, p); // a=2585,b=47
    // printf("y= g^x is %d mod %d\n",mody,p);
    int modc1 = modulo(g, r, p);
    printf("The value of c1 is : %d mod %d\n",modc1,p);
    int modc2 = modulo(m*modulo(mody, r, p),1,p);
    printf("The value of c2 is : %d mod %d\n",modc2,p);
    int c3 = revModulo(modc1, x, p);
    printf("The value of revModulo is: %d\n",c3);
    int m2 = modulo(modc2 * c3, 1, p); // decrypted message
    printf("The value of decrypted message is : %d \n",m2);


    // p = 107;
    // g = 2;
    // x = 67;
    // m = 13;
    // r = 45;

     p = 2879;
     g = 2585;
     x = 47;
     m = 13;
     r = 65;

    printf("The message is %d\n",m);
    // to compute y= g^x = 2585^47(mod 2879) = 2826(mod 2879)
    
    mody = modulo(g, x, p); // a=2585,b=47
    // printf("y= g^x is %d mod %d\n",mody,p);
    int modc11 = modulo(g, r, p);
    printf("The value of c1 is : %d mod %d\n",modc11,p);
    int modc22 = modulo(m*modulo(mody, r, p),1,p);
    printf("The value of c2 is : %d mod %d\n",modc22,p);
    c3 = revModulo(modc11, x, p);
    printf("The value of revModulo is: %d\n",c3);
    m2 = modulo(modc22 * c3, 1, p); // decrypted message
    printf("The value of decrypted message is : %d \n",m2);

    //Multiplication
    int c1mult=modulo(modc1*modc11,1,p);
    int c2mult=modulo(modc2*modc22,1,p);
    printf("The result of multiplication are:\n");
    printf("The value of c1mult is : %d mod %d\n",c1mult,p);
    printf("The value of c2mult is : %d mod %d\n",c2mult,p);
    c3 = revModulo(c1mult, x, p);
    printf("The value of revModulo is: %d\n",c3);
    m2 = modulo(c2mult * c3, 1, p); // decrypted message
    printf("The value of decrypted message is : %d \n",m2);


    gettimeofday(&t2, NULL);
    time_taken = (t2.tv_sec - t1.tv_sec) * 1e6;
    time_taken = (time_taken + (t2.tv_usec - t1.tv_usec)) * 1e-6;
    printf("The tasks took %f seconds to execute\n", time_taken);

    return 0;
}