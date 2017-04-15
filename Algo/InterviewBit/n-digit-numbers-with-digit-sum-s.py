# https://www.interviewbit.com/problems/n-digit-numbers-with-digit-sum-s/

class Solution:
    def rsolve(self, number_of_digits, required_sum, include_0):
        if self.cache.has_key((number_of_digits, required_sum, include_0)):
            return self.cache[(number_of_digits, required_sum, include_0)];
        # print number_of_digits, required_sum, include_0
        if required_sum < 0:
            #print "1"
            return 0
        if number_of_digits < 1:
            #print "2"
            return 0
        if number_of_digits == 1 and required_sum == 0:
            if include_0:
                #print "3"
                return 1
            #print "4"
            return 0
        if number_of_digits == 1 and required_sum < 10:
            #print "5"
            return 1
        ans = 0
        if include_0:
            ans += self.rsolve(number_of_digits - 1, required_sum, True)
        for i in xrange(1,10):
            ans += self.rsolve(number_of_digits - 1, required_sum - i, True)
        # print "In", number_of_digits, required_sum, include_0
        ans = ans % 1000000007
        # print "Ans", ans
        self.cache[(number_of_digits, required_sum, include_0)] = ans
        return ans

    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        self.cache = {}
        return self.rsolve(A, B, False)

s = Solution()
print s.solve(20, 40)

assert(s.solve(2, 4) == 4)
assert(s.solve(3, 5) == 15)