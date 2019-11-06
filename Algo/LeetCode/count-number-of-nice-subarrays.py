class Solution:
    def convert(self, nos):
        no = []
        cur = 0
        if nos[0] == -1:
            no += [0]
        for i in range(len(nos)):
            if nos[i] == -1:
                if cur > 0:
                    no += [cur]
                    cur = 0
                no += [-1]
            else:
                cur += 1
        no += [cur]
        return no
        
    def numberOfSubarrays(self, nums, k):
        nos = [1 if nums[i]%2 == 0 else -1 for i in range(len(nums))]
        nums = self.convert(nos)
        s = 0
        e = 0
        cnt = 0
        ans = 0
        # print(nums)
        while e < len(nums):
            if nums[e] == -1:
                cnt += 1
            if cnt == k:
                while nums[s] != -1:
                    s += 1
                # print(s,e)
                x = 0 if nums[s-1] == -1 else nums[s-1]
                y = 0 if nums[e+1] == -1 else nums[e+1]
                ans += (x+1) * (y+1)
                s += 1
                cnt -= 1
            e += 1
        # print(ans)
        return ans




s = Solution()
assert(s.numberOfSubarrays([1,1,2,1,1], 3) == 2)
assert(s.numberOfSubarrays([2,4,6], 1) == 0)
assert(s.numberOfSubarrays([2,2,2,1,2,2,1,2,2,2], 2) == 16)
assert(s.numberOfSubarrays([1], 1) == 1)
assert(s.numberOfSubarrays([0], 1) == 0)