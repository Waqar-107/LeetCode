/***from dust i have come, dust i will be***/

#include<bits/stdc++.h>

#define dbg printf("in\n")
#define nl printf("\n")
#define N 20
#define inf 1e9

#define pb push_back
#define pp pair<int, int>

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int cnt[300] = {};
        int i = 0, j = 1;
        int mx = 1, n = s.length();
        bool flag;
        
        if(n == 0) return 0;
        
        cnt[s[i]]++;
        while(j < n)
        {
            cnt[s[j]]++;
            
            if(cnt[s[j]] < 2)
                mx = max(mx, j - i + 1), j++;
            else{
                //cout<<i<<" "<<j<<" "<<cnt[s[j]-'a'];nl;
                while(i < j && cnt[s[j]] >= 2){
                    cnt[s[i]]--;
                    i++;
                }
                
                j++;
            }
        }
        
        return mx;
    }
};
