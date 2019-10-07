class Solution:
    
    def gold(self, grid, visited, i, j):
        if i >= len(grid) or j >= len(grid[0]) or i<0 or j<0:
            return 0
        if grid[i][j] == 0:
            return 0
        if visited[i][j] == True:
            return 0
        # print(i, j)
        # vis = [[visited[j][i] for i in range(len(grid[0]))] for j in range(len(grid))]
        # vis[i][j] = True
        visited[i][j] = True
        x = max(self.gold(grid, visited, i+1, j), self.gold(grid, visited, i, j+1), self.gold(grid, visited, i-1, j), self.gold(grid, visited, i, j-1))
        # print("T",i,j,grid[i][j] + x)
        visited[i][j] = False
        return grid[i][j] + x
        
    
    def getMaximumGold(self, grid):
        all_nodes = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    all_nodes += [(i,j)]
        
        ans = 0
        for node in all_nodes:
            visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
            s = self.gold(grid, visited, node[0], node[1])
            # print("Q", ans, s, node)
            ans = max(ans, s)
        return ans

s = Solution()
assert(s.getMaximumGold([[0,6,0],[5,8,7],[0,9,0]]) == 24)
tt = [[1,0,7],
 [2,0,6],
 [3,4,5],
 [0,3,0],
 [9,0,20]]
assert(s.getMaximumGold(tt) == 28)
