class Solution {
public:
    int countVowelStrings(int n) {
        int dp[n + 1][5];
        memset(dp, 0, sizeof(int));
        
        for(int i = 0; i < 5; i++) {
            dp[1][i] = 1;
        }
        
        for(int i = 2; i <= n; i++) {
            int prevSum = 0;
            for(int j = 0; j < 5; j++) {
                prevSum += dp[i - 1][j];
            }
            
            int sumToSubtract = 0;
            for(int j = 0; j < 5; j++) {
                dp[i][j] = prevSum - sumToSubtract;
                sumToSubtract += dp[i - 1][j];
            }
        }
        
        int ans = 0;
        for(int j = 0; j < 5; j++) {
            ans += dp[n][j];
        }
        
        return ans;
    }
};
