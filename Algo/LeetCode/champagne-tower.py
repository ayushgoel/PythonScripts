class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        volume = [[0] * 100 for i in xrange(100)]
        ofv = [[0] * 100 for i in xrange(100)]
        # print volume, ofv
        if poured > 1:
            volume[0][0] = 1
            ofv[0][0] = poured - 1
        else:
            volume[0][0] = poured
            ofv[0][0] = 0
        # print "T", volume[0][0], ofv[0][0]
        for row in xrange(1,100):
            for glass in xrange(row+1):
                assert(row>=1)
                if glass>0:
                    assert(glass>=1)
                    volume[glass][row] += ofv[glass-1][row-1] / 2.0
                # print "Q", glass, row, ofv[glass][row-1]
                volume[glass][row] += ofv[glass][row-1] / 2.0
                if volume[glass][row] > 1:
                    ofv[glass][row] = volume[glass][row] - 1
                    volume[glass][row] = 1
                else:
                    ofv[glass][row] = 0
                # print glass, row, volume[glass][row], ofv[glass][row]
        # for i in xrange(5):
        #     print volume[i][:10], ofv[i][:10]
        return volume[query_glass][query_row]


s = Solution()
print s.champagneTower(1, 1, 1)
print s.champagneTower(2, 1, 1)
print s.champagneTower(2, 2, 0)
print s.champagneTower(50, 2, 1)