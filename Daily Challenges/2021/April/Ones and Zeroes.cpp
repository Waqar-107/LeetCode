class Solution {
public:
    pair<int, int> cnt(string str) {
        int z = 0, o = 0;
        for(char ch : str) {
            if(ch == '0') z++;
            else o++;
        }
        
        return {z, o};
    }
    
    int findMaxForm(vector<string>& strs, int m, int n) {
        int sz = strs.size();
        int dp[sz + 1][m + 1][n + 1];
        vector<pair<int, int>> sizes;
        
        for(string s : strs)
            sizes.push_back(cnt(s));
        
        memset(dp, 0, sizeof(dp));
        
        for(int i = 0; i <= sz; i++)
        {
            for(int j = 0; j <= m; j++)
            {
                for(int k = 0; k <= n; k++)
                {
                    if(i == 0)
                        dp[i][j][k] = 0;
                    
                    else {
                        pair<int, int> p = sizes[i - 1];
                        
                        if(j - p.first >= 0 && k - p.second >= 0)
                            dp[i][j][k] = max(dp[i - 1][j][k], 1 + dp[i - 1][j - p.first][k - p.second]);
                        
                        else
                            dp[i][j][k] = dp[i - 1][j][k];
                    }
                }
            }
        }
        
        return dp[sz][m][n];
    }
};
