digits = set("0123456789")
class Solution:
    def decodeString(self, s: str) -> str:
        # print("STR", s)
        pre = ""
        cnt = ""
        rep = ""
        brstack = []
        endIndex = -1
        for ind, i in enumerate(s):
            # print(brstack, rep)
            if i == '[':
                if len(brstack) > 0:
                    rep += i
                brstack.append(i)
                continue
            if i == ']':
                if len(brstack) > 1:
                    # print(brstack, ind, i)
                    rep += i
                brstack.pop()
                if len(brstack) == 0:
                    endIndex = ind+1
                    break
                continue
            if i in digits:
                if len(brstack) > 0:
                    rep += i
                else:
                    cnt += i
            else:
                if len(brstack) > 0:
                    rep += i
                else:
                    pre += i
        # print(pre, cnt, rep, brstack, endIndex, sep=" X ")
        if rep == "":
            return s
        else:            
            if endIndex == len(s):
                return pre + int(cnt)*self.decodeString(rep)    
            return pre + int(cnt)*self.decodeString(rep) + self.decodeString(s[endIndex:])

s = Solution()

x = s.decodeString("3[a]2[bc]")
print(x)
assert(x == "aaabcbc")

x = s.decodeString("3[a2[c]]")
print(x)
assert(x == "accaccacc")
x = s.decodeString("2[abc]3[cd]ef")
print(x)
assert(x == "abcabccdcdcdef")
x = s.decodeString("3[a]2[bc]")
print(x)
assert(x == "aaabcbc")