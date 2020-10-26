class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0 for _ in range(110)] for _ in range(110)]
        
        dp[0][0] = poured * 1.0
        for i in range(100):
            for j in range(i + 1):
                if dp[i][j] > 1.0:
                    ex = (dp[i][j] - 1.0) / 2
                    dp[i + 1][j] +=  ex
                    dp[i + 1][j + 1] += ex
                    dp[i][j] = 1.0
        
        return dp[query_row][query_glass]
