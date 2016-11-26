# https://www.interviewbit.com/problems/palindrome-string/

class Solution:
    def myalnum(self, x):
        return x.isalnum()

    # @param A : string
    # @return an integer
    def isPalindrome(self, a):
        a = filter(self.myalnum, a)
        a = a.lower()
        for i in xrange(len(a)/2):
            if a[i] != a[-i-1]:
                return 0
        return 1

s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
