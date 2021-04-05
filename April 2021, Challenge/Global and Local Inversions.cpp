#include <ext/pb_ds/assoc_container.hpp> // Common file
#include <ext/pb_ds/tree_policy.hpp> // Including tree_order_statistics_node_update

using namespace __gnu_pbds;

typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> ordered_set;

class Solution {
public:
    bool isIdealPermutation(vector<int>& A) {
        int local_inversion_cnt = 0, global_inversion_cnt = 0;
        int n = A.size();
        
        for(int i = 0; i < n - 1; i++) {
            if(A[i] > A[i + 1])
                local_inversion_cnt++;
        }
        
        ordered_set s;
        for(int i = n - 1; i >= 0; i--)
        {
            global_inversion_cnt += s.order_of_key(A[i]);
            s.insert(A[i]);
        }
        
        return local_inversion_cnt == global_inversion_cnt;
    }
};
