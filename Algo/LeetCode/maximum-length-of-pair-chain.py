# class Solution(object):
#     def isBiggerPair(self, a, b):
#         if a is None: return True
#         return a[1] < b[0]
#
#     def findLongestChain(self, pairs):
#         """
#         :type pairs: List[List[int]]
#         :rtype: int
#         """
#         leni = [0] * len(pairs)
#         previ = [None] * len(pairs)
#         for i in xrange(len(pairs)):
#             new_len = 0
#             prev = None
#             change_prev_to = None
#             for j in xrange(i):
#                 if (leni[j] + 1 > new_len):
#                     prev_pair = None
#                     if previ[j] is not None:
#                         prev_pair = pairs[previ[j]]
#                     if self.isBiggerPair(pairs[j], pairs[i]):
#                         print "1", pairs[j], pairs[i]
#                         new_len = leni[j] + 1
#                         prev = j
#                         change_prev_to = None
#                     elif self.isBiggerPair(pairs[i], pairs[j]) and self.isBiggerPair(prev_pair, pairs[i]):
#                         print "2", pairs[j], pairs[i], prev_pair
#                         new_len = leni[j] + 1
#                         prev = previ[j]
#                         change_prev_to = j
#             if new_len == 0:
#                 new_len = 1
#             leni[i] = new_len
#             if prev is not None:
#                 previ[i] = prev
#             if change_prev_to is not None:
#                 previ[change_prev_to] = i
#                 leni[j] = new_len
#                 leni[i] = new_len - 1
#         print leni
#         print previ
#         return max(leni)

class Solution(object):
    def isBiggerPair(self, a, b):
        if a is None: return True
        return a[1] < b[0]


    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs = sorted(pairs, key=lambda x:x[0])
        leni = [0] * len(pairs)
        for i in xrange(len(pairs)):
            for j in xrange(i):
                if (leni[i] < leni[j] + 1) and self.isBiggerPair(pairs[j], pairs[i]):
                    leni[i] = leni[j] + 1
            if leni[i] == 0:
                leni[i] = 1

        # print pairs
        return max(leni)

s = Solution()
print s.findLongestChain([[3,4], [1,2], [2,3]])
print s.findLongestChain([[5,6], [3,4], [1,2], [2,3]])
print s.findLongestChain([[-10,-8],[8,9],[-5,0],[6,10],[-6,-4],[1,7],[9,10],[-4,7]])
