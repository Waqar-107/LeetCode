/***from dust i have come, dust i will be***/

class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        
        if(!n) return 0;
        
        int dp[n + 1] = {0};
        
        dp[1] = nums[0];
        for(int i = 2; i <= n; i++)
        {
            // we can either take ith or not
            dp[i] = max(dp[i - 2] + nums[i - 1], dp[i - 1]);
        }
        
        return dp[n];
    }
};
