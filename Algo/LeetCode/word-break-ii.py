class Solution:
    def wordBreak(self, s, wordDict):
        if len(s) == 0:
            # print('q')
            return ['']
        ans = []
        # print(s, len(s))
        for i in range(len(s)):
            # print("2", s, i, len(s))
            if s[:i] in wordDict:
                t = self.wordBreak(s[i:], wordDict)
                # print(t)
                for j in t:
                    # print('q')
                    ans += [" ".join([s[:i]]+[j])]
        if s in wordDict:
            ans += [s]
        return ans

s = Solution()
assert(s.wordBreak("catsanddog", ["cat","cats","and","sand","dog"]) == ['cat sand dog', 'cats and dog'])