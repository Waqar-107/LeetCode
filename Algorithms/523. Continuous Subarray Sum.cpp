class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        int n = nums.size();
        
        int sum[n + 1];
        memset(sum, 0, sizeof(sum));
        
        for(int i = 1; i <= n; i++)
            sum[i] = sum[i - 1] + nums[i - 1];
        
        for(int i = 1; i < n; i++)
        {
            for(int j = 1; j <= n; j++)
            {
                if(j - i + 1 <= 1) continue;
                
                if(k == 0) {
                    if(sum[j] - sum[i - 1] == 0) return true;
                }
                
                else if((sum[j] - sum[i - 1]) % k == 0) return true; 
            }
        }
        
        return false;
    }
};
