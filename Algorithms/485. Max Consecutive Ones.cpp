/***from dust i have come, dust i will be***/

class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int ans = 0, sum = 0, n = nums.size();
        for(int e : nums)
        {
            if(e) sum++;
            else
                ans = max(ans, sum), sum = 0;
        }
        
        ans = max(ans, sum);
        return ans;
    }
};
