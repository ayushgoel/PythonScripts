# WA
    # def maxProductingStartingAtFirstElement(self, nums):
    #     prod = nums[0]
    #     for i in nums[1:]:
    #         new_prod = prod * i
    #         if new_prod < prod:
    #             return prod
    #         else:
    #             prod = new_prod
    #     return prod

    # def minProductStartingAtFirstElement(self, nums):
    #     prod = nums[0]
    #     for i in nums[1:]:
    #         new_prod = prod * i
    #         if new_prod > prod:
    #             return prod
    #         else:
    #             prod = new_prod
    #     return prod

    # def maxProduct(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     if len(nums) == 0:
    #         return 0
    #     if len(nums) == 1:
    #         return nums[0]

    #     a = nums[0]
    #     b=0
    #     if a >= 0:
    #         b = self.maxProductingStartingAtFirstElement(nums[1:]) * a
    #     else:
    #         b = self.minProductStartingAtFirstElement(nums[1:]) * a
    #     c = self.maxProduct(nums[1:])
    #     print nums, a, b, c
    #     return max(a,b,c)

# O (n**2)

# class Solution(object):
#     def maxProduct(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         nl = len(nums)
#         if nl == 0:
#             return 0
#         dp = [[0 for i in xrange(nl)] for j in xrange(nl)]
#         dp[0][0] = nums[0]
#         ans = nums[0]
#         for i in xrange(1, nl):
#             dp[0][i] = dp[0][i-1] * nums[i]
#             if dp[0][i] > ans:
#                 ans = dp[0][i]
#         for i in xrange(1, nl):
#             for j in xrange(i, nl):
#                 # print i,j
#                 if j == i:
#                     dp[i][j] = nums[i]
#                 elif j > i:
#                     dp[i][j] = dp[i][j-1] * nums[j]
#                 if dp[i][j] > ans:
#                     ans = dp[i][j]

#         # for i in dp:
#         #     print i
#         return ans

NINF = -(2**32)
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # print nums
        if len(nums) == 0:
            return NINF
        try:
            ind0 = nums.index(0)
            return max(0, self.maxProduct(nums[:ind0]), self.maxProduct(nums[ind0+1:]))
        except ValueError:
            pass

        num_of_ngs = 0
        left_neg = None
        right_neg = None
        for ind, i in enumerate(nums):
            if i < 0:
                num_of_ngs += 1
                if left_neg is None:
                    left_neg = ind
                else:
                    right_neg = ind

        # print num_of_ngs, left_neg, right_neg
        if num_of_ngs %2 == 0:
            return reduce(lambda x, y: x * y, nums)
        if left_neg is not None and right_neg is not None:
            a = self.maxProduct(nums[:left_neg])
            c = self.maxProduct(nums[left_neg+1:])
            b = self.maxProduct(nums[:right_neg])
            d = self.maxProduct(nums[right_neg+1:])
            return max(a,b,c,d)
            # if nums[left_neg] < nums[right_neg]:
            #     return reduce(lambda x, y: x * y, nums[:right_neg])
            # else:
            #     return reduce(lambda x, y: x * y, nums[left_neg+1:])
        elif left_neg is not None:
            a = self.maxProduct(nums[:left_neg])
            c = self.maxProduct(nums[left_neg+1:])
            return max(a,c,nums[left_neg])
        assert("How did we reach here?")

s = Solution()
print s.maxProduct([2,3,-2,4]) #6
print s.maxProduct([-3]) #-3
print s.maxProduct([-3,-2]) #6
print s.maxProduct([2,4]) #8
print s.maxProduct([2,-3,-2,4]) #48
print s.maxProduct([-4,-3,-2]) #12
print s.maxProduct([-1,-2,-9,-6]) #108
print s.maxProduct([-3,0,1,-2]) #1
print s.maxProduct([2,-5,-2,-4,3]) #24