class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #print nums
        if len(nums) < 3:
            return 0
        cur_min = nums[0]
        cur_max = nums[0]
        left_min = [cur_min]
        left_max = [cur_max]

        for num in nums[1:]:
            if num < cur_min:
                cur_min = num
            left_min += [cur_min]

            if num > cur_max:
                cur_max = num
            left_max += [cur_max]
        #print left_min
        #print left_max

        nums = nums[::-1]
        cur_min = nums[0]
        cur_max = nums[0]
        right_min = [cur_min]
        right_max = [cur_max]

        for num in nums[1:]:
            if num < cur_min:
                cur_min = num
            right_min += [cur_min]

            if num > cur_max:
                cur_max = num
            right_max += [cur_max]

        nums = nums[::-1]
        right_min = right_min[::-1]
        right_max = right_max[::-1]

        #print right_min
        #print right_max

        ans = None

        for i in xrange(1, len(nums) -1):
            a = nums[i] * left_min[i-1] * right_min[i+1]
            b = nums[i] * left_min[i-1] * right_max[i+1]
            c = nums[i] * left_max[i-1] * right_min[i+1]
            d = nums[i] * left_max[i-1] * right_max[i+1]
            if ans is None:
                ans = max(a,b,c,d)
            else:
                ans = max(ans, max(a,b,c,d))
        return ans

s = Solution()
print s.maximumProduct([2,3,6,1,-1,-5,-2,4])
print s.maximumProduct([-5,-2,4]) #40
print s.maximumProduct([1,2,3,4]) #24
print s.maximumProduct([1,-1,3,0]) #0
print s.maximumProduct([1,2,-3,-4]) #24