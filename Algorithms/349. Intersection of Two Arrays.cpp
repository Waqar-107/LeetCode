/***from dust i have come, dust i will be***/

#define pb push_back

class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        int k, n = nums2.size();
        set<int> vec;
        sort(nums2.begin(), nums2.end());
        
        for(int e : nums1)
        {
            k = lower_bound(nums2.begin(), nums2.end(), e) - nums2.begin();
            if(k < n && nums2[k] == e)
                vec.insert(e);
        }
        
        vector<int> ans;
        for(int e : vec)
            ans.pb(e);
        
        return ans;
    }
};
