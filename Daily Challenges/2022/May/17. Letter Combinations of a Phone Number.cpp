class Solution {
public:
    vector<string> answer;
    map<char, string> mp;
    
    void solve(string digits, int idx, string current)
    {
        if(idx == digits.length()) {
            if(current.length()) {
                answer.push_back(current);
            }
            
            return;
        }
        
        for(int i = 0; i < mp[digits[idx]].length(); i++) {
            current.push_back(mp[digits[idx]][i]);
            solve(digits, idx + 1, current);
            current.pop_back();
        }
    }
    
    vector<string> letterCombinations(string digits) {
        mp['2'] = "abc";
        mp['3'] = "def";
        mp['4'] = "ghi";
        mp['5'] = "jkl";
        mp['6'] = "mno";
        mp['7'] = "pqrs";
        mp['8'] = "tuv";
        mp['9'] = "wxyz";
        
        solve(digits, 0, "");
        return answer;
    }
};
