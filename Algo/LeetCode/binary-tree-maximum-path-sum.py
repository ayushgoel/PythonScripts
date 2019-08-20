# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def ss(self, root): #(ans, max possible that can be connected)
        if root is None:
            return (None, None)
        elif root.left is None and root.right is None:
            return (root.val, root.val)
        elif root.left is None:
            t = self.ss(root.right)
            x = max(root.val, root.val+t[1], t[0])
            y = max(root.val, root.val+t[1])
            return (x,y)
        elif root.right is None:
            t = self.ss(root.left)
            x = max(root.val, root.val+t[1], t[0])
            y = max(root.val, root.val+t[1])
            return (x,y)
        else:
            t1 = self.ss(root.right)
            t2 = self.ss(root.left)
            x = max(root.val, root.val+t1[1], root.val+t2[1], root.val+t1[1]+t2[1], t1[0], t2[0])
            y = max(root.val, root.val+t1[1], root.val+t2[1])
            return (x,y)

    def maxPathSum(self, root: TreeNode) -> int:
        t = self.ss(root)
        return t[0]
        