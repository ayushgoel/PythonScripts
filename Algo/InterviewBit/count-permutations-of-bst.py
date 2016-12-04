# https://www.interviewbit.com/problems/count-permutations-of-bst/

# class Solution:

#     def key(self, n, h, l):
#         return "{0}.{0}.{0}".format(n,h,l)

#     def nos(self, dp, n, h, lvl):
#         key = self.key(n,h,lvl)
#         if dp.has_key(key):
#             return dp[key]
#         if lvl == 0:
#             ans = sum([self.nos(n-1, h-1, i) for i in xrange(0, h-1)])
#             dp[key] = ans
#             return ans
#         else:
#             ans = 0
#             for i in xrange(1, n-1):
#                 for j in xrange(1, h-1):
#                     ans += self.nos(n-i, h-j, lvl)


#     # @param A : integer
#     # @param B : integer
#     # @return an integer
#     def cntPermBST(self, A, B):
#         dp = [[[0 for i in xrange(1000)] for j in xrange(1000)] for k in xrange(1000)]

import operator as op

dp = {}

def ncr(n, r):
    # print "NCR"
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return numer//denom

class Solution:
    def key(self, a, b):
        return "{0} {1}".format(a, b)
    # @param A : integer
    # @param B : integer
    # @return an integer
    def cntPermBST(self, A, B):
        # print "A", A, B
        k = self.key(A, B)
        if dp.has_key(k):
            return dp[k]

        if A<=1:
            if B==0:
                return 1
            return 0;

        ret=0

        for i in xrange(1, A+1):
            x = i-1
            y = A-i

            ret1=0

            # //iterate over height of left subtree
            for j in xrange(B-1):
            # for j = 0 to M-2:
                ret1 = ret1 + self.cntPermBST(x, j)*self.cntPermBST(y, B-1)

            # //iterate over height of right subtree
            for j in xrange(B-1):
            # for j = 0 to M-2:
                ret1 = ret1 + self.cntPermBST(y, j)*self.cntPermBST(x, B-1)

            # //add the case when both heights=M-1
            ret1 = ret1 + self.cntPermBST(x, B-1)*self.cntPermBST(y, B-1)

            ret = ret + ret1*ncr(x+y, y)

        dp[k] = ret % 1000000007
        return dp[k]

s = Solution()
print s.cntPermBST(8, 8)
