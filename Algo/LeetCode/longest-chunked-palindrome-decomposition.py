class Solution:
    def longestDecomposition(self, text: str) -> int:
        if text == "":
            return 0
        for i in range(1,int(len(text)/2)+1):
            if text[:i] == text[-i:]:
                return 2+ self.longestDecomposition(text[i:-i])
        return 1

s=Solution()
print(s.longestDecomposition("aaa"))
print(s.longestDecomposition("antaprezatepzapreanta"))
print(s.longestDecomposition("merchant"))
print(s.longestDecomposition("ghiabcdefhelloadamhelloabcdefghi"))
