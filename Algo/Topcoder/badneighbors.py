def maxn(x):
    if len(x) == 0:
        return 0
    return max(x)

class BadNeighbors:
    def maxDonations(self, donations):
        arr1 = [-1] * (len(donations) - 1)
        arr2 = [-1] * (len(donations) - 1)
        arr1[0] = donations[0]
        for i in xrange(1, len(donations) - 1):
            arr1[i] = maxn(arr1[:i-1]) + donations[i]
        print arr1
        donations = donations[1:]
        print donations
        arr2[0] = donations[0]
        for i in xrange(1, len(donations)):
            arr2[i] = maxn(arr2[:i-1]) + donations[i]
        print arr2
        tt = [maxn(arr1), arr2[len(donations) - 1]]
        return maxn(tt)

a = BadNeighbors()
inp = [int(i) for i in ["1","2","3","4","5","1","2","3","4","5"]]
print a.maxDonations(inp)
