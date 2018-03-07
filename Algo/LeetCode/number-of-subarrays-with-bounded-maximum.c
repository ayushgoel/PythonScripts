#include <stdio.h>
#include <stdlib.h>

int numSubarrayBoundedMax(int* a, int asize, int l, int r) {
    // create left max where left[i] = number of elements lower than ith element
    // create right max where right[i] = number of elements lower than ith element
    // bool shouldInclude inc[i] = if ith leement in l and r range
    // 2 3 -> 6 element array with max ith element and in range
    // ans += left[i] + 1 * right[i] + 1
    int *shouldInclude = malloc(asize * sizeof(int));
    for (int i = 0; i < asize; ++i)
    {
        if (l <= a[i] && a[i] <= r) {
            shouldInclude[i] = 1;
        } else {
            shouldInclude[i] = 0;
        }
    }

    int *left = malloc(asize * sizeof(int));
    int *right = malloc(asize * sizeof(int));
    long long ans = 0;
    for (int i = 0; i < asize; ++i) {
        if (shouldInclude[i] == 1) {
            left[i] = 1;
            for (int j = i-1; j >= 0; --j) {
                if (a[j] >= a[i]) {
                    left[i] = i-j;
                    break;
                }
                if (j == 0 && a[j] < a[i]) {
                    left[i] = i+1;
                }
            }
            right[i] = 1;
            for (int j = i+1; j < asize; ++j) {
                if (a[j] > a[i]) {
                    right[i] = j-i;
                    break;
                }
                if (j == (asize-1) && a[j] < a[i]) {
                    right[i] = asize-i;
                }
            }

            printf("TQ %d %d %d %d\n", i, a[i], left[i], right[i]);
            ans += left[i] * right[i];
        }
    }
    return ans;
}

int main(int argc, char const *argv[])
{
    // int a[] = {2,1,4,3,3};
    // printf("%d\n", numSubarrayBoundedMax(a, 5, 2, 3));

    // int a[] = {73,55,36,5,55,14,9,7,72,52};
    int a[] = {22,55,36,5,55,14,9,7,55,52};
    // int a[] = {72,55,36,5,55,14,9,7,55,72};
    printf("%d\n", numSubarrayBoundedMax(a, 10, 32, 69));
    return 0;
}
