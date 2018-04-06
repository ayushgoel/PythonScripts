class Solution(object):
    def superPowT(self, a, b, d):
        # print a,b,d
        if len(b) == 1:
            if d.has_key((a,b[0])):
                return d[(a,b[0])]
            d[(a,b[0])] = (a**b[0]) % 1337
            return d[(a,b[0])]

        ones = b[-1]
        if not d.has_key((a,ones)):
            d[(a,ones)] = (a**ones) % 1337
        if not d.has_key((a,10)):
            d[(a,10)] = (a**10) % 1337
        return (d[(a,ones)] * self.superPowT(d[(a,10)], b[:-1], d)) % 1337

    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        return self.superPowT(a, b, {})

s = Solution()
assert(s.superPow(2, [1,0]) == 1024)
assert(s.superPow(2, [3]) == 8)
assert(s.superPow(2, [3,0,0,0,0,0,0,0]) == 351)
assert(s.superPow(2, [0]) == 1)
assert(s.superPow(12, [2,3,1,4,2]) == 421)


print "All tests passed!"
