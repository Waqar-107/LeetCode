class Solution {
public:
    int search(vector<int>& nums, int target) {
        int hi = nums.size() - 1, lo = 0, mid;
        int ans = -1;
        
        while(lo <= hi)
        {
            mid = (hi + lo) / 2;
            
            if(nums[mid] == target) {ans = mid; break;}
            
            else if(nums[mid] > target)
                hi = mid - 1;
            else
                lo = mid + 1;
        }
        
        return ans;
    }
};
