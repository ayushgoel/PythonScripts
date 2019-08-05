class Solution:
    def movesToMakeZigzag(self, nums):
        even = 0
        for i in range(0, len(nums), 2):
            x = 0
            if (i!= len(nums)-1 and nums[i] >= nums[i+1]):
                x = nums[i]-nums[i+1]+1
            if (i!=0 and nums[i] >= nums[i-1]):
                x = max(x, nums[i]-nums[i-1]+1)
            even += x
        odd = 0
        for i in range(1, len(nums), 2):
            x = 0
            if (i!= len(nums)-1 and nums[i] >= nums[i+1]):
                x = nums[i]-nums[i+1]+1
            if (i!=0 and nums[i] >= nums[i-1]):
                x = max(x, nums[i]-nums[i-1]+1)
            odd += x
        # print(even, odd)
        return min(even, odd)

s = Solution()
print(s.movesToMakeZigzag([1,2,3])) # 2
print(s.movesToMakeZigzag([9,6,1,6,2])) # 4
print(s.movesToMakeZigzag([10,4,4,10,10,6,2,3])) # 13
# 7 