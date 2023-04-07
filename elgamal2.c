#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <math.h>
#include <sys/time.h>

struct timeval t1, t2;
double time_taken;

long long int modulo(long long int a, long long int b, long long int p)
{
    long long int c = 1;
    long long int d = a;
    while (b > 0)
    {
        if (b % 2 != 0)
            c = (c * d) % p;
        d = (d * d) % p;
        if (d > (p / 2))
        {
            d = d - p;
        }
        b /= 2;
    }
    // if (c < 0)
    // {
    //     c = c + p;
    // }
    // return c % p;
    return c;
}
long long int revModulo(long long int a, long long int b, long long int p)
{
    long long int z = modulo(a, b, p);
    long long int t1 = 0;
    long long int t2 = 1;
    long long int t;
    long long int quotient, remainder;
    long long int A, B;
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
    while (B != 0)
    {
        quotient = A / B;
        remainder = A % B;
        t = t1 - (quotient * t2);
        A = B;
        B = remainder;
        t1 = t2;
        t2 = t;
    }
    return t1;
}

int main()
{

    printf("The program starts \n");
    long long int p = 443;
    long long int g = 2585;
    long long int x = 47;
    long long int m = 221;
    long long int r = 65;

    // long long int p = 107;
    // long long int g = 2;
    // long long int x = 67;
    // long long int m = 99;
    // long long int r = 45;
    printf("The message is %lld\n", m);
    // to compute y= g^x = 2585^47(mod 2879) = 2826(mod 2879)

    

    // Key Generation
    long long int mody = modulo(g, x, p); // a=2585,b=47
    // printf("y= g^x is %lld mod %lld\n",mody,p);

    

    // Encryption
    long long int modc1 = modulo(g, r, p);
    printf("The value of c1 is : %lld mod %lld\n", modc1, p);
    long long int modc2 = modulo(m * modulo(mody, r, p), 1, p);
    printf("The value of c2 is : %lld mod %lld\n", modc2, p);


    gettimeofday(&t1, NULL);
    
    // Decryption
    long long int c3 = revModulo(modc1, x, p);
    printf("The value of revModulo is: %lld\n", c3);
    long long int m2 = modulo(modc2 * c3, 1, p); // decrypted message
    printf("The value of decrypted message is : %lld \n", m2);

    gettimeofday(&t2, NULL);
    time_taken = (t2.tv_sec - t1.tv_sec) * 1e6;
    time_taken = (time_taken + (t2.tv_usec - t1.tv_usec)) * 1e-6;
    printf("The tasks took %f seconds to execute\n", time_taken);
    

    return 0;
}