# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def find(self, root, val):
        if root is None:
            return None
        if root.val == val:
            return root
        else:
            t = self.find(root.left, val) 
            if t is not None:
                return t
            t = self.find(root.right, val) 
            return t

    def count(self, root):
        if root is None:
            return 0
        x = 1
        x += self.count(root.left)
        x += self.count(root.right)
        return x


    def btreeGameWinningMove(self, root, n, x):
        t = self.find(root, x)
        cl = self.count(t.left)
        cr = self.count(t.right)
        cp = n-(cl+cr+1)
        if (cl > (cr+cp+1)) or (cr > (cl+cp+1)) or (cp > (cr+cl+1)):
            return True
        return False

s = Solution()
r = TreeNode(1)
r.left = TreeNode(2)
r.right = TreeNode(3)
r.left.left = TreeNode(4)
r.right.right = TreeNode(5)
print(s.btreeGameWinningMove(r, 5, 2))
print(s.btreeGameWinningMove(r, 5, 1))