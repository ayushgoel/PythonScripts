class Solution(object):
    def hex(self, num):
        return int(num, 16)
    def similarity(self, c1, c2):
        c1 = c1[1:]
        c2 = c2[1:]
        return (-(self.hex(c1[:2]) - self.hex(c2[:2]))**2
                -(self.hex(c1[2:4]) - self.hex(c2[2:4]))**2
                -(self.hex(c1[4:]) - self.hex(c2[4:]))**2)
    def similarRGB(self, color):
        """
        :type color: str
        :rtype: str
        """
        color = color[1:]
        all_possible = {}
        for i in "0123456789abcdef":
            all_possible[i*2] = self.hex(i*2)
        ans = '#'

        for m in xrange(0,5,2):
            c = self.hex(color[m:m+2])
            t = 1000
            x=""
            for (i,j) in all_possible.iteritems():
                diff = abs(c-j)
                if diff < t:
                    t = diff
                    x = i
            ans += x
        return ans

s = Solution()
print s.similarRGB("#09f166")
