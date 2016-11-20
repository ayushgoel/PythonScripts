# https://www.interviewbit.com/problems/colorful-number/

class Solution:
    # @param A : integer
    # @return an integer
    def colorful(self, a):
        stra = str(a)
        all_products = set()
        for l in xrange(1, len(stra)+1):
            # print(l)
            for i in xrange(len(stra)-l+1):
                subsa = stra[i:i+l]
                subsa_int = [int(j) for j in subsa]
                subsa_multiply_ans = reduce(lambda x,y: x*y, subsa_int)
                if subsa_multiply_ans in all_products:
                    return 0
                all_products.add(subsa_multiply_ans)
                # print("X",subsa)
        return 1


s = Solution()
print(s.colorful(23))
