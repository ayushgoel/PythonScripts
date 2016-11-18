# https://www.interviewbit.com/problems/combination-sum/

class Solution:
    def n_combinationSum(self, A, B, values_greater_than_equal_to):
        # print(A, B)
        if B < 0:
            return -1
        if B == 0:
            return []
        final_ans = []
        for i in A:
            if i < values_greater_than_equal_to:
                continue
            smaller_ans = self.n_combinationSum(A, B-i, i)
            if smaller_ans == -1:
                # print("CONTINUE")
                continue
            elif smaller_ans == []:
                # found solution
                final_ans += [[i]]
            else:
                for j in smaller_ans:
                    y = j + [i]
                    if not y in final_ans:
                        final_ans += [sorted(y)]
                # a combination answer found
        if final_ans == []:
            return -1
        # print ("FINAL", A, B, final_ans)
        return final_ans

    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        newA = sorted(list(set(A)))
        ans = self.n_combinationSum(newA, B, newA[0])
        if ans == -1:
            return []
        else:
            return ans


# x = [2,3,6,7]
# y = 7
# x=  [8, 10, 6, 11, 1, 16, 8]
# y = 28
x=[ 13, 14, 16, 18, 10, 13 ]
y=25
z = Solution()
print(z.combinationSum(x, y))
