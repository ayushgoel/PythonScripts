# import pprint

class Solution:
    def longestPalindrome(self, s: str) -> str:
        ls = len(s)
        dp = [[0 for i in range(ls)] for j in range(ls)]

        for d in range(ls):
            for i in range(ls):
                j = i+d
                if j >= ls:
                    continue
                if d == 0:
                    dp[i][j] = 1
                    continue
                if d == 1:
                    if s[i] == s[j]:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 0
                    continue
                dp[i][j] = 1 if (dp[i+1][j-1] == 1 and s[i] == s[j]) else 0
        ans = ""
        for i in range(ls):
            for j in range(ls):
                if dp[i][j] == 1 and (j-i+1) > len(ans):
                    ans = s[i:j+1]
        # pprint.pprint(dp)
        # print(ans)
        return ans

        # ls = len(s)
        # dp = [1] * ls

        # for i in range(1, ls):
        #     target = i-dp[i-1]-1
        #     if s[i] == s[i-1]:
        #         dp[i] = max(dp[i], 2)
        #     t1 = i - 2
        #     if t1 >= 0 and s[t1] == s[i]:
        #         dp[i] = max(dp[i], 3)
        #     if target >= 0 and s[target] == s[i]:
        #         dp[i] = max(dp[i], dp[i-1] + 2)
        # # dp1 = [0] * ls
        # # for i in range(1, ls):
        # #     target = i-dp1[i-1]-1
        # #     if target >= 0 and s[target] == s[i]:
        # #         dp1[i] = dp1[i-1] + 2
        
        # ans = ""
        # for i in range(ls):
        #     if dp[i] > len(ans):
        #         ans = s[i-dp[i]+1:i+1]
        # # for i in range(ls):
        # #     if dp1[i] > len(ans):
        # #         ans = s[i-dp1[i]+1:i+1]
        
        # print(dp)
        # print(ans)
        # return ans

s = Solution()
assert(s.longestPalindrome("a") == "a")
assert(s.longestPalindrome("bb") == "bb")
assert(s.longestPalindrome("abbd") == "bb")
assert(s.longestPalindrome("abcdca") == "cdc")
assert(s.longestPalindrome("ccc") == "ccc")
assert(s.longestPalindrome("babad") == "bab")
assert(s.longestPalindrome("cccc") == "cccc")
assert(s.longestPalindrome("a") == "a")

