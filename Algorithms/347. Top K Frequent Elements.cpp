/***from dust i have come, dust i will be***/

#include<bits/stdc++.h>

#define dbg printf("in\n")
#define nl printf("\n")
#define N 20
#define inf 1e9

#define pb push_back
#define pp pair<int, int>

using namespace std;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> mp;
        
        int i, n = nums.size();
        for(i = 0; i < n; i++)
            mp[nums[i]]++;
        
        priority_queue<pp> pq;
        
        auto itr = mp.begin();
        while(itr != mp.end())
        {
            // cout<<itr->first<<" "<<itr->second;nl;
            pq.push({itr->second, itr->first}), itr++;
        }
        
        vector<int> ans;
        while(k > 0 && pq.size())
        {
            ans.pb(pq.top().second);
            pq.pop();
            
            k--;
        }
        
        return ans;
    }
};
