# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    
    def ser(self, root, ind, arr):
        # print(ind, arr)
        if root is None:
            return
        arr[ind] = str(root.val)
        self.ser(root.left, 2*ind, arr)
        self.ser(root.right, (2*ind)+1, arr)
    
    def height(self, root):
        if root is None:
            return 0
        return (1+max(self.height(root.left), self.height(root.right)))

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        h = self.height(root)
        # print(h)
        arr = ["null"] * (2**h)
        self.ser(root, 1, arr)
        return ",".join(arr)
        
    def dser(self, ind, arr):
        if ind >= len(arr) or arr[ind] == "null":
            return None
        nd = TreeNode(int(arr[ind]))
        nd.left = self.dser(2*ind, arr)
        nd.right = self.dser((2*ind)+1, arr)
        return nd

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        ns = data.split(",")
        return self.dser(1, ns)
            
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))