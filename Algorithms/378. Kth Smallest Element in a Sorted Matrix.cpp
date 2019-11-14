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
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        int n = matrix.size();
        vector<int> vec;
        for(int i = 0; i < n; i++)
        {
            for(int j = 0; j < n; j++)
                vec.pb(matrix[i][j]);
        }
        
        sort(vec.begin(), vec.end());
        return vec[k - 1];
    }
};
