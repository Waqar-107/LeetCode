class Solution {
public:
    int smallestDivisor(vector<int>& nums, int threshold) {
        int lo = 1, hi = nums.back(), n = nums.size();
        int ans = hi;
        
        while(lo <= hi)
        {
            int mid = (lo + hi) / 2;
            int cnt = 0;
            
            for(int i = 0; i < n; i++)
            {
                cnt += nums[i] / mid;
                if(nums[i] % mid)
                    cnt++;
            }
            
            if(cnt <= threshold)
                ans = min(ans, mid), hi = mid - 1;
            else
                lo = mid + 1;
        }
        
        return ans;
    }
};
