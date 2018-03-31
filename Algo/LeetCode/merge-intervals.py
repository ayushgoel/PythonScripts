# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    def __repr__(self):
        return "{0}-{1}".format(self.start, self.end)
    def __str__(self):
        return "{0}-{1}".format(self.start, self.end)

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return intervals

        def interval_key(interval):
            return interval.start
        intervals = sorted(intervals, key=interval_key)
        ans = []
        cur = intervals[0]
        for i in xrange(1,len(intervals)):
            interval = intervals[i]
            if interval.start <= cur.end:
                if interval.end > cur.end:
                    cur.end = interval.end
            else:
                ans += [cur]
                cur = interval
        ans += [cur]
        return ans

s = Solution()
print s.merge([Interval(1,3), Interval(5,8), Interval(2,6), Interval(9,10),Interval(10,11)])