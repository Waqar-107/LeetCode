/***from dust i have come, dust i will be***/

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int sum = 0, mx = INT_MIN;
        for(int e : nums)
        {
            sum += e; 
            mx = max(mx, sum);
            
            if(sum < 0) sum = 0;
        }
        
        return mx;
    }
};
