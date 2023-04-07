#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <math.h>
#include <sys/time.h>

struct timeval t1, t2;
double time_taken;

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

int lcm(int a, int b) {
    return (a * b) / gcd(a, b);
}

int main(){
    gettimeofday(&t1, NULL);
    printf("The program starts: \n");
    int p=7;
    int q=11;
    int n=p*q;
    int g=5652;
    int m=42;
    int r=23;
    int nsq=n*n;

    // int p=13;
    // int q=17;
    // int n=p*q;
    // int g=4886;
    // int m=123;
    // int r=59;
    // int nsq=n*n;
    printf("The message is: %d\n",m);

    //Encryption
    //c=g^m . r^n .(mod n^2) = [g^m(mod n^2) * r^n(mod n^2)][mod n^2]
    int modc1= modulo(g,m,nsq);
    printf("The value of g^m is: %d mod(%d)\n",modc1,nsq);
    int modc2= modulo(r,n,nsq);
    printf("The value of r^n is: %d mod(%d)\n",modc2,nsq);
    int modc3=modc1*modc2;
    int modc= modulo(modc3,1,nsq);
    printf("The value of g^m.r^n mod n^2 is: %d mod(%d)\n",modc,nsq);

    //Decryption
    int lambda = lcm(p-1,q-1); //LCM(p-1,q-1)
    printf("The value of lambda is %d\n",lambda);
    int modg1=modulo(g,lambda,nsq);
    printf("The value of g^lambda is: %d mod(%d)\n",modg1,nsq);
    int k=(modg1-1)/n;
    printf("The value of k is: %d \n",k);
    int meu = revModulo(k,1,n);
    printf("The value of meu is: %d mod(%d)\n",meu,n);
    int m1= modulo(modc,lambda,nsq);
    printf("The value of c^lambda mod (n^2) is: %d mod(%d)\n",modc,nsq);
    int m2= (m1-1)/n;
    int m3=m2*meu;
    int m4=modulo(m3,1,n);
    printf("The decrypted message is %d\n",m4);

    gettimeofday(&t2, NULL);
    time_taken = (t2.tv_sec - t1.tv_sec) * 1e6;
    time_taken = (time_taken + (t2.tv_usec - t1.tv_usec)) * 1e-6;
    printf("The tasks took %f seconds to execute\n", time_taken);

    return 0;

}