class Solution:
    def __init__(self):
        self.vis = {}
        self.toBeMarked = []
        self.hasBorder = False
        
    def dfs(self, r, c, board):
        self.vis[(r, c)] = True
        self.toBeMarked.append((r, c))
        
        # check if r, c belongs to border
        if r == 0 or r == len(board) - 1 or c == 0 or c == len(board[0]) - 1:
            self.hasBorder = True
        
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        
        for i in range(4):
            x = r + dx[i]
            y = c + dy[i]
            
            if 0 <= x < len(board) and 0 <= y < len(board[0]) and (x, y) not in self.vis and board[x][y] == 'O':
                self.dfs(x, y, board)
        
    def solve(self, board: List[List[str]]) -> None:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i, j) not in self.vis and board[i][j] == 'O':
                    self.toBeMarked = []
                    self.hasBorder = False
                    
                    self.dfs(i, j, board)

                    if not self.hasBorder:
                        for cell in self.toBeMarked:
                            board[cell[0]][cell[1]] = 'X'
        
