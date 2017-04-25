// https://www.interviewbit.com/problems/remove-duplicates-from-sorted-array-ii/

#include <stdio.h>
#include <stdlib.h>

/**
 * @input A : Integer array
 * @input n1 : Integer array's ( A ) length
 *
 * @Output Integer
 */
int removeDuplicates(int* a, int l) {
    int move_index = 0;
    int i;
    int count_same_number = 1;
    for (i = 1; i < l; ++i) {
        if (a[i] != a[i-1]) {
            ++move_index;
            count_same_number = 1;
            a[move_index] = a[i];
        } else {
            if (count_same_number < 2) {
                ++move_index;
                a[move_index] = a[i];
            }
            ++count_same_number;
        }
    }
    return move_index+1;
}

int main(int argc, char const *argv[])
{
    // int a[] = {2,3,3,3,4,5,5,5,6,10};
    // int l = 10;
    // int a[] = {2,2};
    // int l = 2;
    int a[] = {0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2,2,2,2};
    int l = 17;
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