import pprint

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        dp = [[0 for i in range(arrLen)] for j in range(steps+1)]
        dp[1][0] = 1
        dp[1][1] = 1
        for i in range(2, steps+1):
            for j in range(arrLen):
                if j == 0:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j+1]
                    if i == steps:
                        return dp[i][j]
                elif j == arrLen-1:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1]
                dp[i][j] = dp[i][j] % (10**9 + 7)
        # pprint.pprint(dp)
        return dp[steps][0]

s = Solution()
assert(s.numWays(3, 2) == 4)
assert(s.numWays(2, 4) == 2)
assert(s.numWays(4, 2) == 8)
assert(s.numWays(100, 10) == 836991026)
