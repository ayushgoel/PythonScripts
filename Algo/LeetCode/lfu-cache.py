class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class DoubleEndedQueue:
    """docstring for DoubleEndedQueue"""
    def __init__(self):
        super(DoubleEndedQueue, self).__init__()
        self.head = Node()
        self.head.next = self.head
        self.length = 0

    def getFront(self):
        return self.head.next

    def getLast(self):
        return self.head.prev

    def insertInFront(self, val):
        #asd
    def removeNode(self, node):
        # remove
    def detach(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

        
class LFUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.valueDict = {}
        self.freqLL = DoubleEndedQueue()

    def get(self, key):
        self.increaseFrequency(key)
        return self.valueDict[key][1]["value"] if key in self.valueDict else -1

    def put(self, key: int, value: int):
        if key in self.valueDict:
            cur = self.valueDict[key]
            freqNode = self.increaseFrequency(key)
            self.valueDict[key] = (freqNode, cur[1])
            return
        if len(self.valueDict) == self.capacity:
            self.deleteLeastFrequentObject()
        freqNode = self.getFreq1Node()
        valNode = {"key": key, "value": value}
        self.valueDict[key] = (freqNode, valNode)

    def increaseFrequency(self, key):
        (freqNode, valNode) = self.valueDict[key]
        self.freqLL.detach(valNode)
        
        

    def deleteLeastFrequentObject(self):
        x = self.freqLL.getFront()
        toDelete = x.getLast()
        del self.valueDict[toDelete["key"]]
        x.removeNode(toDelete)
        if x.length() == 1:
            self.freqLL.removeNode(x)

    def getFreq1Node(self):
        f = self.freqLL.getFront() 
        if f.val == 1:
            return f
        self.freqLL.insertInFront(1)
        return self.freqLL.getFront()





# Your LFUCache object will be instantiated and called as such:
obj = LFUCache(capacity)
param_1 = obj.get(key)
obj.put(key,value)