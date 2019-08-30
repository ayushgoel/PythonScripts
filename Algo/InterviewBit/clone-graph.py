# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node

    def create_node(self, o, ans_nodes):
        if o in ans_nodes:
            return ans_nodes[o]
        x = UndirectedGraphNode(o.label)
        ans_nodes[o] = x
        return x

    def cloneGraph(self, node):
        visited = set()
        
        ans_nodes = {}
        q = [node]
        
        while len(q) != 0:
            o = q.pop(0)
            if o in visited:
                continue
            
            n = self.create_node(o, ans_nodes)

            for i in o.neighbors:
                if i in ans_nodes:
                    n.neighbors.append(ans_nodes[i])
                else:
                    x = self.create_node(i, ans_nodes)
                    n.neighbors.append(x)
                q.append(i)
            visited.add(o)
        return ans_nodes.itervalues().next()
        
