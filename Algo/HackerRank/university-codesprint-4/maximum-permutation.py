#!/bin/python

from __future__ import print_function

import os
import sys


# Complete the function below.

def createCounter(s):
    d=[0] * 26
    for i in s:
        d[ord(i)-ord('a')] += 1
    return d

def update(d, key):
    if d.has_key(key):
        d[key] += 1
    else:
        d[key] = 1

def maximumPermutation(w, s):
    # Return the string representing the answer.
    ans = {}

    wLen = len(w)
    wCounter = createCounter(w)
    stri = s[0:wLen]
    sCounter = createCounter(stri)

    if sCounter == wCounter:
        update(ans, stri)
        maxAns = stri
        maxC = 1
    else:
        maxAns = "-1"
        maxC = -1

    for i in xrange(1, len(s)-len(w) + 1):
        # print stri, ans
        stri = s[i:i+wLen]
        prev_char_index=ord(s[i-1])-ord('a')
        next_char_index=ord(stri[-1])-ord('a')
        sCounter[prev_char_index] -=1
        sCounter[next_char_index] +=1
        # print(prev_char_index, next_char_index)
        # print "T", sCounter, wCounter
        if sCounter == wCounter:
            update(ans, stri)
            if ans[stri] > maxC:
                maxAns = stri
                maxC = ans[stri]
            elif ans[stri] == maxC and stri<maxAns:
                maxAns = stri

    return maxAns

if __name__ == '__main__':
    print(maximumPermutation("asdw", "wasdesaswdasxdaswd"))

# if __name__ == '__main__':
#     f = open(os.environ['OUTPUT_PATH'], 'w')

#     t = int(raw_input())

#     for t_i in xrange(t):
#         w = raw_input()

#         s = raw_input()

#         result = maximumPermutation(w, s)

#         f.write(result + "\n")

#     f.close()
