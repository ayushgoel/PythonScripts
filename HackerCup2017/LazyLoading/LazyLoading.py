#!/usr/bin/env python

import math

def tripPossible(vals):
    if len(vals) == 0:
        return False
    return len(vals) >= (50.0/vals[-1])

def getAnswer(vals):
    ans = 0
    while tripPossible(vals):
        boxes = int(math.ceil(50.0/vals[-1]))
        vals = vals[:-1]
        vals = vals[(boxes-1):]
        ans += 1
    return ans

with open("in.txt") as f:
    fo = open("out.txt", "w")
    f.readline()
    inp = f.readlines()
    caseno = 1
    while len(inp) > 0:
        t = int(inp[0])
        # print t, inp
        inp = inp[1:]
        # print inp
        values = [int(i) for i in inp[:t]]
        # print inp, values
        inp = inp[t:]
        # print inp

        values.sort()
        answer = getAnswer(values)
        ans = "Case #{0}: {1}".format(caseno, answer)
        print ans
        fo.write(ans+"\n")

        caseno += 1
    fo.close()
