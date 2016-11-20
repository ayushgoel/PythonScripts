# https://www.interviewbit.com/problems/all-unique-permutations/

class Solution:
    def all_permutations(self, s):
        if len(s) == 1:
            return set(frozenset(s))
        # calculate all permutations for s[1:] and place s[0] at all possible locations
        # add the generated strings to a set and return the set
        perms = set()
        s_leaving_first_char = s[1:]
        s_leaving_first_char_perms = self.all_permutations(s_leaving_first_char)
        # print("X", s_leaving_first_char, s_leaving_first_char_perms)
        for permutation_frozenset in s_leaving_first_char_perms:
            permutation = iter(permutation_frozenset).next()
            # print("Y", permutation)
            for i in xrange(len(permutation) + 1):
                res = permutation[:i] + s[0] + permutation[i:]
                # print("AA", i, res)
                perms.add(frozenset([res]))
        # print("Z", perms)
        return perms

    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        if len(A) < 1:
            return []
        a = ''.join([str(i) for i in A])
        perms = self.all_permutations(a) # receive a set of strings
        # print(perms)
        return [[int(i) for i in iter(j).next()] for j in perms]

s = Solution()
inp = [1, 2, 3]
inp = [1, 1, 2]
# inp = []
inp = [1, 10, 2]
print(s.permute(inp))
