class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        map<int, int> mp;
        for(int e : nums) mp[e]++;
        
        vector<int> ans;
        auto itr = mp.begin();
        
        while(itr != mp.end()){
            if(itr->second > nums.size() / 3) ans.push_back(itr->first);
            itr++;
        }
        
        
        return ans;
    }
};
