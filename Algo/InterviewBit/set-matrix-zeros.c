// https://www.interviewbit.com/problems/set-matrix-zeros/

#include <stdio.h>
#include <stdlib.h>

/**
 * @input A : 2D integer array
 * @input n11 : Integer array's ( A ) rows
 * @input n12 : Integer array's ( A ) columns
 *
 * @Output Void. Just modifies the args passed by reference
 */
void setZeroes(int** A, int r, int c) {
    int i,j;
    int **zeroes = (int **)malloc(r * sizeof(int *));
    for (i=0; i<r; i++)
         zeroes[i] = (int *)malloc(c * sizeof(int));

    for (i = 0; i < r; ++i)
    {
        for (j = 0; j < c; ++j)
        {
            if (A[i][j] == 0)
            {
                zeroes[i][j] = 1;
            } else
            {
                zeroes[i][j] = 0;
            }
        }
    }
    for (i = 0; i < r; ++i)
    {
        for (j = 0; j < c; ++j)
        {
            if (zeroes[i][j] == 1)
            {
                int k;
                for (k = 0; k < r; ++k)
                {
                    // printf("T %d %d\n", k, j);
                    A[k][j] = 0;
                }
                for (k = 0; k < c; ++k)
                {
                    // printf("U %d %d\n", i, k);
                    A[i][k] = 0;
                }
            }

        }
    }
}

int main(int argc, char const *argv[])
{
    int r=2,c=2,i,j;
    int **zeroes = (int **)malloc(r * sizeof(int *));
    for (i=0; i<r; i++)
         zeroes[i] = (int *)malloc(c * sizeof(int));
     zeroes[0][1] = 1;
     zeroes[1][0] = 1;
     zeroes[1][1] = 1;
    setZeroes(zeroes, r,c);
    for (i = 0; i < r; ++i)
    {
        for (j = 0; j < c; ++j)
        {
            printf("%d ", zeroes[i][j]);
        }
        printf("\n");
    }
    return 0;
}
