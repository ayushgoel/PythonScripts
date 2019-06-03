class Solution:
    # @param A : string
    # @return an integer
    def braces(self, a):
        s = []
        a = ''.join(a.split())
        for i in a:
            if i == '(':
                s += [i]
            elif i == ')':
                print(s)
                x = 0
                while s[-1] != '(':
                    x += 1
                    s = s[:-1]
                if x == 1:
                    return 1
                else:
                    s = s[:-1]
                    s += ["Exp"]
            else:
                s += i
        return 0

s = Solution()
assert(s.braces('(a*b)') == 0)
assert(s.braces('((a*b))') == 1)
assert(s.braces('(a + (a + b))') == 0)
