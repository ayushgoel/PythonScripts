// https://www.interviewbit.com/problems/verify-prime/

#include <stdio.h>

/**
 * @input A : Integer
 *
 * @Output Integer
 */
int isPrime(int A) {
    if(A == 1) {
        return 0;
    }
    int i;
    for(i = 2; i*i <= A; ++i) {
        if(A % i == 0) {
            return 0;
        }
    }
    return 1;
}

int main(int argc, char const *argv[])
{
    printf("%d\n", isPrime(41443));
    return 0;
}
