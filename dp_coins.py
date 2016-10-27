#! /usr/bin/env python
# Given a list of N coins, their values (V1, V2, VN), and the total sum S. Find the minimum number
# of coins the sum of which is S (we can use as many coins of one type as we want), or report that
# its not possible to select coins in such a way that they sum up to S.

# Recusrsive DP
def solution1():
    max_val = 100
    dp = [max_val]*max_val

    coins = [3, 5]
    S = 15

    def sol(x):
        if x == 0:
            return 0
        if x < 0:
            return max_val
        if dp[x] != max_val:
            return dp[x]

        new_val = max_val
        for i in coins:
            t = sol(x - i) + 1
            if t < new_val:
                new_val = t

        dp[x] = new_val
        return dp[x]

    answer = sol(S)
    answer = answer if answer != max_val else "No answer"
    print "Solution is", answer

solution1()

# Iterative DP
def solution2():
    max_val = 100
    dp = [max_val]*max_val

    coins = [3, 5]
    S = 15

    dp[0] = 0
    for i in xrange(1, S+1):
        min_val = max_val
        for j in coins:
            new_index = i - j
            if new_index < 0:
                continue
            new_val = dp[new_index] + 1
            if min_val > new_val:
                min_val = new_val
        dp[i] = min_val

    answer = dp[S]
    answer = answer if answer != max_val else "No answer"
    print "Solution is", answer

solution2()

