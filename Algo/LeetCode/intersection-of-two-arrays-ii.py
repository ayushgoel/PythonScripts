class Solution:
    def intersect(self, nums1, nums2):
        # print(nums1, nums2)
        n1 = None
        n2 = None
        if len(nums1) < len(nums2):
            n1 = sorted(nums1)
            n2 = sorted(nums2)
        else:
            n1 = sorted(nums2)
            n2 = sorted(nums1)
        # print(n1, n2)
        
        ans = []
        ptr = 0
        for i in range(len(n1)):
            while ptr < len(n2) and n1[i] > n2[ptr]:
                ptr += 1
            if ptr == len(n2):
                break
            if n1[i] == n2[ptr]:
                ans += [n1[i]]
                ptr += 1
        return ans


s = Solution()
assert(s.intersect([],[]) == [])
assert(s.intersect([],[1]) == [])
assert(s.intersect([1],[]) == [])
assert(s.intersect([1,2],[3,4]) == [])
assert(s.intersect([],[]) == [])
assert(s.intersect([4,9,5],[9,4,9,8,4]) == [4,9])
