#include <stdio.h>
#include <stdlib.h>

int findMaxLength(int* nums, int n) {
    if(n <= 1) {
        return 0;
    }
    int t = 0;
    int *x = malloc((2 * n + 1) * sizeof(int)); // assume 0
    for (int i = 0; i < 2*n+1; ++i)
    {
        x[i] = -1;
    }
    int ans = 0;
    x[n] = 0;
    for (int i = 0; i < n; ++i)
    {
        if (nums[i] == 0)
        {
            t++;
        } else
        {
            t--;
        }
        if (x[t+n] == -1)
        {
            x[t+n] = i+1;
        } else {
            int poss = i - x[t+n] + 1;
            if (poss > ans)
            {
                ans = poss;
            }
        }
    }
    return ans;
}

int main(int argc, char const *argv[])
{
    int x[] = {0,1,0,1,1,1,1};
    printf("%d\n", findMaxLength(x,7));
    // int x[] = {0,1,0,1,1,1,0,0,1,1,0,1,1,1,1,1,1,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1,0,1,1,1,1,1,1,0,0,0,0,1,0,0,0,1,1,1,0,1,0,0,1,1,1,1,1,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,1,0,1,0,1,1,0,0,1,1,0,1,1,1,1,0,1,1,0,0,0,1,1};
    // printf("%d\n", findMaxLength(x,100));
    return 0;
}