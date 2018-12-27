class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        # if nums[0]<nums[1]<nums[2]:
        #     return True
        n1 = nums[0]
        n2 = None
        n3 = None
        #n3<n1
        #n1<n2
        for i in xrange(1, len(nums)):
            t = nums[i]
            # print n1, n2, n3, t
            if t > n1:
                if n2 is None:
                    n2 = t
                    continue
                else:
                    if t < n2:
                        n2 = t
                        continue
                    elif t > n2:
                        print n1, n2, t
                        return True
            else:
                if t == n1:
                    if n3 is not None and n3<t:
                        n1 = n3
                        n2 = t
                        n3 = None
                if n3 is None:
                    n3 = t
                    continue
                else:
                    if t > n3:
                        n1 = n3
                        n2 = t
                        n3 = None
                    else:
                        n3 = t
        return False


s = Solution()
print s.increasingTriplet([1,2,3,4,5])
print s.increasingTriplet([3,5,4,2,6])
print s.increasingTriplet([3,5,4,0,1,2])
print s.increasingTriplet([3,5,4,0,7])

print s.increasingTriplet([1,2,0])
print s.increasingTriplet([3,5,4,2,1])
print s.increasingTriplet([3,5,4,0,1,-1])
print s.increasingTriplet([3,5,4,0,2])

print s.increasingTriplet([1,2,2,1])

print s.increasingTriplet([1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2])