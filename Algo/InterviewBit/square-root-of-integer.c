// https://www.interviewbit.com/problems/square-root-of-integer/

#include <stdio.h>
#include <limits.h>

/**
 * @input A : Integer
 *
 * @Output Integer
 */
int Sqrt(int a) {
    int low = 0;
    int high = 46341;
    unsigned int aui = (unsigned int) a;
    while(1) {
        int mid = (low+high) / 2;
        printf("%d %d %d %d\n", low, high, mid, mid * mid);
        unsigned int mid_prod = mid * mid;
        unsigned int mid_1_prod = (mid+1) * (mid+1);

        if (mid_prod <= aui
            && mid_1_prod > aui) {
                return mid;
        }
        if (mid_prod > aui) {
            // printf("X\n");
            high = mid;
        } else {
            // printf("Y\n");
            low = mid;
        }
    }
}

int main(int argc, char const *argv[])
{
    printf("%d\n", Sqrt(2147483647));
    return 0;
}