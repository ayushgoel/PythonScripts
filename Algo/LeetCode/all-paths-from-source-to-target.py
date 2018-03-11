class Solution(object):
    def allPaths(self, graph, paths, cur):
        if cur == len(graph):
            return
        for i in graph[cur]:
            for j in paths[cur]:
                paths[i].append(j+[cur])
        self.allPaths(graph, paths, cur+1)

    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(graph)
        paths = [[] for i in xrange(n)]
        paths[0] = [[-1]]
        self.allPaths(graph, paths, 0)
        p = paths[-1]
        return [i[1:]+[n-1] for i in p]
        # print paths


s = Solution()
print s.allPathsSourceTarget([[1,2],[3],[3],[]])
print s.allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]])