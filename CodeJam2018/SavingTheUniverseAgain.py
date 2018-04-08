
def damage(prog):
    d = 0
    t = 1
    for i in prog:
        if i == 'C':
            t *= 2
        else:
            d += t
    return d

def make_better(P):
    # P = P[::-1]
    shoot = P.rfind('CS')
    # charge = P.rfind('C')
    if shoot == -1: #or charge == -1:
        return P, 0
    else:
        return P[:shoot]+"SC"+P[shoot+2:], 1


def solve(case_no, D, P, moves):
    cur_damage = damage(P)
    # print D, P, moves, cur_damage
    if cur_damage <= D:
        # print "XX"
        print "Case #{0}: {1}".format(case_no, moves)
        return
    else:
        new_P, moves_done = make_better(P)
        if new_P == P:
            print "Case #{0}: IMPOSSIBLE".format(case_no)
        else:
            solve(case_no, D, new_P, moves + moves_done)

def main():
    T = raw_input()
    for i in xrange(int(T)):
        D, P = raw_input().split()
        # print D,P
        solve(i+1, int(D), P, 0)


if __name__ == '__main__':
    main()