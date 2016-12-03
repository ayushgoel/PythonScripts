# https://www.interviewbit.com/problems/highest-product/

class Solution:

    def max3(self, a):
        ans = a[0] * a[1] * a[2]
        for i in xrange(len(a)):
            for j in xrange(i+1, len(a)):
                for k in xrange(j+1, len(a)):
                    if a[i] * a[j] * a[k] > ans:
                        ans = a[i] * a[j] * a[k]
        return ans

    # @param A : list of integers
    # @return an integer
    def maxp3(self, a):
        if len(a) < 3:
            return 0
        a.sort()
        max3 = a[-3:]
        low_index = len(a) - 3
        low3 = a[:low_index]
        # print low3, max3
        return self.max3(low3+max3)

s = Solution()
print(s.maxp3([-5,-2,1,2,3,4]))
