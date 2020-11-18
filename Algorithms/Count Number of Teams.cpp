#include <ext/pb_ds/assoc_container.hpp> // Common file
#include <ext/pb_ds/tree_policy.hpp> // Including tree_order_statistics_node_update

using namespace __gnu_pbds;

typedef tree<
int,
null_type,
less<int>,
rb_tree_tag,
tree_order_statistics_node_update>
ordered_set;

class Solution {
public:
    int numTeams(vector<int>& rating) {
        int n = rating.size();
        
        int rightG[n], rightL[n], leftG[n], leftL[n];
        memset(rightG, 0, sizeof(rightG));
        memset(rightL, 0, sizeof(rightL));
        memset(leftG, 0, sizeof(leftG));
        memset(leftL, 0, sizeof(leftL));
        
        ordered_set s;
        
        // how many are greater than ith in the set
        // how many are less than ith in the set
        for(int i = n - 1; i >= 0; i--)
        {
            rightG[i] = s.size() - s.order_of_key(rating[i]);
            rightL[i] = s.order_of_key(rating[i]);
            s.insert(rating[i]);
        }
        
        s.clear();
        
        // how many are greater than ith in the set in the left
        // how many are less than ith in the set in the left
        for(int i = 0; i < n; i++)
        {
            leftG[i] = s.size() - s.order_of_key(rating[i]);
            leftL[i] = s.order_of_key(rating[i]);
            s.insert(rating[i]);
        }
        
        int ans = 0;
        for(int i = 0; i < n; i++)
        {
            ans += (rightG[i] * leftL[i]);
            ans += (rightL[i] * leftG[i]);
        }
        
        return ans;
    }
};
