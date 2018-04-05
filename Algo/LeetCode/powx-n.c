#include <stdio.h>
#include <limits.h>

double myPow(double x, int n) {
    // printf("%f %d\n",x,n);
    if (n == 0) {
        return 1;
    }
    if (n == 1) {
        return x;
    }
    if (n == -1) {
        return 1/x;
    }
    double t = myPow(x, n/2);
    if (n%2 == 0) {
        return t*t;
    } else {
        if (n < 0) {
            return (t*t)/x;
        } else {
            return t*t*x;
        }
    }
}

int main(int argc, char const *argv[])
{
    printf("%f\n", myPow(2.1,10));
    printf("%f\n", myPow(2.1,0));
    printf("%f\n", myPow(2.1,-10));
    printf("%f\n", myPow(2.123,INT_MAX));
    printf("%f\n", myPow(2.123,INT_MIN));
    printf("%f\n", myPow(1,INT_MAX));
    // printf("%f\n", myPow(2.123,-2147483648));
    return 0;
}