/***from dust i have come, dust i will be***/

#include<bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        set<int> s;
        map<int, int> mp;
        
        int mx = nums[0];
        
        for(int i = 0; i < k; i++){
            s.insert(nums[i]);
            mp[nums[i]]++;
            mx = max(mx, nums[i]);
        }
        
        vector<int> vec;
        vec.push_back(mx);
        
        int i = 0;
        while(k < nums.size())
        {
            mp[nums[i]]--;
            if(mp[nums[i]] == 0) s.erase(nums[i]);
            i++;
            
            mp[nums[k]]++;
            s.insert(nums[k]);
            k++;
        
            auto itr = s.rbegin();
            vec.push_back(*itr);
        }
        
        return vec;
    }
};
