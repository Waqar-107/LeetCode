#include<vector>

using namespace std;

class Solution {
public:
    int peakIndexInMountainArray(vector<int>& A) {
        int mx = 0, idx = -1;
        for(int i = 0; i < A.size(); i++)
        {
            if(A[i] > mx)
                mx = A[i], idx = i;
        }
        
        return idx;
    }
};
