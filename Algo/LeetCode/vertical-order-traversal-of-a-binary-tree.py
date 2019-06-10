## Python 2.7
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        d = {}
        q = [(root, 0, 0)] #node, vertical_level, horizontal_level
        while len(q) != 0:
            n = q.pop(0)
            if n[1] in d:
                d[n[1]] += [[n[0].val, n[2]]]
            else:
                d[n[1]] = [[n[0].val, n[2]]]
            if n[0].left:
                q.append((n[0].left, n[1]-1, n[2]+1))
            if n[0].right:
                q.append((n[0].right, n[1]+1, n[2]+1))
        # print(d)
        ans = []
        lowest = min(d.keys())
        highest = max(d.keys())
        def my_cmp(x, y):
            if x[1] < y[1]:
                return -1
            elif x[1] > y[1]:
                return 1
            else:
                return 1 if x[0]>y[0] else -1
        for i in range(lowest, highest+1):
            # print(i, [k.val for k in d[i]])
            p = sorted(d[i], cmp=my_cmp)
            ans.append([k[0] for k in p])
        return ans
