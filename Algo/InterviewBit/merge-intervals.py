# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    def __repr__(self):
        return "{0}-{1}".format(self.start, self.end)

class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, n):
        ans = []
        inserted = False
        for i in intervals:
            if (i.start <= n.start and i.end >= n.start) or (i.start <= n.end and i.end >= n.end) or (i.start >= n.start and i.end <= n.end):
                n = Interval(min(i.start, n.start), max(i.end, n.end))
            else:
                if not inserted and (i.start > n.end):
                    ans += [n]
                    inserted = True
                ans += [i]
        if not inserted:
            ans += [n]
        return ans
                
s = Solution()
x = s.insert([Interval(i[0],i[1]) for i in [[3,5], [8,10]]], Interval(1,12))
print(x)
x = s.insert([Interval(i[0],i[1]) for i in [[1,2], [3,5], [6,8], [10,12]]], Interval(7,9))
print(x)
# x = s.insert([Interval(i[0],i[1]) for i in [(29823256, 32060921), (33950165, 36418956), (37225039, 37785557), (40087908, 41184444), (41922814, 45297414), (48142402, 48244133), (48622983, 50443163), (50898369, 55612831), (57030757, 58120901), (59772759, 59943999), (61141939, 64859907), (65277782, 65296274)]], Interval(36210193, 61984219))
# print(x)
# assert(x == [Interval(i[0],i[1]) for i in [(6037774, 6198243), (6726550, 7004541), (8842554, 10866536), (11027721, 11341296), (11972532, 14746848), (16374805, 16706396), (17557262, 20518214), (22139780, 22379559), (27212352, 28404611), (28921768, 29621583), (29823256, 32060921), (33950165, 64859907), (65277782, 65296274), (67497842, 68386607), (70414085, 73339545), (73896106, 75605861), (79672668, 84539434), (84821550, 86558001), (91116470, 92198054), (96147808, 98979097)]])

