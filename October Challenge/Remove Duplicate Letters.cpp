class Solution {
public:
    string removeDuplicateLetters(string s) {
        string ans = "";
        
        int cnt[26];
        memset(cnt, 0, sizeof(cnt));
        bool used[26];
        memset(used, false, sizeof(used));
        int n = s.length();
        
        for(int i = 0; i < n; i++)
            cnt[s[i] - 'a']++;
        
        for(int i = 0; i < n; i++){
            cnt[s[i] - 'a']--;
            if(used[s[i] - 'a']) continue;
            
            while(ans.length() && ans.back() > s[i] && cnt[ans.back() - 'a'])
                used[ans.back() - 'a'] = false, ans.pop_back();
            
            ans.push_back(s[i]);
            used[s[i] - 'a'] = true;
        }
        
        return ans;
    }
};
