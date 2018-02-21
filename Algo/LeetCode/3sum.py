class Solution(object):
    def twoSum(self, nums, s):
        if len(nums) < 2:
            return []
        i = 0
        j = len(nums) - 1
        ans = []
        while i < j:
            # print i, j, s, nums
            sumx = nums[i] + nums[j]
            if sumx == s:
                ans += [[nums[i], nums[j]]] # handle case of repeated numbers
                t = nums[i]
                while i < len(nums) and nums[i] == t:
                    i += 1
            elif sumx > s:
                j -= 1
            else:
                i += 1
        return ans

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        ans = []
        for i in xrange(len(nums)):
            a1 = nums[i]
            if a1 > 0:
                break
            if i > 0 and a1 == nums[i-1]:
                continue
            all_ans = self.twoSum(nums[i+1:], -a1)
            # print "T", all_ans
            for j in all_ans:
                ans += [[a1, j[0], j[1]]]
        return ans

s = Solution()
print "X", s.threeSum([-1, 0, 1, 2, -1, -4])
print "X", s.threeSum([0,0])
print "X", s.threeSum([2,5,3,4,-7])
