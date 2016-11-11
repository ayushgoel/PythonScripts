// https://www.interviewbit.com/problems/largest-rectangle-in-histogram/

#include<stdio.h>
#include<stdlib.h>

/**
 * @input A : Integer array
 * @input n1 : Integer array's ( A ) length
 *
 * @Output Integer
 */
int largestRectangleArea(int* A, int n1) {
    int i=0;
    int *s = malloc(n1 * sizeof(int));
    int max_area = 0;
    int si = 0;
    int area_of_top = 0;

    while (i<n1)
    {
        // //printf("%d\n", i);
        if (si == 0
            || A[s[si-1]] <= A[i]) {
            s[si++] = i++;
            //printf("Added %d %d %d\n", si, s[si-1], i);
        } else {
            int tp = s[--si];
            //printf("Dropped to %d %d\n", si, s[si-1]);
            int area_of_top = A[tp] * ((si == 0) ? i : (i - s[si-1] -1));
            //printf("i %d %d si %d s[si] %d %d A[tp]%d \n", i, tp, si, s[si], area_of_top, A[tp]);
            if (max_area < area_of_top)
            {
                max_area = area_of_top;
                //printf("%d\n", max_area);
            }
        }
    }
    while(si != 0) {
        // //printf("%d %d\n", i, si);
        int tp = s[--si];
        int area_of_top = A[tp] * ((si == 0) ? i : (i - s[si-1] -1));
        //printf("%d %d %d %d %d \n", tp, si, s[si], area_of_top, A[tp]);
        if (max_area < area_of_top)
        {
            max_area = area_of_top;
            //printf("%d\n", max_area);
        }
    }
    return max_area;
}

int main(int argc, char const *argv[])
{
    // int a[] = {6, 2, 5, 4, 5, 1, 6};
    int a[] = {2, 5, 4, 5, 1};
    //printf("%d\n", largestRectangleArea(a, 5));
    return 0;
}
