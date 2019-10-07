class Node:
    def __init__(self, key, val):
        self.pre = None
        self.next = None
        self.key = key
        self.val = val

class LRUCache:

    def __init__(self, capacity: int):
        self.deq = Node(-1,-1)
        self.deq.next = self.deq
        self.deq.prev = self.deq
        self.map = {}
        self.capacity = capacity
        
    def print(self):
        for i in self.map:
            print("T",i, self.map[i].key, self.map[i].val)

    def print_ll(self):
        x = self.deq.next
        while x!=self.deq:
            print(x.key,x.val,"->",end=' ')
            x = x.next

    def get(self, key):
        if not key in self.map:
            return -1

        n = self.map[key]
        self.detach(n)
        self.put_in_front(n)
        return n.val
    
    def detach(self, n):
        n.prev.next = n.next
        n.next.prev = n.prev
        
    def put_in_front(self, n):
        i = self.deq.next
        i.prev = n
        n.next = i
        self.deq.next = n
        n.prev = self.deq

    def get_node(self, key, value):
        if key in self.map:
            n = self.map[key]
            n.val = value
            self.detach(n)
            return n
        else:
            n = Node(key, value)
            self.map[key] = n
            return n

    def put(self, key: int, value: int) -> None:
        #print("Putting",key,value)
        n = self.get_node(key, value)
        self.put_in_front(n)
        if len(self.map) > self.capacity:
            m = self.deq.prev
            #print("Going to delete",m.key,m.val)
            del self.map[m.key]
            self.detach(m)
            # self.print()
            # self.print_ll()
            #print("Deleted")

# x = LRUCache(5)
# x.put_in_front(Node(1,2))
# p = Node(3,4)
# x.put_in_front(p)
# x.print_ll()
# print()
# print(p.key, p.prev.key, p.next.key)
# x.detach(p)
# x.print_ll()

c = LRUCache(10)
c.put(10,13)
c.put(3,17)
c.put(6,11)
c.put(10,5)
c.put(9,10)
print(c.get(13))
c.put(2,19)
print(c.get(2))
print(c.get(3))
c.put(5,25)
print(c.get(8))
c.put(9,22)
c.put(5,5)
c.put(1,30)
c.put(9,22)
c.put(5,5)
c.put(1,30)
print(c.get( 11 ))
c.put( 9,12 )
print(c.get( 7 ))
print(c.get( 5 ))
print(c.get( 8 ))
print(c.get( 9 ))
c.put( 4,30 )
c.put( 9,3 )
print(c.get( 9 ))
print(c.get( 10 ))
print(c.get( 10 ))
c.put( 6,14 )
c.put( 3,1 )
print(c.get( 3 ))
c.put( 10,11 )
print(c.get( 8 ))
c.put( 2,14 )
print(c.get( 1 ))
print(c.get( 5 ))
print(c.get( 4 ))
c.put( 11,4 )
c.put( 12,24 )
c.put( 5,18 )
print(c.get( 13 ))
c.put( 7,23 )
print(c.get( 8 ))
print(c.get( 12 ))
c.put( 3,27 )
c.put( 2,12 )
print("Q")
print(c.get( 5 ))
c.print()
c.put( 2,9 )
c.put( 13,4 )
c.print()
c.put( 8,18 )
c.put( 1,7 )
print("L")




print(c.get( 6 ))
c.put( 9,29 )
c.put( 8,21 )
print(c.get( 5 ))
c.put( 6,30 )
c.put( 1,12 )
print(c.get( 10 ))
c.put( 4,15 )
c.put( 7,22 )
c.put( 11,26 )
c.put( 8,17 )
c.put( 9,29 )
print(c.get( 5 ))
c.put( 3,4 )
c.put( 11,30 )
print(c.get( 12 ))
c.put( 4,29 )
print(c.get( 3 ))
print(c.get( 9 ))
print(c.get( 6 ))
c.put( 3,4 )
print(c.get( 1 ))
print(c.get( 10 ))
c.put( 3,29 )
c.put( 10,28 )
c.put( 1,20 )
c.put( 11,13 )
print(c.get( 3 ))
c.put( 3,12 )
c.put( 3,8 )
c.put( 10,9 )
c.put( 3,26 )
print(c.get( 8 ))
print(c.get( 7 ))
print(c.get( 5 ))
c.put( 13,17 )
c.put( 2,27 )
c.put( 11,15 )
print(c.get( 12 ))
c.put( 9,19 )
c.put( 2,15 )
c.put( 3,16 )
print(c.get( 1 ))
c.put( 12,17 )
c.put( 9,1 )
c.put( 6,19 )
print(c.get( 4 ))
print(c.get( 5 ))
print(c.get( 5 ))
c.put( 8,1 )
c.put( 11,7 )
c.put( 5,2 )
c.put( 9,28 )
print(c.get( 1 ))
c.put( 2,2 )
c.put( 7,4 )
c.put( 4,22 )
c.put( 7,24 )
c.put( 9,26 )
c.put( 13,28 )
c.put( 11,26 )




