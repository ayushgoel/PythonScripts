# https://www.interviewbit.com/problems/best-time-to-buy-and-sell-stocks-ii/

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        if len(A) <= 1:
            return 0
        ans = []
        mini = A[0]
        maxp = 0
        isLastMax = False
        for i in xrange(1, len(A)):
            if A[i] > A[i-1]:
                maxp = A[i] - mini
                isLastMax = True
            else:
                mini = A[i]
                ans += [maxp]
                maxp = 0
                isLastMax = False
        if isLastMax:
            ans += [maxp]
        return sum(ans)

s = Solution()
inp = [ 1, 5, 9, 2, 8 ]
inp = [5, 1, 5, 9, 2, 10]
print s.maxProfit(inp)
