class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        copy_board = deepcopy(board)
        n = len(board)
        m = len(board[0])
        
        dx = [1, -1, 0, 0, 1, 1, -1, -1]
        dy = [0, 0, 1, -1, 1, -1, 1, -1]
        
        for i in range(n):
            for j in range(m):
                cnt = 0
                for k in range(8):
                    x = dx[k] + j
                    y = dy[k] + i
                    
                    if 0 <= x < m and 0 <= y < n:
                        cnt += copy_board[y][x]
                
                if cnt < 2 or cnt > 3:
                    board[i][j] = 0
                elif cnt == 3:
                    board[i][j] = 1
                
        
