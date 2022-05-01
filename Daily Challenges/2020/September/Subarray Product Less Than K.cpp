class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        int i = 0, j = 0;
        int n = nums.size();
        
        int mult = 1, ans = 0;
        while(j < n) {
            mult *= nums[j];
            
            while(i <= j && mult >= k)
            {
                mult /= nums[i];
                i++;
            }
            
            if(i > j) j = i;
            else ans += (j - i + 1), j++;
        }
        
        return ans;
    }
};
