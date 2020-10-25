class Solution:
    def __init__(self):
        self.dp = {}
        
    def winnerSquareGame(self, n: int) -> bool:
        if n == 0:
            return False
        
        if n in self.dp:
            return self.dp[n]
        
        x = int(math.sqrt(n))
        while x >= 1:
            if not self.winnerSquareGame(n - x ** 2):
                self.dp[n] = True
                return True
            x -= 1
        
        self.dp[n] = False
        return False
