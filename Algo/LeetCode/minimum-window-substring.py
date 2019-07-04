class Solution:

    def contains_all(self, small, big):
        for k in small:
            if k not in big or big[k] < small[k]:
                return False
        return True

    def minWindow(self, st: str, t: str) -> str:
        d = {}
        for i in t:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        
        s = 0
        e = 0
        dd = {}
        found = False
        ans = st
        while e != len(st):
            if not self.contains_all(d, dd):
                if st[e] in dd:
                    dd[st[e]] += 1
                else:
                    dd[st[e]] = 1
                e += 1
            
            while self.contains_all(d, dd):
                # print("Q", s, e)
                if len(ans) >= len(st[s:e]):
                    found = True
                    ans = st[s:e]
                dd[st[s]] -= 1
                if dd[st[s]] == 0:
                    del dd[st[s]]
                s += 1
        if not found:
            ans = ''
        return ans


s = Solution()
print(s.minWindow("ADOBECODEBANC", "ABC"))
assert(s.minWindow("ADOBECODEBANC", "ABC") == 'BANC')
# ADOBE CODEB ANC

assert(s.minWindow("ADOBECODEBANC", "ABCQ") == '')
assert(s.minWindow("ADOBECODEBANC", "AB") == 'BA')
assert(s.minWindow("A", "A") == 'A')
