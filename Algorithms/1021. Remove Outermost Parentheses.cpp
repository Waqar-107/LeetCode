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
    string removeOuterParentheses(string S) {
        stack<int> ss;
        string s;
        for(int i = 0; i < S.length(); i++)
        {
            if(S[i] == '(')
                ss.push(i);
            else
            {
                if(ss.size() == 1)
                {
                    for(int j = ss.top() + 1; j < i; j++)
                        s.pb(S[j]);
                }
                
                ss.pop();
            }
        }
        
        return s;
    }
};
