#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        
        int n = numbers.size();
        vector<int> ans;
        
        for(int i = 0; i < n; i++)
        {
            int k = lower_bound(numbers.begin(), numbers.end(), target - numbers[i]) - numbers.begin();
            
            if(k != i && k < n && numbers[k] == target - numbers[i])
            {
                ans.push_back(i + 1);
                ans.push_back(k + 1);
                break;
            }
        }
        
        if(ans[0] > ans[1]) swap(ans[0], ans[1]);
        return ans;
    }
};
