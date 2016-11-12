/**
 * @input A : 2D integer array
 * @input n11 : Integer array's ( A ) rows
 * @input n12 : Integer array's ( A ) columns
 *
 * @Output Void. Just modifies the args passed by reference
 */
void setZeroes(int** A, int r, int c) {
    int *r0=malloc(r*c*sizeof(int));
    int *c0=malloc(r*c*sizeof(int));
    int rc = 0, cc = 0, zeroes = 0;
    int i,j;
    for (i = 0; i < r; ++i)
    {
        for (j = 0; j < c; ++j)
        {
            if (A[i][j] == 0)
            {
                r0[rc++] = i;
                c0[cc++] = j;
                zeroes++;
            }
        }
    }
    int k;
    for (k = 0; k < zeroes; ++k)
    {
        for (i = 0; i < r; ++i)
        {
            A[i][c0[k]] = 0;
        }
        for (i = 0; i < c; ++i)
        {
            A[r0[k]][i] = 0;
        }
    }
}
