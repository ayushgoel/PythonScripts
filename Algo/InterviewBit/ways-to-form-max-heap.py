import operator as op
import math

class Solution:
    # @param A : integer
    # @return an integer

    def __init__(self):
        self.cCache = {}
        self.sCache = {}

    def ncr(self, n, r):
        if self.cCache.has_key((n,r)):
            return self.cCache[(n,r)]
        #print n, r, "b"
        r = int(min(r, n-r))
        n = int(n)
        if r == 0:
            return 1
        #print n, r, "c"
        numer = reduce(op.mul, xrange(n-r+1, n+1))
        denom = reduce(op.mul, xrange(1, r+1))
        self.cCache[(n,r)] = numer//denom
        return self.cCache[(n,r)]

    def solve(self, a):
        if a == 0 or a == 1:
            return 1
        if self.sCache.has_key(a):
            return self.sCache[a]
        k = math.floor(math.log(a, 2))
        nodes = 2**k
        m = a + 1 - nodes
        x = nodes/2
        #print m,x,"a"
        l = x - 1 + min(x, m)
        r = x - 1 + max(0, m-x)
        self.sCache[a] = (self.ncr(a-1, l) * self.solve(l) * self.solve(r)) % 1000000007
        return self.sCache[a]

s = Solution()
print s.solve(2)
print s.solve(3)
print s.solve(4)
print s.solve(5)
print s.solve(6)
print s.solve(7)

