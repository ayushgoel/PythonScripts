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
        ans = []
        while len(q) > 0:
            n, lvl = q.pop(0)
            if n.left is not None:
                q.append((n.left, lvl+1))
            if n.right is not None:
                q.append((n.right, lvl+1))
            if lvl >= len(ans):
                ans += [[]]
            ans[lvl] += [n.val]
        return ans
