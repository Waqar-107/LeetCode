class Solution:
    def __init__(self):
        self.n = 0
        self.m = 0
    
    
    def inside(self, r, c):
        return r >= 0 and c >= 0 and r < self.n and c < self.m
    
    
    def dfs(self, r, c, matrix, track):
        track[r][c] = True
        
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        
        for i in range(4):
            x = r + dx[i]
            y = c + dy[i]
            
            if self.inside(x, y) and not track[x][y] and matrix[r][c] <= matrix[x][y]:
                self.dfs(x, y, matrix, track)
        
        
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        self.n = len(matrix)
        
        if self.n == 0:
            return []
        
        self.m = len(matrix[0])
        
        n = self.n
        m = self.m
        
        # pacific
        pacific = [[False for _ in range(m)] for _ in range(n)]
        
        for j in range(m):
            self.dfs(0, j, matrix, pacific)
        
        for i in range(n):
            self.dfs(i, 0, matrix, pacific)
            
        # atlantic
        atlantic = [[False for _ in range(m)] for _ in range(n)]
        
        for j in range(m):
            self.dfs(n - 1, j, matrix, atlantic)
        
        for i in range(n):
            self.dfs(i, m - 1, matrix, atlantic)
            
        ans = []
        for i in range(n):
            for j in range(m):
                if pacific[i][j] and atlantic[i][j]:
                    ans.append([i, j])
        
        return ans
