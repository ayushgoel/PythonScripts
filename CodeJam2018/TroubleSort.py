
def solve(case_no, arr):
    odds = sorted(arr[::2])
    evens = sorted(arr[1::2])
    # t=0
    # for i,j in zip(odds,evens):
    #     if i>j:
    #         print "Case #{0}: {1}".format(case_no, (2*t))
    #         return
    #     t += 1
    # if len(odds) > len(evens):
    #     if len(evens) > 0 and odds[-1] < evens[-1]:
    #         print "Case #{0}: {1}".format(case_no, (2*t)-1)
    #         return
    lo = len(odds)
    le = len(evens)
    for i in xrange(lo):
        if (i < le) and odds[i] > evens[i]:
            print "Case #{0}: {1}".format(case_no, (2*i))
            return
        if (i+1 < lo) and evens[i] > odds[i+1]:
            print "Case #{0}: {1}".format(case_no, (2*i)+1)
            return
        # t += 1
    print "Case #{0}: OK".format(case_no)


def main():
    T = raw_input()
    for i in xrange(int(T)):
        raw_input()
        arr = [int(j) for j in raw_input().split()]
        solve(i+1, arr)

if __name__ == '__main__':
    main()

# Case #1: OK
# Case #2: 1
# Case #3: OK
# Case #4: OK
# Case #5: 3
# Case #6: 0
# Case #7: 3
# Case #8: 3
# Case #9: 3
# Case #10: 3