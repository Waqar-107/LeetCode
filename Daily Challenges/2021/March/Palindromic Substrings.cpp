class Solution {
public:
    int countSubstrings(string s) {
        int n = s.length();
        
        bool dp[n][n];
        memset(dp, false, sizeof(dp));
        
        // substr starting from i and ending at i is a palindrome - len 1
        for(int i = 0; i < n; i++)
            dp[i][i] = true;
        
        // substr starting from i and ending at i+1 - len 2
        for(int i = 0; i < n - 1; i++) {
            if(s[i] == s[i + 1])
                dp[i][i + 1] = true;
        }
        
        // len k
        for(int k = 3; k <= n; k++)
        {
            // fix the starting
            for(int i = 0; i < n - k + 1; i++)
            {
                // end
                int j = i + k - 1;
                
                // check if start-end is same and except these two, the substr in the middle is a palindrome
                if(dp[i + 1][j - 1] && s[i] == s[j])
                    dp[i][j] = true;
            }
        }
        
        int ans = 0;
        for(int i = 0; i < n; i++)
        {
            for(int j = 0; j < n; j++)
            {
                if(dp[i][j])
                    ans++;
            }
        }
        
        return ans;
    }
};
