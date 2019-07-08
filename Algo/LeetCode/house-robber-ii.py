class Solution:
    def rob_avoiding(self, nums, ind):
        nums = nums[ind+1:] + nums[:ind]
        if len(nums) < 3:
            return max(nums)
        dp = [0]*(len(nums))
        dp[0] = nums[0]
        dp[1] = nums[1]
        for i in range(2, len(nums)):
            dp[i] = max(dp[:i-1]) + nums[i]
        # print(ind, dp)
        return max(dp)

    def rob(self, nums) -> int:
        if len(nums) == 1:
            return nums[0]
        ans = 0
        for i in range(len(nums)):
            t = self.rob_avoiding(nums, i)
            if ans < t:
                ans = t
        # print(ans)
        return ans

s = Solution()
assert(s.rob([]) == 0)
assert(s.rob([2]) == 2)
assert(s.rob([2,1]) == 2)
assert(s.rob([2,3,2]) == 3)
assert(s.rob([1,2,3,1]) == 4)
assert(s.rob([1,2,3,1,5]) == 8)