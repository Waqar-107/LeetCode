class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        mx = 1
        idx = 0
        
        dp = [[False for _ in range(n)] for _ in range(n)]
        
        # length 1
        for i in range(n):
            dp[i][i] = True
        
        # length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                mx = 2
                idx = i
                
        # length k
        for k in range(3, n + 1):
            # fix the start
            for i in range(n - k + 1):
                j = i + k - 1
                if dp[i + 1][j - 1] and s[i] == s[j]:
                    dp[i][j] = True
                    
                    if k > mx:
                        mx = k
                        idx = i
        
        ans = ""
        for i in range(idx, idx + mx):
            ans += s[i]
    
        return ans
        
