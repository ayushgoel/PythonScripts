class Solution:
    def maxSlidingWindow(self, nums, k):
        ln = len(nums)
        if k > ln:
            return []
        q = []
        ans = []
        for i in range(ln):
            # print(i,q)
            if len(q) == 0:
                q.append(i)
            if q[0] <= (i-k):
                q.pop(0)
            while len(q) > 0 and nums[q[-1]] <= nums[i]:
                q.pop(-1)
            q.append(i)
            # print(i,q)
            if i >= k-1:
                ans += [nums[q[0]]]
            # print("A", i,ans)
        # ans += [nums[q[0]]]
        return ans



        
s = Solution()
assert(s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7])
assert(s.maxSlidingWindow([1,2], 3) == [])
assert(s.maxSlidingWindow([1,2,3], 3) == [3])
assert(s.maxSlidingWindow([5,4,3,2,1], 2) == [5,4,3,2])
assert(s.maxSlidingWindow([5,4,3,2,1], 2) == [5,4,3,2])
# x = s.maxSlidingWindow([1], 1)
# print(x)
assert(s.maxSlidingWindow([1], 1) == [1])
assert(s.maxSlidingWindow([1,2,3,4,5], 1) == [1,2,3,4,5])