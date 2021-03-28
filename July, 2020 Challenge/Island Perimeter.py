class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    for k in range(4):
                        x = dx[k] + i
                        y = dy[k] + j
                        
                        # a border
                        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
                            ans += 1
                        
                        elif grid[x][y] == 0:
                            ans += 1
        
        return ans
