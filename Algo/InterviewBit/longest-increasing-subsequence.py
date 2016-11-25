# https://www.interviewbit.com/problems/longest-increasing-subsequence/

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def lis(self, A):
        if len(A) < 1:
            return 0
        ans = [0] * len(A)
        ans[0] = 1
        for i in xrange(1, len(A)):
            max_len = 1
            for j in xrange(i):
                if A[i] > A[j]:
                    new_max_len = ans[j] + 1
                    if new_max_len > max_len:
                        max_len = new_max_len
            ans[i] = max_len
        print ans
        return max(ans)

s = Solution()
inp = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
inp = [ 14, 24, 18, 46, 55, 53, 82, 18, 101, 20, 78, 35, 68, 9, 16, 93, 101, 85, 81, 28, 78 ]
print inp
print(s.lis(inp))
