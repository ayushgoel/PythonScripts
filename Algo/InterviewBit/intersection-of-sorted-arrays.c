// https://www.interviewbit.com/problems/intersection-of-sorted-arrays/

#include <stdio.h>
#include <stdlib.h>

/**
 * @input A : Read only ( DON'T MODIFY ) Integer array
 * @input n1 : Integer array's ( A ) length
 * @input B : Read only ( DON'T MODIFY ) Integer array
 * @input n2 : Integer array's ( B ) length
 *
 * @Output Integer array. You need to malloc memory, and fill the length in len1
 */
int* intersect(const int* A, int n1, const int* B, int n2, int *len1) {
    int i = 0, j = 0;
    *len1 = 0;
    int *ans = malloc(10000 * sizeof(int));
    while(i<n1 && j<n2) {
        // printf("X %d\n", *len1);
        if (A[i] < B[j])
        {
            i++;
            continue;
        }
        if (A[i] > B[j])
        {
            j++;
            continue;
        }
        if (A[i] == B[j])
        {
            ans[*len1] = A[i];
            i++;
            j++;
            *len1 = *len1 + 1;
            continue;
        }
    }
    return ans;
}

int main(int argc, char const *argv[])
{
    int n1 = 5;
    int A[] = {1, 2, 3, 3, 3};
    int n2 = 5;
    int B[] = {1, 2, 3, 5, 99};
    int ansL = 0;
    int *ans = intersect(A, n1, B, n2, &ansL);
    for (int i = 0; i < ansL; ++i)
    {
        printf("%d \n", ans[i]);
    }
    return 0;
}
