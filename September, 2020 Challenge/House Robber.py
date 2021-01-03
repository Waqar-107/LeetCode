class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0 for i in range(n + 1)] for j in range(2)]
        
        for i in range(1, n + 1, 1):
            # take
            dp[0][i] = nums[i - 1] + dp[1][i - 1]
            
            # won't take
            dp[1][i] = max(dp[0][i - 1], dp[1][i - 1])
        
        return max(dp[0][n], dp[1][n])
        
