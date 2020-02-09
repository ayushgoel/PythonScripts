import pprint
import heapq
class Solution:
    def findTheCity(self, n: int, edges, distanceThreshold: int) -> int:
        # g = [[10005 for i in range(n)] for j in range(n)]
        d={}
        for i in edges:
            if i[2] > distanceThreshold:
                continue
            # g[i[0]][i[1]] = i[2]
            # g[i[1]][i[0]] = i[2]
            if i[0] in d:
                d[i[0]] += [[i[1],i[2]]]
            else:
                d[i[0]] = [[i[1],i[2]]]
            if i[1] in d:
                d[i[1]] += [[i[0],i[2]]]
            else:
                d[i[1]] = [[i[0],i[2]]]
        
        for i in d:
            d[i].sort(key=lambda x:x[1])
        
        ans = -1
        ans_con = n

        for node in range(n-1, -1, -1):
            #print("starting node", node)
            vis = set()
            h = [(0,node)]
            con = set()
            while len(h) != 0:
                t = heapq.heappop(h)
                #print("taking", t)
                if t[1] in vis:
                    continue
                else:
                    vis.add(t[1])
                if t[1] != node: # dont reduce gap for self node
                    #print("Updating", t[0], node)
                    con.add(t[1])
                if t[1] in d: # for all connected nodes
                    for i in d[t[1]]:
                        new_d = t[0] + i[1]
                        #print(i, t, new_d)
                        if new_d <= distanceThreshold:
                            heapq.heappush(h, (new_d, i[0]))

            if len(con) < ans_con:
                # print("Setting", ans, "to", node)
                # print(con)
                # print("Because {0} has {1} connections while {2} has {3}".format(node, len(con), ans, ans_con))
                ans = node
                ans_con = len(con)

        return ans

s = Solution()
# print(s.findTheCity(4, [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], 4))

print(s.findTheCity(5, [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], 2)