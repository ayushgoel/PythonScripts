# https://www.interviewbit.com/problems/unique-binary-search-trees/

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : integer
    # @return a list of TreeNode
    def generateAllTrees(self, lower, upper): # inclusive
        # print "X", lower, upper
        # if self.cache.has_key((lower, upper)):
        #     return self.cache[(lower, upper)]
        if upper < lower:
            return []
        if upper == lower:
            return [TreeNode(upper)]
        ans = []
        # print "Y", lower, upper
        for i in xrange(lower, upper + 1):
            all_left_nodes = self.generateAllTrees(lower, i-1)
            all_right_nodes = self.generateAllTrees(i+1, upper)
            # print "QQ", i, all_left_nodes, all_right_nodes
            # for TT in all_left_nodes:
            #     # print "Left"
            #     printTree(TT)
            # for TT in all_right_nodes:
            #     # print "Right"
            #     printTree(TT)
            if len(all_left_nodes) == 0:
                for y in all_right_nodes:
                    t = TreeNode(i)
                    t.right = y
                    ans += [t]
            if len(all_right_nodes) == 0:
                for x in all_left_nodes:
                    t = TreeNode(i)
                    t.left = x
                    ans += [t]
            if len(all_left_nodes) != 0 and len(all_right_nodes) != 0:
                for x in all_left_nodes:
                    for y in all_right_nodes:
                        t = TreeNode(i)
                        t.left = x
                        t.right = y
                        ans += [t]
        # print "Cache", self.cache
        # self.cache[(lower, upper)] = ans
        # print "ASD", lower, upper, ans
        return ans


    def generateTrees(self, n):
        # self.cache = {}
        return self.generateAllTrees(1, n)

def printTree(x):
    print x.val
    if x.left is not None:
        print "L"
        printTree(x.left)
    if x.right is not None:
        print "R"
        printTree(x.right)

s=Solution()
x=s.generateTrees(3)
for i in x:
    print "Tree"
    printTree(i)
