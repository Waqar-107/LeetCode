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
    
    bool similar(string a, string b)
    {
        int n = a.length(), i;
        int si = -1, sj = -1;
        for(i = 0; i < n; i++)
        {
            if(a[i] != b[i])
            {
                if(si == -1) si = i;
                else if(sj == -1){
                    sj = i;
                    break;
                }
            }
        }
        
        if(si != -1 && sj != -1)
            swap(b[si], b[sj]);
        
        return a == b;
    }
    
    int numSimilarGroups(vector<string>& A) {
        int n = A.size();
        DisjointSetUnion dsu(n);
        
        for(int i = 0; i < n; i++)
        {
            for(int j = i + 1; j < n; j++)
            {
                if(similar(A[i], A[j]))
                {
                    //cout<<A[i]<<" "<<A[j]<<endl;
                    if(dsu.Find(i + 1) != dsu.Find(j + 1)) 
                        dsu.Union(i + 1, j + 1);
                }
            }
        }
        
        vector<int> parent;
        for(int i = 1; i <= n; i++)
            parent.push_back(dsu.Find(i));
       
        sort(parent.begin(), parent.end());
        int ret =  unique(parent.begin(), parent.end()) - parent.begin();
        return ret;
    }
};
