
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if root is None:
            return 0
        ans = 0
        if root.val %2 == 0:
            if root.left is not None:
                if root.left.left is not None:
                    ans += root.left.left.val
                if root.left.right is not None:
                    ans += root.left.right.val
            if root.right is not None:
                if root.right.left is not None:
                    ans += root.right.left.val
                if root.right.right is not None:
                    ans += root.right.right.val
        return ans + self.sumEvenGrandParent(root.left) + self.sumEvenGrandParent(root.right)

s = Solution()