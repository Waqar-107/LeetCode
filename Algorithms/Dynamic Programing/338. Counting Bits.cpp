/***from dust i have come, dust i will be***/

class Solution {
public:
    vector<int> dp;
    void solve(int curr, int cnt, int n)
    {
        if(curr > n) return;
        if(dp[curr] != -1) return;
        
        dp[curr] = cnt;
        
        solve(curr << 1 | 1, cnt + 1, n);
        solve(curr << 1, cnt, n);
    }
    
    vector<int> countBits(int num) {
        dp.resize(num + 1);
        fill(dp.begin(), dp.end(), -1);
        
        solve(0, 0, num);
        return dp;
    }
};
