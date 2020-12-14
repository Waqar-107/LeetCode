class Solution:
    
    def __init__(self):
        self.A = []
    
    @lru_cache(None)
    def dfs(self, i, j):
        mx = 0
        for k in range(i + 1, j):
            mx = max(mx, self.A[i] * self.A[k] * self.A[j] + self.dfs(i, k) + self.dfs(k, j))
        
        return mx
    
    def maxCoins(self, nums):
        self.A = [1] + nums + [1]
        return self.dfs(0, len(self.A) - 1)
        
        
