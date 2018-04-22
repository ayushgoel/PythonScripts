class Solution(object):
    def chars_needed(self, d1, d2):
        """
            Check if d2 has all keys listed in d1
        """
        t={}
        for k,v in d1.iteritems():
            if (not d2.has_key(k)) or d2[k] < d1[k]:
                return False
            else:
                m = d2[k] - d1[k]
                if m > 0:
                    t[k] = m
        return t

    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        tplaces = {}
        for i in t:
            if tplaces.has_key(i):
                tplaces[i] += 1
            else:
                tplaces[i] = 1

        all_chars = []
        for index, ch in enumerate(s):
            if tplaces.has_key(ch):
                all_chars.append((index, ch))
        ans = None
        window = {}
        iter_chars = all_chars[:]
        #print iter_chars
        for t in iter_chars:
            i = t[1]
            if window.has_key(i):
                window[i] += 1
            else:
                window[i] = 1
            diff = self.chars_needed(tplaces, window)
            if diff is not False:
                #print "S", diff, window, t, ans
                if ans is None:
                    #print "Q", t[0], all_chars[0]
                    ans = s[all_chars[0][0]:t[0]+1]
                else:
                    if t[0] - all_chars[0][0] < len(ans):
                        ans = s[all_chars[0][0]:t[0]+1]

                while diff is not False:
                    rem = all_chars[0]
                    if diff.has_key(rem[1]):
                        diff[rem[1]] -= 1
                        if diff[rem[1]] == 0:
                            del diff[rem[1]]
                    else:
                        diff = False
                    window[rem[1]] -= 1
                    if window[rem[1]] == 0:
                        del window[rem[1]]
                    all_chars = all_chars[1:]
                    # diff = self.chars_needed(tplaces, window)
                    #print "T", diff, window, t, ans
                    if diff is not False:
                        if ans is None:
                            #print "R", t[0], all_chars[0]
                            ans = s[all_chars[0][0]:t[0]+1]
                        else:
                            if t[0] - all_chars[0][0] < len(ans):
                                ans = s[all_chars[0][0]:t[0]+1]
        if ans is None:
            ans = ""
        return ans

s = Solution()
print s.minWindow("ADOBECODEBANC", "ABC")
print s.minWindow("ADOBECODEBANC", "ABCQ")
print s.minWindow("ADOBECODEBANC", "AB")
print s.minWindow("ADOBECODEBANC", "DN")