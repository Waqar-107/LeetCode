class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        map<int, int> cnt;
        
        for(int e : nums) {
            if(e <= k) {
                cnt[e]++;
            }
        }
        
        int ans = 0;
        auto itr = cnt.begin();
        
        while(itr != cnt.end())
        {
            if(k % 2 == 0 && k / 2 == itr->first)
            {
                ans += itr->second / 2;
                itr++;
                continue;
            }
            
            int x = itr->second;
            int y = cnt[k - itr->first];
            int mn = min(x, y);
            
            ans += mn;
            cnt[k - itr->first] -= mn;
            cnt[itr->first] -= mn;
            
            itr++;
        }
        
        return ans;
    }
};
