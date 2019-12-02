/***from dust i have come, dust i will be***/

#include<bits/stdc++.h>

#define dbg printf("in\n")
#define nl printf("\n")
#define N 20
#define inf 1e9

#define pb push_back
#define pp pair<int, int>

using namespace std;

class DisjointSetUnion
{
	int n;
	int *p, *r;
public:
	DisjointSetUnion(int n)
	{
		this->n = n;
		p = new int[n + 1];
		r = new int[n + 1];

		for (int i = 0; i <= n; i++)
			r[i] = 1, p[i] = i;
	}

	void Union(int a,int b)
	{
		int x = Find(a);
		int y = Find(b);

		if (r[x] > r[y])
		{
			p[y] = x;
			r[x] += r[y];
		}

		else
		{
			p[x] = y;
			r[y] += r[x];
		}
	}

	int Find(int x)
	{
		if (p[x] == x)
			return x;

		return p[x] = Find(p[x]);
	}
};

class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        int n, i;
        int u, v;
        
        n = edges.size();
        DisjointSetUnion dsu(1010);
        
        vector<int> ans;
        for(i = 0; i < n; i++)
        {
            u = edges[i][0];
            v = edges[i][1];
            
            if(dsu.Find(u) == dsu.Find(v)){
                ans.clear();
                
                if(u > v) swap(u, v);
                ans.pb(u);
                ans.pb(v);
            }
            
            else dsu.Union(u, v);
        }
        
        return ans;
    }
};
