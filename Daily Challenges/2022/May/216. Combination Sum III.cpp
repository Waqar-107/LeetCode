class Solution {
public:
    vector<vector<int>> results;
    vector<int> current;
    
    void solve(int k, int n, int currentSum, int currentDigit)
    {
        if(current.size() == k && currentSum == n)
        {
            results.push_back(current);
            return;
        }
        
        if(currentDigit > 9) return;
        
        // will use currentDigit
        if(currentSum + currentDigit <= n)
        {
            current.push_back(currentDigit);
            solve(k, n, currentSum + currentDigit, currentDigit + 1);
            current.pop_back();
        }
        
        // won't use currentDigit
        solve(k, n, currentSum, currentDigit + 1);
    }
    
    vector<vector<int>> combinationSum3(int k, int n) {
        solve(k, n, 0, 1);
        
        return results;
    }
};
