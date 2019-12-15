class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.chars = [i for i in characters]
        self.clen = combinationLength
        self.maxIndex = len(self.chars)-1
        self.finalState = [self.maxIndex-i for i in range(self.clen)][::-1]
        
        self.state = [i for i in range(self.clen)]
        self.stopped = False

    def nextState(self, state, maxIndex):
        if state[-1] != maxIndex:
            state[-1] += 1
            return state
        new_state = self.nextState(state[:-1], maxIndex-1)
        return new_state + [new_state[-1] + 1]

    def next(self) -> str:
        print(self.state)
        str_to_ret = ''.join([self.chars[i] for i in self.state])
        if self.state == self.finalState:
            self.stopped = True
        else:
            self.state = self.nextState(self.state, self.maxIndex)
        return str_to_ret

    def hasNext(self) -> bool:
        return self.stopped == False


# obj = CombinationIterator("abcd", 2)
# print(obj.next())
# print(obj.next())
# print(obj.next())
# print(obj.next())
# print(obj.hasNext())
# print(obj.next())
# print(obj.next())
# print(obj.next())
# print(obj.next())
# print(obj.hasNext())
# print(obj.next())
# print(obj.next())
# print(obj.hasNext())

# obj = CombinationIterator("abcd", 4)
# print(obj.next())
# print(obj.next())
# print(obj.next())
# print(obj.next())
# print(obj.hasNext())
# print(obj.next())
# print(obj.next())
# print(obj.next())
# print(obj.next())
# print(obj.hasNext())
# print(obj.next())
# print(obj.next())
# print(obj.hasNext())

obj = CombinationIterator("fiklnuy", 3)
print(obj.next())
print(obj.next())
print(obj.next())
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.next())
print(obj.next())
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.next())
print(obj.hasNext())
for i in range(100):
    print(obj.next())

# ["CombinationIterator","hasNext","next","hasNext","next","hasNext","next","next","next","hasNext","hasNext","next","hasNext","hasNext","next","hasNext","next","hasNext","hasNext","hasNext","next","next","hasNext","next","hasNext","next","next","hasNext","hasNext","next","next","hasNext","hasNext","next","hasNext","next","next","next","next","hasNext","hasNext","next","next","hasNext","hasNext","next","next","hasNext","next","hasNext","hasNext","hasNext","next","next","hasNext","hasNext","hasNext","hasNext","next","hasNext","next","hasNext","next","next","next","next","next","next","hasNext","hasNext","hasNext","hasNext","hasNext","hasNext","hasNext","hasNext","hasNext","hasNext","hasNext","hasNext","hasNext","hasNext","hasNext","hasNext","hasNext","hasNext","hasNext","hasNext","hasNext","hasNext","hasNext","hasNext","hasNext","hasNext","hasNext","hasNext","hasNext","hasNext","hasNext","hasNext","hasNext"]
# [["fiklnuy",3],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]