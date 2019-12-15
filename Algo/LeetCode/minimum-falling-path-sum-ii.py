import pprint

class Solution:
    def minFallingPathSum(self, arr) -> int:
        # pprint.pprint(arr)
        dp = [[0 for i in range(len(arr[0])+1)] for j in range(len(arr))]
        m = 0
        for i in range(len(arr[0])):
            dp[0][i] = arr[0][i]
            if dp[0][i] < arr[0][m]:
                m = i
        dp[0][-1] = m

        for i in range(1, len(arr)):
            m = 0
            for j in range(len(arr[0])):
                t = dp[i-1][-1]
                if j != t:
                    dp[i][j] = arr[i][j] + dp[i-1][t]
                else:
                    min_sum = None
                    for k in range(len(arr[0])):
                        if j == k:
                            continue
                        if min_sum is None:
                            min_sum = arr[i][j] + dp[i-1][k]
                            continue
                        min_sum = min(min_sum, arr[i][j] + dp[i-1][k])
                    dp[i][j] = min_sum

                if dp[i][j] < dp[i][m]:
                    m = j
            dp[i][-1] = m

        # pprint.pprint(dp)
        return min(dp[-1][:-1])

s = Solution()
assert(s.minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]]) == 13)
assert(s.minFallingPathSum([[-73,61,43,-48,-36],[3,30,27,57,10],[96,-76,84,59,-15],[5,-49,76,31,-7],[97,91,61,-46,67]]) == -192)