class Solution:
    def letters(self, word):
        l = [0]*26
        orda = ord('a')
        for i in word:
            l[ord(i)-orda] += 1
        return l

    def is_successor(self, suc, pre):
        d = False
        for i in range(26):
            if suc[i]-pre[i] == 1:
                if d:
                    return False
                d = True
            elif suc[i]-pre[i] == 0:
                continue
            else:
                return False
        return d
            
    def longestStrChain(self, words):
        lw = len(words)
        words.sort(key=len)
        if lw < 1:
            return 1
        s = []
        for i in words:
            s += [self.letters(i)]
        dp = [1] * lw
        ans = 1
        for i in range(lw):
            for j in range(i):
                # print(s[i], s[j])
                ls = len(words[i])
                lp = len(words[j])
                if lp >= ls or  1 < (ls - lp):
                    # print(lp,ls,s[i],s[j])
                    continue
                if self.is_successor(s[i], s[j]):
                    # print("Q")
                    dp[i] = max(dp[i], dp[j] + 1)
                    ans = max(ans, dp[i])
        # print(words, dp)
        return ans


s = Solution()
assert(s.is_successor([1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == False)
assert(s.is_successor([1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == True)
assert(s.is_successor([1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == False)
assert(s.is_successor([1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == True)

assert(s.longestStrChain(["a","b","ba","bca","bda","bdca"]) == 4)
assert(s.longestStrChain(["a","b"]) == 1)
assert(s.longestStrChain(["a","b","ba","bca","bda","bdca"]) == 4)
assert(s.longestStrChain([]) == 1)
assert(s.longestStrChain(["ksqvsyq","ks","kss","czvh","zczpzvdhx","zczpzvh","zczpzvhx","zcpzvh","zczvh","gr","grukmj","ksqvsq","gruj","kssq","ksqsq","grukkmj","grukj","zczpzfvdhx","gru"]) == 7)


