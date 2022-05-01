class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0 for _ in range(n)] for _ in range(amount + 1)]
        
        if amount == 0:
            return 1
        if n == 0:
            return 0
        
        for j in range(n):
            dp[0][j] = 1
            
        for i in range(1, amount + 1):
            for j in range(n):
                # include coin j
                if i - coins[j] >= 0:
                    x = dp[i - coins[j]][j]
                else:
                    x = 0
                
                # do not include j
                if j >= 1:
                    y = dp[i][j - 1]
                else:
                    y = 0
                
                dp[i][j] = x + y
        
        return dp[amount][n - 1]
                
