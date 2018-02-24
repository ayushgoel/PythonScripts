
#!/bin/python

from __future__ import print_function

import os
import sys
import math


# Complete the function below.

def maximumPackages(S, K, R, C):
    # Return the maximum number of packages that can be put in the containers.
    ans = 0
    pack = dict(zip(S,K))
    con = dict(zip(R,C))
    lens = sorted(S, reverse=True)
    rs = sorted(R, reverse=True)
    for r in rs:
        possibleL = math.floor(r*1.414)
        pCaps = con[r]
        for i in xrange(len(lens)):
            if pCaps <= 0:
                break
            if lens[i] <= possibleL:
                copies = pack[lens[i]]
                if pCaps >= copies:
                    ans += copies
                    pCaps = pCaps - copies
                    pack[lens[i]] = 0
                else:
                    ans += pCaps
                    pack[lens[i]] = copies - pCaps
                    pCaps = 0
        # delete lens with copies 0
    return ans

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = raw_input().split()
    n = int(nm[0])
    m = int(nm[1])

    S = map(int, raw_input().rstrip().split())
    K = map(int, raw_input().rstrip().split())
    R = map(int, raw_input().rstrip().split())
    C = map(int, raw_input().rstrip().split())

    result = maximumPackages(S, K, R, C)
    f.write(str(result) + "\n")
    f.close()


# if __name__ == '__main__':
#     print(maximumPackages([1,2],[1,3],[1,2],[1,1]))
