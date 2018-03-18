class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        sum_gas = sum(gas)
        sum_cost = sum(cost)
        if sum_cost>sum_gas:
            return -1
        if len(gas) == 1:
            return 0
        t = [gas[i]-cost[i] for i in xrange(len(gas))]

        ind = 0
        p = t[-1] - t[0]
        print t
        for i in xrange(1,len(t)):
            if (t[i-1] - t[i]) < p:
                print i, p
                p = t[i-1] - t[i]
                ind = i
        return ind

s = Solution()
print s.canCompleteCircuit([6,1,4,3,5], [3,8,2,4,2])
print s.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2])
print s.canCompleteCircuit([1,2], [2,1])