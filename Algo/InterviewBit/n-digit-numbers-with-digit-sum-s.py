# https://www.interviewbit.com/problems/n-digit-numbers-with-digit-sum-s/

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, number_of_digits, required_sum):
        grid = [
            [0 for i in xrange(required_sum + 1)],
            # Any number greater than 9 requires 2 digits and thus has 0 ways.
            [1 for i in xrange(10)] + [0 for i in xrange(required_sum - 9)]
        ]
        for n in xrange(2, number_of_digits):
            row = []
            for i in xrange(required_sum + 1):
                current = 0
                for j in xrange(min(i + 1, 10)):
                    current += grid[n-1][i-j]
                row += [current]
            grid += [row]
        ans = 0
        for j in xrange(1, min(10, required_sum + 1)):
            ans += grid[number_of_digits-1][required_sum-j]
        return ans % 1000000007



s = Solution()
assert(s.solve(75, 22) == 478432066)
assert(s.solve(2, 4) == 4)
assert(s.solve(3, 5) == 15)
