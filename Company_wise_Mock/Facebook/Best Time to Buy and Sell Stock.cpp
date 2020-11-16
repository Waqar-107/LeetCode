class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        if(n == 0) return 0;
            
        int mx[n];
        
        mx[n - 1] = 0;
        for(int i = n - 2; i >= 0; i--) {
            mx[i] = max(mx[i + 1], prices[i + 1]);
        }
        
        int ans = 0;
        for(int i = 0; i < n; i++) {
            ans = max(ans, max(0, mx[i] - prices[i]));
        }
        
        return ans;
    }
};
