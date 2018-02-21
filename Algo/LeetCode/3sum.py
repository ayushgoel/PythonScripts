class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        num_len = len(nums)
        ans = []
        for i in xrange(len(nums)-2):
            a1 = nums[i]
            if a1 > 0:
                break
            if i > 0 and a1 == nums[i-1]:
                continue
            l = i+1
            r = num_len - 1
            while l < r:
                # print i, j, s, nums
                sumx = nums[l] + nums[r]
                if sumx == -a1:
                    ans += [[a1, nums[l], nums[r]]]
                    t = nums[l]
                    while l < r and nums[l] == t:
                        l += 1
                elif sumx > -a1:
                    r -= 1
                else:
                    l += 1
        return ans

s = Solution()
print "X", s.threeSum([-1, 0, 1, 2, -1, -4])
print "X", s.threeSum([0,0])
print "X", s.threeSum([2,5,3,4,-7])
