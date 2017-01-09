#!/usr/bin/env python

import math

def isOnAxis(x, y):
    return x == 50 or y == 50

def angleWhenOnAxis(x, y):
    if x == 50:
        if y >= 50:
            return 0
        else:
            return 180
    if y == 50:
        if x >= 50:
            return 90
        else:
            return 270

def angle(x, y):
    if isOnAxis(x,y):
        return angleWhenOnAxis(x, y)
    if x > 50 and y > 50:
        q = (1.0 * (x-50)) / (y-50)
        return math.degrees(math.atan(q))
    if x > 50 and y < 50:
        q = (1.0 * (x-50)) / (50-y)
        return math.degrees(math.atan(q)) + 90
    if x < 50 and y < 50:
        q = (1.0 * (50-x)) / (50-y)
        return math.degrees(math.atan(q)) + 180
    if x < 50 and y > 50:
        q = (1.0 * (50-x)) / (y-50)
        return math.degrees(math.atan(q)) + 270

def outsideCircle(x, y):
    x1 = x-50
    y1 = y-50
    if (x1*x1 + y1*y1) > 2500:
        return True
    return False

with open("in.txt") as f:
    fo = open("out.txt", "w")
    f.readline()
    caseno = 1
    for line in f:
        inp = [int(i) for i in line.split()]
        p = inp[0]
        x = inp[1]
        y = inp[2]

        ans = ""
        if outsideCircle(x, y) or p == 0:
            ans = "Case #{0}: white".format(caseno)
        else:
            a = angle(x, y)
            pa = p * 3.6
            ans = "Case #{0}: ".format(caseno)
            print a, pa
            if a > pa:
                ans += "white"
            else:
                ans += "black"

        print ans
        fo.write(ans+"\n")
        caseno += 1
    fo.close()
