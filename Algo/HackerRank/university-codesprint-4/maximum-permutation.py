#!/bin/python

# from __future__ import print_function

import os
import sys


# Complete the function below.
from collections import defaultdict

def createCounter(s):
    d=defaultdict(int)
    for i in s:
        d[i] += 1
    return d


def maximumPermutation(w, s):
    # Return the string representing the answer.
    ans = defaultdict(int)

    wLen = len(w)
    wCounter = createCounter(w)
    stri = s[0:wLen]
    sCounter = createCounter(stri)

    if sCounter == wCounter:
        ans[stri] += 1
        maxAns = stri
        maxC = 1
    else:
        maxAns = "-1"
        maxC = -1

    for i in xrange(1, len(s)-len(w) + 1):
        # print stri, ans
        stri = s[i:i+wLen]
        sCounter[s[i-1]] -=1
        sCounter[s[i+wLen-1]] +=1
        if sCounter[s[i-1]] == 0:
            del sCounter[s[i-1]]
        # print "T", sCounter, wCounter
        if sCounter == wCounter:
            ans[stri] += 1
            if ans[stri] > maxC:
                maxAns = stri
                maxC = ans[stri]
            elif ans[stri] == maxC and stri<maxAns:
                maxAns = stri

    return maxAns

if __name__ == '__main__':
    print(maximumPermutation("asd", "wasdesasdasxdas"))

# if __name__ == '__main__':
#     f = open(os.environ['OUTPUT_PATH'], 'w')

#     t = int(raw_input())

#     for t_i in xrange(t):
#         w = raw_input()

#         s = raw_input()

#         result = maximumPermutation(w, s)

#         f.write(result + "\n")

#     f.close()
