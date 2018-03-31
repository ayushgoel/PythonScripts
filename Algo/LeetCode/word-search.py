import copy

repl_char = '.'

class Solution(object):
    def search(self, cache, board, word, i, j):
        #printf board, word, i, j
        lw = len(word)
        if lw == 0:
            return True
        #printf cache
        if lw in cache[i][j]:
            return False
        if (i+1) < len(board) and board[i+1][j] == word[0]:
            #printf "1"
            board[i+1][j] = repl_char
            if self.search(cache, board, word[1:], i+1, j):
                return True
            #printf "1.1"
            board[i+1][j] = word[0]
            # cache[i+1][j].add(lw-1)
        if (j+1) < len(board[i]) and board[i][j+1] == word[0]:
            #printf "2"
            board[i][j+1] = repl_char
            if self.search(cache, board, word[1:], i, j+1):
                return True
            #printf "2.1"
            board[i][j+1] = word[0]
            # cache[i][j+1].add(lw-1)
        if (i-1) >=0 and board[i-1][j] == word[0]:
            #printf "3"
            board[i-1][j] = repl_char
            if self.search(cache, board, word[1:], i-1, j):
                return True
            #printf "3.1"
            board[i-1][j] = word[0]
            # cache[i-1][j].add(lw-1)
        if (j-1) >=0 and board[i][j-1] == word[0]:
            #printf "4"
            board[i][j-1] = repl_char
            if self.search(cache, board, word[1:], i, j-1):
                return True
            #printf "4.1"
            board[i][j-1] = word[0]
            # cache[i][j-1].add(lw-1)
        # cache[i][j].add(lw)
        return False

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(word) == 0:
            return True
        cache = [[set() for i in xrange(len(board[0]))] for j in xrange(len(board))]

        for i in xrange(len(board)):
            for j in xrange(len(board[i])):
                if board[i][j] == word[0]:
                    # new_board = copy.deepcopy(board)
                    board[i][j] = repl_char
                    if self.search(cache, board, word[1:], i, j):
                        return True
                    board[i][j] = word[0]
        return False

s = Solution()
print s.exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFSAX")
# A B C E
# S F E S
# A D E E
