class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        
        if(!n) return 0;
        
        int mx[n];
        
        mx[n - 1] = prices[n - 1];
        for(int i = n - 2; i >= 0; i--){
            mx[i] = max(mx[i + 1], prices[i]);
        }
        
        int ans = 0;
        for(int i = 0; i < n - 1; i++){
            ans = max(ans, mx[i + 1] - prices[i]);
        }
        
        return ans;
    }
};
