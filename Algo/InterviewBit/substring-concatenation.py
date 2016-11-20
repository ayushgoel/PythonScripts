# https://www.interviewbit.com/problems/substring-concatenation/

class Solution:

    def create_dict(self, s, part_len):
        ans = {}
        # print("Y", s, part_len)
        for i in xrange(0, len(s), part_len):
            x = s[i:i+part_len]
            if ans.has_key(x):
                ans[x] += 1
            else:
                ans[x] = 1
        return ans

    # @param A : string
    # @param B : tuple of strings
    # @return a list of integers
    def findSubstring(self, A, B):
        B_part_len = len(B[0])
        B_string = ''.join(B)
        B_string_len = len(B_string)
        all_keys_dict = self.create_dict(B_string, B_part_len)

        ans = []
        for i in xrange(0, len(A) - B_string_len + 1):
            current_s = A[i: i+B_string_len]
            current_s_dict = self.create_dict(current_s, B_part_len)
            # print("X", current_s, all_keys_dict, current_s_dict)
            if current_s_dict == all_keys_dict:
                ans += [i]

        return ans

s = Solution()
# string = "barfoothefoobarman"
# string_strings = "foo", "bar"
string = "helhelhtmlhelhel"
string_strings = "hel", "hel"
print(s.findSubstring(string, string_strings))
