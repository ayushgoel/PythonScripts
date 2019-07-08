import bisect

class Solution:

    def find_pos(self, arr, val):
        # print("Q",arr, val)
        s = 0
        e = len(arr)-1
        while True:
            m = int((s+e)/2)
            # print(m)
            if val >= arr[m] and ((m+1 == len(arr)) or (val < arr[m+1])):
                return m+1
            elif val <= arr[m] and m==0:
                return 0
            elif val > arr[m]:
                s = m+1
            else:
                e = m-1


    # @param A : list of integers
    # @return an integer
    def countInversions(self, A):
        if len(A) == 0:
            return 0
        d = [A[0]]
        ans = 0
        for i in range(1,len(A)):
            # ind = self.find_pos(d, A[i]) # find pos in d
            ind = bisect.bisect(d,A[i])
            # print(A[i],ind)
            ans += (i - ind)
            d.insert(ind, A[i])
            # d = d[:ind] + [A[i]] + d[ind:]
        # print(ans)
        return ans



s = Solution()
# s.countInversions([8,9,7])
# # 1 1 
# assert(s.countInversions([2, 4, 1, 3, 5]) == 3)
assert(s.countInversions([ 84, 2, 37, 3, 67, 82, 19, 97, 91, 63, 27, 6, 13, 90, 63, 89, 100, 60, 47, 96, 54, 26, 64, 50, 71, 16, 6, 40, 84, 93, 67, 85, 16, 22, 60 ]) == 290)