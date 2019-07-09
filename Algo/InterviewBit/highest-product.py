# https://www.interviewbit.com/problems/highest-product/

class Solution:

    # @param A : list of integers
    # @return an integer
    def maxp3(self, a):
        if len(a) < 3:
            return 0
        ans = None
        b = []
        for i in a:
            if i == 0:
                ans = 0
            else:
                b.append(i)

        if len(b) < 3:
            return 0

        b.sort()

        if ans is None:
            ans = b[0] * b[1] * b[2]
        ans = max(ans, b[0] * b[1] * b[-1])
        ans = max(ans, b[-3] * b[-1] * b[-2])

        print(ans)
        return ans


s = Solution()
print(s.maxp3([-5,-2,1,2,3,4,8,10,-4]))
assert(s.maxp3([-5,-2,1,2,3,4]) == 40)
assert(s.maxp3([ 0, -1, 3, 100, 70, 50 ]) == 350000)
