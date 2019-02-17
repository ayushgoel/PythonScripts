class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        

    def addWord(self, word: 'str') -> 'None':
        """
        Adds a word into the data structure.
        """
        x = self.d
        for i in word:
            if i in x:
                x = x[i]
            else:
                t = {}
                x[i] = t
                x = t
        x[-1] = -1
                

    def search(self, word: 'str') -> 'bool':
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.searchT(word, self.d)

    def searchT(self, word: 'str', d: 'dict') -> bool:
        if word == '':
            if -1 in d:
                return True
            else:
                return False
        if word[0] == '.':
            for i in d.keys():
                if i == -1:
                    continue

                if self.searchT(word[1:], d[i]):
                    return True
            return False
        else:
            if word[0] in d:
                return self.searchT(word[1:], d[word[0]])
            else:
                return False


        


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("word")
obj.addWord("kord")
obj.addWord("wo")
print(obj.d)
print(obj.search('word'))
print(obj.search('wo'))
print(obj.search('kord'))
print(obj.search('wor'))
print(obj.search('k'))
print(obj.search('w'))
print(obj.search('i'))
