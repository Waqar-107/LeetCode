/***from dust i have come, dust i will be***/

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int i = 0, j, k = 0, n = nums.size();
        while(i < n)
        {
            nums[k] = nums[i];
            for(j = i + 1; j < n; j++)
                if(nums[j] != nums[i]) break;
            
            i = j;
            k++;
        }
        
        while(nums.size() > k) nums.pop_back();
        
        return nums.size();
    }
};
