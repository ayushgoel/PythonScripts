# https://www.interviewbit.com/problems/ways-to-decode/

class Solution:
    # @param a : string
    # @return an integer
    def numDecodings(self, a):
        if a[0]=='0':
            return 0
        sp = [1, 1]
        for i in xrange(2, len(a)+1):
            x = 0
            last_two_digit_num = int(a[i-2:i])
            if a[i-1] != '0':
                x = sp[i-1]
            elif last_two_digit_num > 26:
                return 0
            if last_two_digit_num > 9 and last_two_digit_num <= 26:
                x += sp[i-2]
            sp += [x]
        return sp[len(a)]
