class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def twoSum(self, A, B):
        ans = []
        value_set = set()
        value_index_dict = {}
        for index, val in enumerate(A):
            if B-val in value_set:
                ans += [sorted([index, value_index_dict[B-val]])]
            value_set.add(val)
            if value_index_dict.has_key(val):
                value_index_dict[val] = min(index, value_index_dict[val])
            else:
                value_index_dict[val] = index
        # print ans
        if len(ans) > 0:
            final_ans = sorted(ans, key=lambda x: (x[1], x[0]))[0]
            return [i+1 for i in final_ans]
        return []


s = Solution()
print (s.twoSum((1,2,3,4,5,6), 4))
print (s.twoSum((1,2,3,4,5,6), 5))
print (s.twoSum((1,2,3,4,5,6), 2))
print (s.twoSum((4,2,4,4,2,6), 6))
