class Solution {
public:
    vector<string> findAndReplacePattern(vector<string>& words, string pattern) {
        vector<string> ans;
        map<char, char> mp;
        map<char, char> used;
        bool f = true;
        
        for(int i = 0; i < words.size(); i++){
            f = true;
            mp.clear();
            used.clear();
            
            if(pattern.length() != words[i].length()) continue;
            
            for(int j = 0; j < words[i].length(); j++){
                if(!mp[words[i][j]]) {
                    if(!used[pattern[j]])
                        mp[words[i][j]] = pattern[j], used[pattern[j]] = words[i][j];
                    else{
                        f = false;
                        break;
                    }
                }
                
                else if(mp[words[i][j]] == pattern[j]) continue;
                
                else {
                    f = false;
                    break;
                }
            }
            
            if(f) ans.push_back(words[i]);
        }
        
        return ans;
    }
};
