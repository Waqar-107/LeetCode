class Solution {
public:
    string solve(string s)
    {
        string finalS = "";
        for(int i = 0; i < s.length(); i++) {
            if(s[i] == '#') {
                if(finalS.length()) {
                    finalS.pop_back();
                }
            } else {
                finalS.push_back(s[i]);
            }
        }
        
        return finalS;
    }
    
    bool backspaceCompare(string s, string t) {
        return solve(s) == solve(t);
    }
};
