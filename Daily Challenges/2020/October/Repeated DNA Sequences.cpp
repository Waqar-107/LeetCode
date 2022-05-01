class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        map<string, int> cnt;
        string str = "";
        vector<string> ans;
        int n = s.length();
            
        if(n < 10) return ans;
        for(int i = 0; i < 10; i++)
            str.push_back(s[i]);
        
        cnt[str]++;
        for(int i = 10; i < n; i++)
        {
            str.erase(0, 1);
            str.push_back(s[i]);
            cnt[str]++;
        }
        
        auto itr = cnt.begin();
        while(itr != cnt.end())
        {
            if(itr->second > 1)
                ans.push_back(itr->first);
            itr++;
        }
        
        return ans;
    }
};
