def compare(x, y):
    if x[0] == y[0]:
        if x[1] > y[1]:
            return 1
        else:
            return -1
    else:
        if x[0] > y[0]:
            return -1
        else:
            return 1

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        height_sorted = sorted(people, cmp=compare)
        ans = []
        for i in height_sorted:
            ind = 0
            ans.insert(i[1],i)
        return ans

if __name__ == '__main__':
    s= Solution()
    print s.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])
