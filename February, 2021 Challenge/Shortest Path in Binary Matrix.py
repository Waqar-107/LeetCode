class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        if grid[0][0]:
            return -1
        
        dist = [[math.inf for _ in range(m)] for _ in range(n)]
        vis = [[False for _ in range(m)] for _ in range(n)]
        
        q = [(0, 0)]
        dist[0][0] = 0
        vis[0][0] = True
        
        dx = [0, 0, 1, -1, -1, -1, 1, 1]
        dy = [1, -1, 0, 0, -1, 1, 1, -1]
        
        while len(q):
            u = q.pop(0)
            
            for i in range(8):
                x = u[0] + dx[i]
                y = u[1] + dy[i]

                if 0 <= x < n and 0 <= y < m and not vis[x][y] and grid[x][y] == 0:
                    dist[x][y] = dist[u[0]][u[1]] + 1
                    q.append((x, y))
                    vis[x][y] = True
        
        if not vis[n - 1][m - 1]:
            return -1
        
        return dist[n - 1][m - 1] + 1
        
