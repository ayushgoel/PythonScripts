// https://www.interviewbit.com/problems/remove-element-from-array/

#include <stdio.h>

/**
 * @input A : Integer array
 * @input n1 : Integer array's ( A ) length
 * @input B : Integer
 *
 * @Output Integer
 */
int removeElement(int* a, int l, int x) {
    int move_index = 0;
    int i;
    for (i = 0; i < l; ++i)
    {
        if (a[i] != x)
        {
            a[move_index++] = a[i];
        }
    }
    return move_index;
}

int main(int argc, char const *argv[])
{
    int a[] = {2,3,3,3,4,5,5,5,6,10};
    int l = 10;
    int x = 2;
    // int a[] = {0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2,2,2,2};
    // int l = 17;
    for (int i = 0; i < l; ++i)
    {
        printf("%d ", a[i]);
    }
    printf("\n");
    int ln = removeElement(a, l, x);
    for (int i = 0; i < ln; ++i)
    {
        printf("%d ", a[i]);
    }
    return 0;
}