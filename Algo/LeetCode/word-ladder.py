class Solution:
    def isDiffOne(self, wo1, wo2, io1, io2, index, ignore):
        if not ignore and index[io1][io2] != None:
            return index[io1][io2]
        w1 = w2 = i1 = i2 = None
        if io1 > io2:
            i1 = io2
            i2 = io1
            w1 = wo2
            w2 = wo1
        else:
            i1 = io1
            i2 = io2
            w1 = wo1
            w2 = wo2

        ln1 = len(w1)
        
        od = False
        for i in range(ln1):
            if w1[i] != w2[i]:
                if od:
                    if not ignore:
                        index[i1][i2] = False
                    return False
                else:
                    od = True
        if not ignore:
            index[i1][i2] = True
        return True
                
        
    def ladderLength(self, beginWord: str, endWord: str, words) -> int:
        ln = len(words)
        isVisited = [False]*ln
        q = [] # (word_index, iteration)
        index = [[None for i in range(ln)] for i in range(ln)]
        for i in range(ln):
            if self.isDiffOne(beginWord, words[i], 1, 1, index, True):
                q.append((i, 1))
                isVisited[i] = True
        while len(q) != 0:
            # print(q)
            x = q.pop(0)
            if words[x[0]] == endWord:
                # print(index)
                return x[1]+1
            for i in range(ln):
                if not isVisited[i] and self.isDiffOne(words[x[0]], words[i], x[0], i, index, False):
                    q.append((i, x[1] + 1))
                    isVisited[i] = True
        return 0
            
            
s = Solution()
assert(s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]) == 5)