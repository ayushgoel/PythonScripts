// https://www.interviewbit.com/problems/highest-product/

#include <stdio.h>
#include <stdlib.h>

/**
 * @input A : Integer array
 * @input n1 : Integer array's ( A ) length
 *
 * @Output Integer
 */
int maxp3(int* a, int n) {
    if (n < 3)
    {
        return 0;
    }
    int *min_heap = malloc(3*sizeof(int));
    int minimum_index = 0;
    int i;
    for (i = 0; i < 3; ++i)
    {
        min_heap[i] = i;
        if (a[i] < a[minimum_index])
        {
            minimum_index = i;
        }
    }

    for (i = 3; i < n; ++i)
    {
        if (a[i] > a[minimum_index])
        {
            int j;
            for (j = 0; j < 3; ++j)
            {
                if (min_heap[j] == minimum_index)
                {
                    min_heap[j] = i;
                }
            }

            // Recalculate minimum_index
            minimum_index = i;
            for (j = 0; j < 3; ++j)
            {
                if (a[min_heap[j]] < a[minimum_index])
                {
                    minimum_index = min_heap[j];
                }
            }
        }
    }

    int ans = 1;
    for (i = 0; i < 3; ++i)
    {
        ans *= a[min_heap[i]];
    }
    return ans;
}

int main(int argc, char const *argv[])
{
    int a[] = {0, -1, 3, 100, 70, 50};
    printf("X %d\n", maxp3(a, 6));
    return 0;
}
