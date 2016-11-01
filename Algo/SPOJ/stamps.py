#! /usr/bin/env python

for i in xrange(int(raw_input())):
    gem_needed = [int(j) for j in raw_input().split()][0]
    gems = [int(j) for j in raw_input().split()]
    gems.sort(reverse=True)
    s = 0
    ans = 0
    ans_found = False
    for j in gems:
        ans += 1
        s += j
        if s >= gem_needed:
            ans_found = True
            break
    if ans_found == False:
        ans = "impossible"
    print "Scenario #{0}:".format(i + 1)
    print ans
    print
