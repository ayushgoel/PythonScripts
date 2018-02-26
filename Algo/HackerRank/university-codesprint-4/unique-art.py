#!/bin/python

from __future__ import print_function

import os
import sys

class Node(object):
    def __init__(self):
        super(Node, self).__init__()
        self.left = None
        self.right = None
        self.interval = []
        self.unique_vals = set()

def createNode(arr, i, j):
    # print(arr,i,j)
    if j == i:
        node = Node()
        node.unique_vals = set([arr[i]])
        node.interval = [i,j]
        return node
    else:
        mid = (i+j)/2
        n = Node()
        n.left = createNode(arr, i, mid)
        n.right = createNode(arr, mid+1, j)
        n.interval = [i,j]
        n.unique_vals = n.left.unique_vals.symmetric_difference(n.right.unique_vals)
        return n

def printNode(n):
    if n is None:
        return
    print(n.interval, n.unique_vals)
    # print(n.left.unique_vals, end = ' ')
    # print(n.right.unique_vals, end = ' ')
    printNode(n.left)
    printNode(n.right)

#
# Complete the initialize function below.
#
segment_tree = None
def initialize(t):
    #
    # Write your code here.
    #
    global segment_tree
    segment_tree = createNode(t, 0, len(t) - 1)
    # printNode(segment_tree)

def query(n,i,j):
    if n is None:
        return set()
    if n.interval == [i,j]:
        return n.unique_vals
    mid = (n.interval[0] + n.interval[1])/2
    if i>=mid+1:
        return query(n.right, i,j)
    elif j<=mid:
        return query(n.left,i,j)
    else:
        left_all = query(n.left,i,mid)
        right_all = query(n.right,mid+1,j)
        return left_all.symmetric_difference(right_all)
#
# Complete the student function below.
#
def student(i, j):
    # Return the number of paintings that this student will appreciate.
    return len(query(segment_tree, i-1,j-1))


if __name__ == '__main__':
    initialize([1, 1, 2, 3, 5, 8])
    # n = int(raw_input())

    # t = map(int, raw_input().rstrip().split())

    # initialize(t)
    # q = int(raw_input())

    # for q_itr in xrange(q):
    #     ij = raw_input().split()

    #     i = int(ij[0])

    #     j = int(ij[1])

    #     result = student(i, j)

    #     print(result)
