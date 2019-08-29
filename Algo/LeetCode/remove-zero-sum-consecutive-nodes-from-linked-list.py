# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def find_zero_sum(self,ll):
        s = set() 
  
        # traverse through array  
        # and store prefix sums  
        sum = 0
        for i in range(len(ll)): 
            sum += arr[i] 

            # If prefix sum is 0 or  
            # it is already present  
            if sum == 0 or sum in s: 
                return True
            s.add(sum) 
          
        return ll


    def find_ans(self,ll):
        print(ll)
        for i in range(len(ll)):
            if ll[i] < 0:
                t = i+1
                s = ll[i]
                while t < len(ll):# and s < 0:
                    s += ll[t]
                    if s == 0:
                        new_ll = ll[:i]+ll[t+1:]
                        return self.find_ans(new_ll)
                    t += 1
                
                t = i-1
                s = ll[i]
                while t >= 0:# and s < 0:
                    s += ll[t]
                    if s == 0:
                        new_ll = ll[:t]+ll[i+1:]
                        return self.find_ans(new_ll)
                    t -= 1
        return ll

    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        x = []
        y=head
        while y != None:
            x.append(y.val)
            y = y.next
        m = self.find_ans([i for i in x if i != 0])
        if len(m) == 0:
            return None
        # print(m)
        nh = head
        while nh != None:
            if nh.val == m[0]:
                break
            nh = nh.next
        y = nh
        ind = 1
        while y != None and ind < len(m):
            if y.next.val == m[ind]:
                ind += 1
                y = y.next
            else:
                y.next = y.next.next
        y.next=None
        return nh
            
            
