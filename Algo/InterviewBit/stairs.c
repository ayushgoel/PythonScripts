/**
 * @input A : Integer
 *
 * @Output Integer
 */
int climbStairs(int n) {
    int *dp = malloc(n * sizeof(int));
    int i;
    for (i = 0; i < n; ++i)
    {
        dp[i] = 0;
    }
    dp[0] = 1;
    dp[1] = 1;
    for (i = 0; i < n; ++i)
    {
        if (i + 1 < n)
        {
            dp[i+1] += dp[i];
        }
        if (i + 2 < n)
        {
            dp[i+2] += dp[i];
        }
    }
    return dp[n-1];
}
