class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int mx = nums[0];
        int mn = nums[0];
        int n = nums.size();
        int ans = nums[0];
        
        for(int i = 1; i < n; i++)
        {
            int temp_mx = mx, temp_mn = mn;
            mx = max(nums[i], max(temp_mx * nums[i], temp_mn * nums[i]));
            mn = min(nums[i], min(temp_mx * nums[i], temp_mn * nums[i]));
            
            ans = max(ans, mx);
        }
        
        return ans;
    }
};
