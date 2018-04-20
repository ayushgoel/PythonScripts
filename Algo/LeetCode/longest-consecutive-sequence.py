class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set_nums = set(nums)
        ans = 0
        for i in nums:
            if i-1 not in set_nums:
                pos_ans = 0
                j = i
                while True:
                    if j in set_nums:
                        pos_ans += 1
                        j += 1
                    else:
                        if pos_ans > ans:
                            ans = pos_ans
                        break
        return ans

s = Solution()
assert(s.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4)
assert(s.longestConsecutive([100, 4, 200, 1, 2]) == 2)
assert(s.longestConsecutive([]) == 0)
assert(s.longestConsecutive([5,4,3,2,1]) == 5)
