class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        
        if s[0] == '0':
            return 0
        
        dp[0] = 1
        for i in range(1, n):
            if s[i] != '0':
                dp[i] += dp[i - 1]
            
            if s[i - 1] == "1" or (s[i - 1] == "2" and "0" <= s[i] <= "6"):
                if i - 2 >= 0:
                    dp[i] += dp[i - 2]
                else:
                    dp[i] += 1
                
        
        return dp[-1]
