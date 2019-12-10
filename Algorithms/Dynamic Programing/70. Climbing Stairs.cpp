/***from dust i have come, dust i will be***/

class Solution {
public:
    int climbStairs(int n) {
        // 1 1 2 3 5 8 13
        int dp[n + 1] = {0};
        dp[0] = 1, dp[1] = 1;
        for(int i = 2; i <= n; i++)
            dp[i] = dp[i - 1] + dp[i - 2];
        
        return dp[n];
    }
};
