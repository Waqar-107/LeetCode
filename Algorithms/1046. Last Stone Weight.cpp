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
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int> pq;
        for(int e : stones)
            pq.push(e);
        
        while(pq.size() > 1)
        {
            int x = pq.top(); pq.pop();
            int y = pq.top(); pq.pop();
            
            int m = min(x, y);
            
            x -= m;
            y -= m;
            
            if(x) pq.push(x);
            if(y) pq.push(y);
        }
        
        if(pq.size())
            return pq.top();
        return 0;
    }
};
