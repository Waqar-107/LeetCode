class Solution {
public:
    string removeDuplicates(string s, int k) {
        stack<pair<char, int>> stk;
        int len = s.length();
        
        for(int i = 0; i < len; i++) {
            if(!stk.empty() && stk.top().first == s[i]) {
                stk.push({ s[i], stk.top().second + 1 });
            } else {
                stk.push({ s[i], 1 });
            }
            
            if(stk.top().second == k) {
                for(int j = 0; j < k; j++) {
                    stk.pop();
                }
            }
        }
        
        string ans = "";
        while(!stk.empty()) {
            ans.push_back(stk.top().first);
            stk.pop();
        }
        
        reverse(ans.begin(), ans.end());
        return ans;
    }
};
