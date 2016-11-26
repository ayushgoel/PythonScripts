# https://www.interviewbit.com/problems/largest-number/

class Solution:
    def comparator_function(self, a, b):
        str_a = str(a)
        str_b = str(b)
        num_1 = int(str_a + str_b)
        num_2 = int(str_b + str_a)
        if num_1 > num_2:
            return -1
        elif num_1 == num_2:
            return 0
        return 1

    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        a = list(A)
        a.sort(cmp=self.comparator_function)
        return str(int(''.join([str(i) for i in a])))

s = Solution()
inp = [3, 30, 34, 5, 9]
inp = [472, 663, 964, 722, 485, 852, 635, 4, 368, 676, 319, 412]
# inp = [472, 485, 4, 412]
print(s.largestNumber(inp))
