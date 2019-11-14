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
    map<char, int> mp;
    string frequencySort(string s) {
        int i, n = s.length();
        for(i = 0; i < n; i++)
            mp[s[i]]++;
        
        vector<pp> vec;
        for(auto itr = mp.begin(); itr != mp.end(); itr++)
            vec.pb({itr->second, itr->first});
        
        sort(vec.begin(), vec.end(), greater<>());
        string ans;
        
        for(pp e : vec){
            while(e.first--)
                ans.pb(e.second);
        }
        
        return ans;
    }
};
