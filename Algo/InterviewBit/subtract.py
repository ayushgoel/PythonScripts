class ListNode:
  def __init__(self, x):
      self.val = x
      self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def subtract(self, a):
        if a is None or a.next is None:
            return a
        s = []
        i = a
        i2 = a
        while True:
            if i2 is None or i2.next is None:
                break
            print(i2.val)
            s += [i]
            i = i.next
            if i2.next is not None:
                i2 = i2.next.next
        print(i.val)
        if i2 is not None: # fix for odd
            i = i.next
        for t in range(len(s)-1, -1, -1):
            s[t].val = i.val-s[t].val
            i = i.next
        return a

s = Solution()
ll = ListNode(5)
ll.next = ListNode(9)
ll.next.next = ListNode(7)
ll2 = s.subtract(ll)
while ll2 is not None:
    print(ll2.val)
    ll2 = ll2.next