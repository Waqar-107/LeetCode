class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 0:
            return 0
        
        dp = [1] * n
        ways = [1] * n
        
        for i in range(1, n):
            mx = -1
            cnt = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    if mx < dp[j]:
                        mx = dp[j]
                        cnt = ways[j]
                    elif mx == dp[j]:
                        cnt += ways[j]
            
            if mx == -1:
                dp[i] = 1
                ways[i] = 1
            
            else:
                dp[i] = 1 + mx
                ways[i] = cnt

        mx = max(dp)
        ans = 0
        for i in range(n):
            if dp[i] == mx:
                ans += ways[i]
        
        return ans
