# https://www.interviewbit.com/problems/merge-k-sorted-lists/

import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):
        head = ListNode(-1)
        head_iter = head
        heap = [(node.val, index) for index, node in enumerate(A)]
        heapq.heapify(heap)
        while len(heap) != 0:
            # print("Y", heap)
            top_node = heapq.heappop(heap)
            # print("Y", heap)

            new_node = ListNode(top_node[0])
            head_iter.next = new_node
            head_iter = new_node

            top_index = top_node[1]
            # print heap, top_index#, next_node
            A[top_index] = A[top_index].next
            next_node = A[top_index]
            if next_node:
                heapq.heappush(heap, (next_node.val, top_index))
        return head.next

a1 = ListNode(1)
a2 = ListNode(2)
a1.next = a2

b1 = ListNode(3)
b2 = ListNode(4)
b1.next = b2

s = Solution()
x = s.mergeKLists([a1, b1])
while x:
    print("X", x.val)
    x = x.next
