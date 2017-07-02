cached = {}
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        #print s, p

        if cached.has_key((s, p)):
            return cached[(s, p)]

        if s == p:
            cached[(s, p)] = True
            return True

        if len(p) >= 2 and p[1] == "*":
            if self.isMatch(s, p[2:]):
                #print "1"
                cached[(s, p)] = True
                return True
            elif len(s) >= 1 and self.isMatch(s[0], p[0]) and self.isMatch(s[1:], p):
                #print "2"
                cached[(s, p)] = True
                return True
            #print "3"
            cached[(s, p)] = False
            return False
        elif len(p) >= 1 and len(s) >= 1 and p[0] == ".":
            #print "4"
            return self.isMatch(s[1:], p[1:])
        elif len(p) >= 1 and len(s) >= 1 and s[0] == p[0]:
            #print "5"
            return self.isMatch(s[1:], p[1:])
        cached[(s, p)] = False
        return False

s = Solution()
print(s.isMatch("abc", "abc")) #true
print(s.isMatch("aa","a")) # false
print(s.isMatch("aa","aa")) # true
print(s.isMatch("aaa","aa")) # false
print(s.isMatch("aa", "a*")) # true
print(s.isMatch("aa", ".*")) # true
print(s.isMatch("abcsdwqwe", ".*")) # true
print(s.isMatch("aab", "c*a*b")) # true
print(s.isMatch("ab", ".*c")) # false
print(s.isMatch("a", ".*..a*")) # false
print(s.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c")) # false
