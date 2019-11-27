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
    int shipWithinDays(vector<int>& weights, int D) {
        int hi = 0, lo = 1, mid, n = weights.size();
        for(int e : weights)
            hi += e;
        
        int ans = hi;
        while(lo <= hi)
        {
            mid = (lo + hi) / 2;
            
            int sum = 0, cnt = 1;
            for(int i = 0; i < n; i++){
                if(mid < weights[i]){
                    cnt = D + 1;
                    break;
                }
                
                if(sum + weights[i] <= mid)
                    sum += weights[i];
                else
                    cnt++, sum = weights[i];
            }
            
            // cout<<mid<<" "<<cnt;nl;
            
            if(cnt <= D)
                ans = min(ans, mid), hi = mid - 1;
            else
                lo = mid + 1;
        }
        
        return ans;
    }
};
