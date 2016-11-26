// https://www.interviewbit.com/problems/first-missing-integer/

#include <stdio.h>
#include <stdlib.h>

/**
 * @input A : Integer array
 * @input n1 : Integer array's ( A ) length
 *
 * @Output Integer
 */

void swap(int *a, int ind1, int ind2) {
    // printf("%d %d\n", ind1, ind2);
    int tmp = a[ind1];
    a[ind1] = a[ind2];
    a[ind2] = tmp;
}

int firstMissingPositive(int* a, int n) {
    int positive_start = 0;
    int i;
    for (i = 0; i < n; ++i) {
        if (a[i] <= 0) {
            swap(a, i, positive_start++);
        }
    }

    // for (i = 0; i < n; ++i) {
    //     printf("%d\n", a[i]);
    // }
    // printf("XXX\n");

    for (i = positive_start; i < n; ++i) {
        int new_index;
        if (a[i] > 0) {
            new_index = positive_start + a[i] - 1;
        } else {
            new_index = positive_start - a[i] - 1;
        }
        if (new_index < n && a[new_index] > 0) {
            a[new_index] = -a[new_index];
        }
    }
    // for (i = 0; i < n; ++i) {
    //     printf("%d\n", a[i]);
    // }

    for (i = positive_start; i < n; ++i) {
        if (!(a[i] < 0)) {
            return (i - positive_start + 1);
        }
    }
    return (i - positive_start + 1);
}

int main(int argc, char const *argv[])
{
    int a[] = {1, 2, 3, 4, 5, 6};
    printf("ANS %d\n", firstMissingPositive(a, 6));
    return 0;
}
