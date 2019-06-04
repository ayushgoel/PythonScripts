class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, a):
        for i in xrange(len(a)):
            # print(a)
            val = abs(a[i])
            if a[val] < 0:
                return val
            else:
                # print(val)
                a[val] = -a[val]
        return -1

s = Solution()
print(s.repeatedNumber([3,4,1,4,1]))
assert(s.repeatedNumber([3,4,1,4,1]) == 4)