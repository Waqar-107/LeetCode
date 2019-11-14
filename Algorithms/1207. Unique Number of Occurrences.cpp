/***from dust i have come, dust i will be***/

class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        int cnt[2010] = {};
        for(int i = 0; i < arr.size(); i++)
        {
            arr[i] += 1000;
            cnt[arr[i]]++;
        }
        
        bool occur[2010];
        memset(occur, 0, sizeof(occur));
        
        for(int i = 0; i < 2010; i++)
        {
            if(cnt[i])
            {
                if(occur[cnt[i]]) return false;
                occur[cnt[i]] = true;
            }
        }
        
        return true;
    }
};
