import pprint

class Solution:
    def add_prefix(self, d, s, j):
        if j >= len(s):
            return
        cur = s[j]
        if cur not in d:
            d[cur] = {"values":[], "data": {}}
        if len(d[cur]["values"]) < 3:
            d[cur]["values"] += [s]
        self.add_prefix(d[cur]["data"], s, j+1)

    def search(self, d, s):
        if len(s) == 0:
            return None
        cur = s[0]
        if cur in d:
            x = self.search(d[cur]['data'], s[1:])
            if x is None:
                return [d[cur]['values']]
            return [d[cur]['values']] + x
        else:
            return [[]] * len(s)
        
        
        
    def suggestedProducts(self, products, searchWord):
        d = {}
        products = sorted(products)

        for s in products:
            self.add_prefix(d, s, 0)
        x = self.search(d, searchWord)
        # pprint.pprint(x)
        return x
        
s = Solution()
assert(s.suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"], "mouse") == [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]])

assert(s.suggestedProducts(["bags","baggage","banner","box","cloths"], "bags") == [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]])

assert(s.suggestedProducts(["havana"], "tatiana") == [[],[],[],[],[],[],[]])

