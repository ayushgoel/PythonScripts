class Node:
    def __init__(self, val):
        self.val = val
        self.leftChild = None
        self.rightChild = None
        
class BST:
    def __init__(self):
        self.root = None

    def setRoot(self, val):
        self.root = Node(val)

    def insert(self, val):
        if(self.root is None):
            self.setRoot(val)
        else:
            self.insertNode(self.root, val)

    def insertNode(self, currentNode, val):
        if val == currentNode.val:
            return
        elif(val < currentNode.val):
            if(currentNode.leftChild):
                self.insertNode(currentNode.leftChild, val)
            else:
                currentNode.leftChild = Node(val)
        elif(val > currentNode.val):
            if(currentNode.rightChild):
                self.insertNode(currentNode.rightChild, val)
            else:
                currentNode.rightChild = Node(val)
    
    def printt(self, n):
        if n is None:
            print "Node is none"
            return
        if n.leftChild is not None:
            print "L"
            self.printt(n.leftChild)
        print "X"
        print n.val
        if n.rightChild is not None:
            print "R"
            self.printt(n.rightChild)

        

    def findGreaterNode(self, currentNode, val):
        if(currentNode is None):
            return None
        if currentNode.val == val:
            x = self.findGreaterNode(currentNode.rightChild, val)
            if x is None:
                return None
            else:
                return x
        elif currentNode.val < val:
            x = self.findGreaterNode(currentNode.rightChild, val)
            if x is None:
                return None
            else:
                return x
        else:
            x = self.findGreaterNode(currentNode.leftChild, val)
            if x is None:
                return currentNode
            else:
                return x



class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextGreater(self, A):
        # if len(A) == 0:
        #     return []
        bst = BST()
        ans = []
        for i in A[::-1]:
            # print i, "TTT"
            # bst.printt(bst.root)
            n = bst.findGreaterNode(bst.root, i)
            if n is None:
                ans += [-1]
            else:
                ans += [n.val]
            bst.insert(i)
            # print i, "EEE"
            # bst.printt(bst.root)
            # print ans
        return ans[::-1]

s = Solution()
assert(s.nextGreater([1,3,2,5,2,8])== [2, 5, 5, 8, 8, -1])
print(s.nextGreater([ 34, 35, 27, 42, 5, 28, 39, 20, 28 ]))