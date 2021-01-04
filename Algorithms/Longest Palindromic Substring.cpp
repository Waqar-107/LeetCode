class Solution {
public:
    string longestPalindrome(string s) {
        int n = s.length();
        int mx = 1, idx = 0;
        
        bool dp[n][n];
        memset(dp, false, sizeof(dp));
        
        // length 1
        for(int i = 0; i < n; i++)
            dp[i][i] = true;
        
        // length 2    
        for(int i = 0; i < n - 1; i++) {
            if(s[i] == s[i + 1]) {
                dp[i][i + 1] = true;
                idx = i;
                mx = 2;
            }
        }
        
        // k length of palindrome
        for(int k = 3; k <= n; k++)
        {
            // fix the starting
            for(int i = 0; i < n - k + 1; i++)
            {
                // ending index
                int j = i + k - 1;
                if(dp[i + 1][j - 1] && s[i] == s[j]) {
                    dp[i][j] = true;
 
                    if (k > mx) {
                        idx = i;
                        mx = k;
                    }
                }
            }
        }
        
        string ans = "";
        for(int i = idx; i < mx + idx; i++)
            ans += s[i];
        
        return ans;
    }
};
