class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1:
            return nums[0]
        
        dp = []
        for i in range(2):
            dp.append([0] * n)
        
        for i in range(n - 1):
            # take this element
            dp[0][i + 1] = dp[1][i] + nums[i]
            
            # do not take this element
            dp[1][i + 1] = max(dp[0][i], dp[1][i])
        
        ans = max(dp[1][n - 1], dp[0][n - 1])
        
        dp = []
        for i in range(2):
            dp.append([0] * n)
            
        for i in range(1, n, 1):
            # take this element
            dp[0][i] = dp[1][i - 1] + nums[i]
            
            # do not take this element
            dp[1][i] = max(dp[0][i - 1], dp[1][i - 1])
        
        ans = max(ans, dp[1][n - 1], dp[0][n - 1])
        return ans
