
    # def decreasing(self, arr):
    #     dp = [1]*len(arr)
    #     for i in range(len(arr)):
    #         for j in range(i):
    #             if arr[j] > arr[i]:
    #                 dp[j] = max(dp[j], dp[i] + 1)
    #     return dp
    
class Solution:
    
    def increasing(self, arr):
        dp = [1]*len(arr)
        for i in range(len(arr)):
            for j in range(i):
                if arr[j] < arr[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return dp

    # @param A : tuple of integers
    # @return an integer
    def longestSubsequenceLength(self, A):
        inc = self.increasing(A)
        print(A)
        print(inc)
        dec = self.increasing(A[::-1])[::-1]
        ans = 0
        for i in range(len(A)):
            l1 = inc[i]
            l2 = dec[i]
            ans = max(l1+l2-1, ans)
        print(inc, dec)
        return ans
        
s = Solution()
print(s.longestSubsequenceLength([1, 11, 2 ,10, 4, 5, 2, 1]))