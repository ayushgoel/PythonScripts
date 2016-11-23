# https://www.interviewbit.com/problems/coin-sum-infinite/

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer

    def solve(self, a, a_index, n):
        dp = [0] * (n+1)
        dp[0] = 1
        for i in xrange(a_index):
            for j in xrange(a[i], n+1):
                dp[j] = (dp[j] + dp[j-a[i]]) % 1000007
                # print i, j, dp
        return dp[n]

    def coinchange2(self, A, B):
        return self.solve(A, len(A), B)

s = Solution()
print(s.coinchange2([1,2,3], 4))
# print s.dp
