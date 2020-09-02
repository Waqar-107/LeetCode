typedef long long int ll;

class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
        multiset<ll> s;
        int j = 0, n = nums.size();
        ll x, y, inf = -1000000000;
        
        for(int i = 0; i < n; i++)
        {
            if(i > k)
            {
                auto itr = s.find(nums[j]);
                s.erase(itr);
                j++;
            }

            auto uno = s.lower_bound((ll)nums[i] - (ll)t);
            auto dos = s.lower_bound((ll)nums[i] + (ll)t);

            x = y = inf;

            if(uno == s.end() && s.size()) x = *s.rbegin();
            else if(uno != s.end()) x = *uno;

            if(dos == s.end() && s.size()) y = *s.rbegin();
            else if(dos != s.end()) y = *dos;

            // find if there is any number in this range
            if((x != inf && abs(x - (ll)nums[i]) <= t) || (y != inf && abs(y - (ll)nums[i]) <= t)) return true;

            s.insert(nums[i]);
        }

        return false;
    }
};
