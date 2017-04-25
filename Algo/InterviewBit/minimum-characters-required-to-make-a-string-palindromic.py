# https://www.interviewbit.com/problems/minimum-characters-required-to-make-a-string-palindromic/

class Solution:

    def computeLPS(self, pat):
        M = len(pat)
        lps = [0]*M
        length = 0
        i = 1
        while i < M:
            if pat[i] == pat[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length-1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    # @param A : string
    # @return an integer
    def solve(self, A):
        string = A + "$" + A[::-1]
        lps = self.computeLPS(string)
        return len(A) - lps[-1]

s = Solution()
print s.solve("ABC")
print s.solve("AACECAAAA")
print s.solve("AACECAA")
print s.solve("AACEC")
