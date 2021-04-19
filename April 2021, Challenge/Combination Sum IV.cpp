class Solution {
public:
    vector<int> dp;
    int solve(vector<int>& nums, int target) {
        if(target == 0) return 1;
        if(target < 0) return 0;
        
        if(dp[target] != -1) return dp[target];
        
        int cnt = 0;
        for(int e : nums) {
            cnt += solve(nums, target - e);
        }
        
        return dp[target] = cnt;
    }
    
    int combinationSum4(vector<int>& nums, int target) {
        dp.resize(target + 1);
        fill(dp.begin(), dp.end(), -1);
        
        solve(nums, target);
        
        return dp[target];
    }
};
