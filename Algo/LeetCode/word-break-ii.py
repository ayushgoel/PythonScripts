import pprint

class Solution:
    def __init__(self):
        self.memo = {}

    def breakW(self, s, d):
        if len(s) == 0:
            return []
        if s in self.memo:
            return self.memo[s]
        # print(s, d, memo)
        # pprint.pprint(self.memo)
        # print("1")
        ans = []
        m = d
        for i in range(len(s)):
            # print("2", s[i], i, len(s))
            if s[i] not in m:
                break
            if 'stop' in m[s[i]]: # found word
                # print("3")
                if i+1 == len(s): # sentance completes
                    ans += [[s]]
                    continue
                p = self.breakW(s[i+1:], d)
                # if p == []:
                #     ans += [[s[:i+1]]]
                # else:
                    # pprint.pprint(p)
                # print("4", p)
                ans += [[s[:i+1]]+j for j in p]
            m = m[s[i]]
        # pprint.pprint("BREAK")
        # if ans is []:
        #     ans = None
        self.memo[s] = ans
        # pprint.pprint(self.memo)
        return ans


    def wordBreak(self, s, wordDict):
        tr = {}
        for word in wordDict:
            m = tr
            for i in word:
                if i in m:
                    m = m[i]
                else:
                    m[i] = {}
                    m = m[i]
            m['stop'] = True
        # pprint.pprint(tr)
        ans = self.breakW(s, tr)
        # pprint.pprint(ans)
        return [" ".join(i) for i in ans]

assert(Solution().wordBreak("sanddog", ["cat","cats","and","sand","dog"]) == ['sand dog'])
x = Solution().wordBreak("catsanddog", ["cat","cats","and","sand","dog"])
# print("QQQ", x)
assert(x == ['cat sand dog', 'cats and dog'])
assert(Solution().wordBreak("asd", ["as", "ds", "dsa"]) == [])
y = Solution().wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])
# pprint.pprint("QQQ", y)
