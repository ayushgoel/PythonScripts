# https://www.interviewbit.com/problems/best-time-to-buy-and-sell-stocks-i/

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        if len(A) == 1:
            return 0
        profit = 0
        for i in xrange(1, len(A)):
            for j in xrange(i):
                if (A[i] - A[j]) > profit:
                    profit = A[i] - A[j]
        return profit
