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
    bool isValid(string s) {
        stack<char> ch;
        map<char, char> mp;
        mp['('] = ')', mp['{'] = '}', mp['['] = ']';
        
        for(int i = 0; i < s.length(); i++)
        {
            if(s[i] == '(' || s[i] == '{' || s[i] == '[')
                ch.push(s[i]);
            else
            {
                if(ch.empty()) return false;
                else if(mp[ch.top()] != s[i]) return false;
                else ch.pop();
            }
        }
        
        if(ch.empty())
            return true;
        
        return false;
    }
};
