class Solution(object):
    def numMatchingSubseq(self, s, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """

        expected_letters = {}
        for i in 'abcdefghijklmnopqrstuvwxyz':
            expected_letters[i] = []
        for i in words:
            expected_letters[i[0]].append(i)

        ans = 0
        for ch in s:
            wrds = expected_letters[ch]
            expected_letters[ch] = []
            for word in wrds:
                if len(word) == 1:
                    ans += 1
                else:
                    nw = word[1:]
                    expected_letters[nw[0]].append(nw)

        return ans
        # inds = [0]*len(words)
        # for i in s:
        #     for ind, p in enumerate(inds):
        #         if p != len(words[ind]) and words[ind][p] == i:
        #             inds[ind] += 1
        # ans = 0
        # for ind, p in enumerate(inds):
        #     if p == len(words[ind]):
        #         ans += 1
        # return ans

s = Solution()
print s.numMatchingSubseq("abcde",["a", "bb", "acd", "ace"])
