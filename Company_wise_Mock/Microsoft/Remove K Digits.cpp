class Solution {
public:
    string removeKdigits(string num, int k) {
        stack<char> stk;
        int n = num.length();
        
        for(int i = 0; i < n; i++)
        {
            if(stk.empty())
                stk.push(num[i]);
            
            else {
                while(k > 0 && !stk.empty() && stk.top() > num[i]){
                    stk.pop();
                    k--;
                }
                
                stk.push(num[i]);
            }
        }
        
        // maybe the string is sorted, r.g. 123456789. in that case delete the last k
        while(k > 0 && !stk.empty()){
            stk.pop();
            k--;
        }
        
        string ans = "";
        while(stk.size()){
            ans.push_back(stk.top());
            stk.pop();
        }
        
        while(ans.length() > 0 && ans.back() == '0') ans.pop_back();
        reverse(ans.begin(), ans.end());
        
        if(ans.length() == 0) return "0";
        return ans;
    }
};
