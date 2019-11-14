/***from dust i have come, dust i will be***/

#include<bits/stdc++.h>

#define dbg printf("in\n")
#define nl printf("\n")
#define N 20
#define inf 1e9

#define pb push_back
#define pp pair<int, char>

using namespace std;

class Solution {
public:
    string reorganizeString(string s) {
        int cnt[26] = {};
        
        int i, j, n = s.length();
        for(i = 0; i < n; i++)
            cnt[s[i] - 'a']++;
        
        priority_queue<pp> pq;
        for(i = 0; i < 26; i++)
        {
            if(cnt[i])
                pq.push({cnt[i], i + 'a'});
        }
        
        string ret;
        while(pq.size())
        {
            pp x = pq.top(); pq.pop();
            if(pq.empty())
            {
                while(x.first--)
                    ret.pb(x.second);
                break;
            }
            pp y = pq.top(); pq.pop();
            
            int m = min(x.first, y.first);
            for(i = 0; i < m; i++)
                ret.pb(x.second), ret.pb(y.second);
            
            
            x.first -= m;
            y.first -= m;
            
            if(x.first > 0) pq.push(x);
            if(y.first > 0) pq.push(y);
        }
        
        n = s.length();
        for(i = 0; i < n; i++)
        {
            if(i + 1 < n)
            {
                if(ret[i] == ret[i + 1]) return "";
            }
        }
        
        return ret;
        
    }
};
