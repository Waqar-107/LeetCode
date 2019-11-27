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
    int searchInsert(vector<int>& nums, int target) {
        int idx = lower_bound(nums.begin(), nums.end(), target) - nums.begin();
        return idx;
    }
};
