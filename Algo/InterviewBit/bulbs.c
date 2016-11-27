// https://www.interviewbit.com/problems/bulbs/

/**
 * @input A : Integer array
 * @input n1 : Integer array's ( A ) length
 *
 * @Output Integer
 */
int bulbs(int* a, int n) {
    int ans = 0;
    if (n == 0)
    {
        return 0;
    }
    if (a[0] == 0)
    {
        ans++;
    }
    int i;
    for (i = 1; i < n; ++i)
    {
        if (a[i] == 0)
        {
            if (a[i-1] == 1)
            {
                ans++;
            }
        }
        if (a[i] == 1)
        {
            if (a[i-1] == 0)
            {
                ans++;
            }
        }
    }
    return ans;
}
