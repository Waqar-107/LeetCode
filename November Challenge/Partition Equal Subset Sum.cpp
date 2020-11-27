class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int n = nums.size();
        int sum = 0;
        
        for(int i = 0; i < n; i++)
            sum += nums[i];
        
        if(sum % 2) return false;
        sum /= 2;
        
        bool dp[n + 1][sum + 1];
        memset(dp, false, sizeof(dp));
        
        dp[0][0] = true;
        for(int i = 1; i <= n; i++)
        {
            for(int j = 0; j <= sum; j++)
            {
                dp[i][j] = dp[i - 1][j];
                if(j - nums[i - 1] >= 0)
                    dp[i][j] |= dp[i - 1][j - nums[i - 1]];
            }
        }
        
        return dp[n][sum];
    }
};
