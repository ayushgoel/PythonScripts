// https://www.interviewbit.com/problems/min-steps-in-infinite-grid/

#include <stdio.h>
#include <stdlib.h>

/**
 * @input X : Integer array corresponding to the X co-ordinate
 * @input n1 : Integer array's ( X ) length
 * @input Y : Integer array corresponding to the Y co-ordinate
 * @input n2 : Integer array's ( Y ) length
 *
 * Points are represented by (X[i], Y[i])
 *
 * @Output Integer
 *
 */
int coverPoints(int* X, int n1, int* Y, int n2) {
    if (n1 <= 1 || n2 <= 1)
    {
        return 0;
    }
    int i, dist = 0;
    for (i = 0; i < n1-1; ++i)
    {
        dist += distance(X[i], Y[i], X[i+1], Y[i+1]);
    }
    return dist;
}

int maxI(int a, int b) {
    if (a>b)
    {
        return a;
    }
    return b;
}

int absI(int x) {
    if (x < 0)
    {
        return -x;
    }
    return x;
}

int distance(int x1, int y1, int x2, int y2) {
    return maxI(absI(x2 - x1), absI(y2 - y1));
}