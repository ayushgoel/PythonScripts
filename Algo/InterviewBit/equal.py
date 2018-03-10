class Solution:
    # @param A : list of integers
    # @return a list of integers

    def isSmall(self, a, b):
        if a[0] < b[0]:
            return True
        elif a[0] > b[0]:
            return False
        else:
            return self.isSmall(a[1:], b[1:])

    def equal(self, a):
        dict = {}
        ans = None
        for i in xrange(len(a)):
            for j in xrange(i+1,len(a)):
                s = a[i] + a[j]
                # print dict, i, j
                if dict.has_key(s):
                    x = dict[s][:]
                    x.extend([i, j])
                    if len(set(x)) < 4:
                        continue
                    if ans is None or self.isSmall(x, ans):
                        ans = x
                dict[s] = [i, j]
        if ans is None:
            return []
        return ans

s = Solution()
print s.equal([3, 4, 7, 1, 2, 9, 8])
print s.equal([1, 1, 1, 1, 1])