// https://www.interviewbit.com/problems/diffk/

#include <stdio.h>

/**
 * @input A : Integer array
 * @input n1 : Integer array's ( A ) length
 * @input B : Integer
 *
 * @Output Integer
 */
int diffPossible(int* a, int n, int b) {
    int i1 = 0, i2 = 0;
    while (1) {
        // printf("X %d %d\n", i1, i2);
        if (i1 == n || i2 == n) {
            return 0;
        }
        if (a[i2] - a[i1] == b && i2 != i1) {
            // printf("Answer %d %d\n", a[i2], a[i1]);
            return 1;
        }
        if (a[i2] - a[i1] > b) {
            i1++;
        } else {
            i2++;
        }
    }
}

int main(int argc, char const *argv[])
{
    int in[] = { 0, 1, 9, 10, 13, 17, 17, 17, 23, 25, 29, 30, 37, 38, 39, 39, 40, 41, 42, 60, 64, 70, 70, 70, 72, 75, 85, 85, 90, 91, 91, 93, 95 };
    printf("%d\n", diffPossible(in, 33, 83));
    return 0;
}