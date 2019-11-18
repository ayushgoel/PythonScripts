class Solution:
    def distributeCandies(self, c: int, n: int):
        x = int((n*(n+1))/2)
        s = 0
        rnds = 0
        while True:
            rnds += 1
            s += (rnds-1)*n*n + x #rnds*x 
            if s >= c:
                break
        ans = [0] * n
        for i in range(1,n+1):
            # print(i, rnds)
            ans[i-1] = i*rnds + n * (int((rnds-1)*rnds/2))
        left = s-c
        idx = n
        # print("R", s, c, rnds)
        while left > 0:
            can_remove = rnds*n + (idx-n)
            # print("Q", can_remove, left, idx)
            if can_remove > left:
                ans[idx-1] -= left
                left = 0
            else:
                ans[idx-1] -= can_remove
                left -= can_remove
            idx -=1
        # print(ans)
        return ans
            

s = Solution()
s.distributeCandies(10, 4)
s.distributeCandies(7, 4)
s.distributeCandies(12, 4)