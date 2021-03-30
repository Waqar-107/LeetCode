bool cmp(vector<int> a, vector<int> b) {
    if(a[0] == b[0]) return a[1] > b[1];
    return a[0] > b[0];
}

class Solution {
public:
    int maxEnvelopes(vector<vector<int>>& envelopes) {
        int n = envelopes.size();
        
        int dp[n];
        fill(dp, dp + n, 1);
        
        sort(envelopes.begin(), envelopes.end(), cmp);
        
        for(int i = 1; i < n; i++) {
            for(int j = 0; j < i; j++){
                if(envelopes[i][0] < envelopes[j][0] && envelopes[i][1] < envelopes[j][1])
                    dp[i] = max(dp[i], 1 + dp[j]);
            }
        }
        
        int ans = 0;
        for(int i = 0; i < n; i++)
            ans = max(ans, dp[i]);
        
        return ans;
    }
};
