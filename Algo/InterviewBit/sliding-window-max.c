// https://www.interviewbit.com/problems/sliding-window-max/

#include <stdio.h>
#include <stdlib.h>

/**
 * @input A : Read only ( DON'T MODIFY ) Integer array
 * @input n1 : Integer array's ( A ) length
 * @input B : Integer
 *
 * @Output Integer array. You need to malloc memory, and fill the length in len1
 */
int* slidingMaximum(const int* A, int n1, int w, int *len1) {
    if (w >= n1)
    {
        *len1 = 1;
        int *ans = malloc(sizeof(int));
        ans[0] = A[0];
        int i;
        for (i = 1; i < n1; ++i)
        {
            if (A[i] > ans[0])
            {
                ans[0] = A[i];
            }
        }
        return ans;
    }

    int *ans = malloc(sizeof(int) * (n1-w+1));
    *len1 = n1-w+1;

    // get max in width
    int max_element_value = A[0];
    int max_element_index = 0;
    int i;

    for (i = 0; i < w; ++i)
    {
        if (A[i] >= max_element_value)
        {
            max_element_value = A[i];
            max_element_index = i;
            ans[0] = max_element_value;
        }
    }

    //printf("1 %d %d\n", max_element_value, max_element_index);

    // for all next a[i]
    //     if added new element > current max, b[i] = new element
    //     else index of max_element dropped, find new max;
    for (i = 1; i < *len1; ++i)
    {
        //printf("2 %d %d %d\n", i, max_element_value, max_element_index);

        if (A[i+w-1] > max_element_value)
        {
            //printf("3\n");
            max_element_index = i+w-1;
            max_element_value = A[i+w-1];
            ans[i] = max_element_value;
            continue;
        }
        if (i-1 == max_element_index)
        {
            //printf("4\n");
            int j;
            max_element_value = A[i];
            max_element_index = i;
            for (j = i; j < i+w; ++j)
            {
                if (A[j] >= max_element_value)
                {
                    //printf("Y\n");
                    max_element_value = A[j];
                    max_element_index = j;
                    ans[i] = max_element_value;
                }
            }
            continue;
        }
        ans[i] = max_element_value;
    }
    return ans;
}

int main(int argc, char const *argv[])
{
    int l;
    int a[] = {10, 9,8,7,6,5,4,3,2,1};
    int l1 = 10;
    int *b = slidingMaximum(a, l1, 1, &l);
    for (int i = 0; i < l; ++i)
    {
        printf("X %d\n", b[i]);
    }
    return 0;
}
