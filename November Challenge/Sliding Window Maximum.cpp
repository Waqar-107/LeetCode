class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        multiset<int> ms;
        int i = 0, j = k - 1, n = nums.size();
        
        for(int idx = 0; idx <= j; idx++)
            ms.insert(nums[idx]);
        
        vector<int> ans;
        ans.push_back(*ms.rbegin());
        
        j++;
        while(j < n)
        {
            ms.erase(ms.find(nums[i]));
            i++;
            
            ms.insert(nums[j]);
            j++;
            
            ans.push_back(*ms.rbegin());
        }
        
        return ans;
    }
};
