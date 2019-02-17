#! /usr/bin/env python3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: 'TreeNode') -> 'List[List[int]]':
        if root is None:
            return []
        q=[(root,0)]
        cur = 0
        while True:
            if cur >= len(q):
                break
            # print(cur, len(q))
            n, lvl = q[cur]
            if n.left is not None:
                q.append((n.left, lvl+1))
            if n.right is not None:
                q.append((n.right, lvl+1))
            cur += 1
        # print([[i[0].val, i[1]] for i in q])
        ans = []
        for i in q:
            if i[1] >= len(ans):
                ans += [[]]
            ans[i[1]] += [i[0].val]
        return ans
            
        