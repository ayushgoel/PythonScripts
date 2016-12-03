// https://www.interviewbit.com/problems/min-jumps-array/

#include <stdio.h>
#include <stdlib.h>
#include <limits.h>


/**
 * @input A : Integer array
 * @input n1 : Integer array's ( A ) length
 *
 * @Output Integer
 */
int jump(int* a, int n) {
    int *min_steps = malloc(n * sizeof(int));
    int i;
    for (i = 0; i < n; ++i)
    {
        min_steps[i] = INT_MAX;
    }
    min_steps[0] = 0;
    for (i = 0; i < n; ++i)
    {
        int j;
        for (j = 1; j <= a[i]; ++j)
        {
            if (i+j < n)
            {
                if (min_steps[i] + 1 < min_steps[i+j])
                {
                    min_steps[i+j] = min_steps[i] + 1;
                }
            }
        }
    }
    return min_steps[n-1];
}
