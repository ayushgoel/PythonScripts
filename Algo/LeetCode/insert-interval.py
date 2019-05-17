#!/usr/bin/env python3

class Solution:
    def insert(self, intervals, newInterval):
        if len(intervals) == 0:
            return [newInterval]
        ans = []
        ni = newInterval
        added = False
        if ni[1] < intervals[0][0]:
            ans += [ni]
            added = True
        for i in intervals:
            if i[0] > newInterval[1]:
                if added == False:
                    ans += [ni]
                    added = True
            if i[1]<newInterval[0] or i[0] > newInterval[1]:
                ans += [i]
            else:
                if i[1] >= ni[0]:
                    ni = [min(i[0], ni[0]), ni[1]]
                if i[0] <= ni[1]:
                    ni = [ni[0], max(i[1],ni[1])]
        if added == False:
            ans += [ni]
        return ans

s = Solution()
assert(s.insert([], [1,2]) == [[1,2]])
assert(s.insert([[8,9]], [4,6]) == [[4,6], [8,9]])
assert(s.insert([[1,2]], [4,6]) == [[1,2], [4,6]])
assert(s.insert([[1,2], [3,5],[8,9]], [4,6]) == [[1,2],[3,6], [8,9]])
assert(s.insert([[3,5],[12,15]], [6,6]) == [[3,5],[6,6],[12,15]])
assert(s.insert([[1,5]], [0,0]) == [[0,0],[1,5]])
