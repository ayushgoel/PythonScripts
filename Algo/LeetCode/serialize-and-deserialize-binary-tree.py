
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ""
        enc = [str(root.val)]
        q = [root]
        while len(q) != 0:
            n = q.pop(0)
            if n.left is not None:
                enc.append(str(n.left.val))
                q.append(n.left)
            else:
                enc.append("null")

            if n.right is not None:
                enc.append(str(n.right.val))
                q.append(n.right)
            else:
                enc.append("null")
        return ",".join(enc)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None
        dec = data.split(",")
        root = TreeNode(int(dec[0]))
        q=[root]
        ind  = 1
        while len(q)!=0:
            n = q.pop(0)
            if dec[ind] != "null":
                t = TreeNode(int(dec[ind]))
                n.left = t
                q.append(t)
            ind += 1
            if dec[ind] != "null":
                t = TreeNode(int(dec[ind]))
                n.right = t
                q.append(t)
            ind += 1
        return root


        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

n = TreeNode(2)
n.left = TreeNode(1)
n.right = TreeNode(3)
n.right.right = TreeNode(4)

c = Codec()
a = c.serialize(n)
assert(a == "2,1,3,null,null,null,4,null,null")

b = c.deserialize(a)
assert(b.val == 2)
assert(b.left.val == 1)
assert(b.right.val == 3)
assert(b.right.right.val == 4)
assert(b.right.right.left == None)

print(c.serialize(None))
print(c.deserialize(c.serialize(None)))
