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
    string removeDuplicates(string S) {
        string ret = "";
        int n = S.length();
        stack<char> ss;
        
        for(int i = 0; i < n; i++)
        {
            if(ss.empty()) ss.push(S[i]);
            else
            {
                if(ss.top() == S[i])
                    ss.pop();
                else
                    ss.push(S[i]);
            }
        }
        
        while(ss.size())
            ret.pb(ss.top()), ss.pop();
        
        reverse(ret.begin(), ret.end());
        
        return ret;
    }
};
