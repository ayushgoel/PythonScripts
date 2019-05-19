class Solution:
    def removeDuplicates(self, s: str) -> str:
        ls = len(s)
        remove = [0] * ls
        for i in range(0, ls-1):
            # print(i, s[i], s, remove)   
            if s[i] == s[i+1] and remove[i] != 1 and remove[i+1] != 1:
                remove[i] = remove[i+1] = 1
                j = i-1
                while j >= 0 and remove[j] == 1:
                    j -= 1
                k = i+2
                while j >= 0 and k < ls:
                    if s[j] == s[k] and remove[j] != 1 and remove[k] != 1:
                        remove[j] = remove[k] = 1
                        j -= 1
                        k += 1
                    else:
                        break
        ans = ""
        for i in range(ls):
            if not remove[i]:
                ans += s[i]
        return ans
        
                
s = Solution()
assert(s.removeDuplicates("azxxzy") == "ay")
assert(s.removeDuplicates("zxxz") == "")
assert(s.removeDuplicates("azxx") == "az")
assert(s.removeDuplicates("ay") == "ay")
assert(s.removeDuplicates("ibfjcaffccadidiaidchakchchcahabhibdcejkdkfbaeeaecdjhajbkfebebfea") == "ibfjcdidiaidchakchchcahabhibdcejkdkfbecdjhajbkfebebfea")
assert(s.removeDuplicates("ibfjcaffccad") == "ibfjcd")
assert(s.removeDuplicates("aaaaaaaa") == "")

