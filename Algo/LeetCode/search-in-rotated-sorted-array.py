class Solution:
    def find_pivot(self, nums):
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            return 1 if nums[0] > nums[1] else 0
        if len(nums) == 3:
            return nums.index(min(nums))
        
        mid = len(nums) / 2
        if nums[mid]>nums[0]:
            if nums[-1] > nums[mid]:
                return 0
            else:
                return mid + self.find_pivot(nums[mid:])
        else:
            return self.find_pivot(nums[:mid+1])
            
        
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ln = len(nums)
        if ln == 0:
            return -1
        if ln == 1:
            return 0 if nums[0] == target else -1
        pivot = self.find_pivot(nums)
        
        start = pivot
        end = (start - 1) if (start != 0) else (ln-1)

        while True:
            s=0
            e=(end-start+ln)%ln
            m=(e+s)/2

            mid = (start + m) %ln
            #((((start + end) / 2)%ln) +start) % ln

            # print start, mid, end, ln
            if end-start == 1 or (start == end):
                if nums[start] == target:
                    return start
                elif nums[end] == target:
                    return end
                else:
                    return -1
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = (mid + 1) %ln
            else:
                end = (mid - 1) %ln

            if start-end == 1:
                if nums[start] == target:
                    return start
                elif nums[end] == target:
                    return end
                else:
                    return -1

        return -2

        
s = Solution()
# print s.find_pivot([1,2,3,4,5,6])
# print s.find_pivot([4,5,6,1,2,3])
# print s.find_pivot([2,3,4,5,6,1])
print s.search([2,3,4,5,6,1], 4) # 2
print s.search([2,3,4,5,6,1], 1) # 5
print s.search([2,3,4,5,6,1], 6) # 4
print s.search([2,3,4,5,6,1], 2) # 0
print s.search([2,3,4,5,6,1], 7) # -1
print s.search([1], 1) # 0
print s.search([1], 0) # -1
print s.search([1,3], 0) # -1
print s.search([3,1], 0) # -1