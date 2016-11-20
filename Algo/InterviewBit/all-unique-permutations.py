# https://www.interviewbit.com/problems/all-unique-permutations/

class Solution:
    def remove_dupes(self, arr):
        # Get list of list of integers
        # return list of list of integers, with duplicates removed.
        no_dupes = set()
        ans = []
        for i in arr:
            strarr = [str(j) for j in i]
            stri = ':'.join(strarr)
            if stri in no_dupes:
                continue
            else:
                no_dupes.add(stri)
                ans += [i]
        return ans

    def get_all_permutations(self, arr):
        # input - list of integers
        # return list of list of integers of permutation, all unique
        if len(arr) < 1:
            return []
        if len(arr) == 1:
            return [arr]
        arr_without_first_number = arr[1:]
        arr_without_first_number_perms = self.get_all_permutations(arr_without_first_number)
        # print("A", arr_without_first_number_perms)
        arr_without_first_number_perms = self.remove_dupes(arr_without_first_number_perms)
        # print("B", arr_without_first_number_perms)
        perms = []
        for permutation in arr_without_first_number_perms:
            for i in xrange(len(permutation) + 1):
                res = permutation[:i] + [arr[0]] + permutation[i:]
                perms += [res]
        return perms

    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        return self.remove_dupes(self.get_all_permutations(A))

s = Solution()
inp = [1, 2, 3]
inp = [1, 1, 2]
# inp = []
inp = [1, 10, 2]
print(s.permute(inp))
