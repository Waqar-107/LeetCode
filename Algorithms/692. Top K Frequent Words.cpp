/***from dust i have come, dust i will be***/

#include<bits/stdc++.h>

#define dbg printf("in\n")
#define nl printf("\n")
#define N 20
#define inf 1e9

#define pb push_back
#define pp pair<int, string>

using namespace std;

class cmp
{
public:
    bool operator() (pp a, pp b)
    {
        if(a.first == b.first)
            return a.second > b.second;
        
        return a.first < b.first;
    }
};

/*bool cmp(pp a, pp b)
{
    if(a.first == b.first)
        return a.second < b.second;
    return a.first > b.first;
}*/

class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        unordered_map<string, int> mp;

        int i, n = words.size();
        for(i = 0; i < n; i++)
            mp[words[i]]++;

        priority_queue<pp, vector<pp>, cmp> pq;

        auto itr = mp.begin();
        while(itr != mp.end())
        {
            //cout<<itr->first<<" "<<itr->second;nl;
            pq.push({itr->second, itr->first}), itr++;
        }

        vector<string> ans;
        while(k > 0 && pq.size())
        {
            ans.pb(pq.top().second);
            pq.pop();

            k--;
        }

        return ans;
    }
};
