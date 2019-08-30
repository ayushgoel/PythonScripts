# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def removeZeroSum(self, head: ListNode):
        prefix_sum = {}
        cur_sum = 0
        p = head

        while p is not None:
            cur_sum += p.val
            if cur_sum == 0:
                return self.removeZeroSum(p.next)
            if cur_sum in prefix_sum: # found 0
                prefix_sum[cur_sum].next = p.next
                return self.removeZeroSum(head)
            else:
                prefix_sum[cur_sum] = p
            p = p.next
        return head

    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        return self.removeZeroSum(head)


def printL(h):
    while h is not None:
        print(h.val, end = " -> ")
        h = h.next
    print()

def make(arr):
    h = ListNode(arr[0])
    p = h
    for x in range(1, len(arr)):
        p.next = ListNode(arr[x])
        p = p.next
    return h

s = Solution()

def t1(arr):
    x = make(arr)
    printL(x)
    y = s.removeZeroSumSublists(x)
    printL(y)

t1([1,0,0,-1,2,-1,0])
# 1 1 1 0 2 1 1
t1([1,2,-3,3,1])
t1([1,2,-2])
t1([0,2,-2])
t1([1,2,-3])
t1([1,2,3,-3,-2])
t1([1,3,2,-3,-2,5,5,-5,1])
#   1 4 6 3 1 6 11 6 1
