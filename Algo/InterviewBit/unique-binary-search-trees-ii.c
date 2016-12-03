// https://www.interviewbit.com/problems/unique-binary-search-trees-ii/

#include <stdio.h>
#include <stdlib.h>

/**
 * @input A : Integer
 *
 * @Output Integer
 */
int numTrees(int a) {
    int *dp = malloc((a+1) * sizeof(int));
    dp[0] = 0;
    dp[1] = 1;
    dp[2] = 2;
    int i;
    for (i = 3; i <= a; ++i)
    {
        // calculate dp[i]
        int ans = 2 * dp[i-1];
        int j;
        for (j = 1; i-j-1 > 0; ++j)
        {
            ans += dp[j] * dp[i-j-1];
        }
        dp[i] = ans;
    }
    return dp[a];
}

int main(int argc, char const *argv[])
{
    int x = 5;
    printf("%d\n", numTrees(x));
    return 0;
}
