import heapq

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.left = []
        self.right = []
        

    def addNum(self, num: int) -> None:
        ln1 = len(self.left)
        if ln1 == 0:
            heapq.heappush(self.left, -num)
            return
        # ln2 = len(self.right)
        # if ln2 == 0:
        #     heapq.heappush(self.right, num)
        #     return
        
        if num > -(self.left[0]):
            heapq.heappush(self.right, num)
        else:
            heapq.heappush(self.left, -num)

        if abs(len(self.left) - len(self.right)) > 1:
            ln1 = len(self.left)
            ln2 = len(self.right)
            
            if ln1 > ln2:
                x = heapq.heappop(self.left)
                heapq.heappush(self.right, -x)
            else:
                x = heapq.heappop(self.right)
                heapq.heappush(self.left, -x)

    def findMedian(self) -> float:
        ln1 = len(self.left)
        ln2 = len(self.right)
        # print("L", self.left)
        # print("R", self.right)
        if ln1 < ln2:
            return self.right[0]
        elif ln1 == ln2:
            return ((-(self.left[0]))+self.right[0])/2.0
        else:
            return -(self.left[0])
        


# Your MedianFinder object will be instantiated and called as such:
# ["MedianFinder","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian"]
# [[],[-1],[],[-2],[],[-3],[],[-4],[],[-5],[]]
# [null,null,-1,null,-1.5,null,-1,null,-2.5,null,-3]

obj = MedianFinder()
obj.addNum(-1)
print(obj.findMedian())
obj.addNum(-2)
print(obj.findMedian())
obj.addNum(-3)
print(obj.findMedian())
obj.addNum(-4)
print(obj.findMedian())
obj.addNum(-5)
print(obj.findMedian())
