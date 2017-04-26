# https://www.interviewbit.com/problems/copy-list/

# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        old_to_new = {}
        x = head
        while x != None:
            n = RandomListNode(x.label)
            old_to_new[x] = n
            x = x.next

        x = head
        while x != None:
            n = old_to_new[x]
            if x.next:
                n.next = old_to_new[x.next]
            if x.random:
                n.random = old_to_new[x.random]
            x = x.next

        return old_to_new[head]

def printnode(x):
    while x:
        print x.label, x.next.label, x.random.label
        x = x.next

s=Solution()
a = RandomListNode(1)
b = RandomListNode(2)
a.next = b
b.random = a
printnode(a)
printnode(copyRandomList(a))