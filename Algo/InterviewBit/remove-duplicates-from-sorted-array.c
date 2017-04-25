// https://www.interviewbit.com/problems/remove-duplicates-from-sorted-array/

#include <stdio.h>
#include <stdlib.h>

/**
 * @input A : Integer array
 * @input n1 : Integer array's ( A ) length
 *
 * @Output Integer
 */
int removeDuplicates(int* a, int l) {
    int move_to = 0;
    int i;
    for (i = 1; i < l; ++i) {
        if (a[i] != a[i-1]) {
            move_to++;
            a[move_to] = a[i];
        }
    }
    return move_to+1;
}

int main(int argc, char const *argv[])
{
    // int a[] = {2,3,3,4,5,5,5,6,10};
    // int l = 9;
    int a[] = {2,2};
    int l = 2;
    // int a[] = {2,3,3,4,5,5,5,6,10};
    // int l = 9;
    for (int i = 0; i < l; ++i)
    {
        printf("%d ", a[i]);
    }
    printf("\n");
    int ln = removeDuplicates(a, l);
    for (int i = 0; i < ln; ++i)
    {
        printf("%d ", a[i]);
    }
    return 0;
}