class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):
        if len(A) == 0:
            return 0
        a = set(A)
        ans = 0
        for i in A:
            if i-1 not in a:
                cnt = 0
                j = i
                while j in a:
                    cnt += 1
                    j += 1
                if cnt > ans:
                    ans = cnt
                # print(i, cnt, ans)
        return ans

s = Solution()
print(s.longestConsecutive([ 97, 86, 67, 19, 107, 9, 8, 49, 23, 46, -4, 22, 72, 4, 57, 111, 20, 52, 99, 2, 113, 81, 7, 5, 21, 0, 47, 54, 76, 117, -2, 102, 34, 12, 103, 69, 36, 51, 105, -3, 33, 91, 37, 11, 48, 106, 109, 45, 58, 77, 104, 60, 75, 90, 3, 62, 16, 119, 85, 63, 87, 43, 74, 13, 95, 94, 56, 28, 55, 66, 92, 79, 27, 42, 70 ]))