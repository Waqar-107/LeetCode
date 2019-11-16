/***from dust i have come, dust i will be***/

#include<bits/stdc++.h>

#define dbg printf("in\n")
#define nl printf("\n")
#define N 20
#define inf 1e9

#define pb push_back
#define pp pair<int, int>

using namespace std;

class NumArray {
public:
    vector<int> segTree;
    vector<int> a;
    
    NumArray(vector<int>& nums) {
        a.resize(nums.size());
        segTree.resize(a.size() * 4);
        
        for(int i = 0; i < nums.size(); i++)
            a[i] = nums[i];
        
        // who the fuck gives an empty array :3
        if(a.size())
            Build(1, 1, a.size());
    }
    
    void Build(int at, int L, int R)
    {
        if(L == R)
        {
            segTree[at] = a[L - 1];
            return;
        }
        
        int mid = (L + R) / 2;
        
        Build(at * 2, L, mid);
        Build(at * 2 + 1, mid + 1, R);
        
        segTree[at] = segTree[at * 2] + segTree[at * 2 + 1];
    }
    
    void Update(int at, int L, int R, int idx, int val)
    {
        // out of range
        if(idx < L || idx > R) return;

        // completely in range
        if(L <= idx && idx <= R)
            segTree[at] += val;
        
        if(L == R) return;
        
        int mid = (L + R) / 2;
        
        Update(at * 2, L, mid, idx, val);
        Update(at * 2 + 1, mid + 1, R, idx, val);
    }
    
    void update(int i, int val) {
        if(a.size() == 0){
            return;    
        }
        
        int x = val - a[i];
        Update(1, 1, a.size(), i + 1, x);
        
        a[i] = val;
    }
    
    int Query(int at, int L, int R, int l, int r)
    {
        // out of range
        if(r < L || R < l)return 0;

        // completely in range
        if(l <= L && R <= r)
            return segTree[at];

        int mid = (L + R) / 2;
        int x = Query(at * 2, L, mid, l, r);
        int y = Query(at * 2 + 1, mid + 1, R, l, r);
        
        return x + y;
    }
    
    int sumRange(int i, int j) {
        if(a.size())
            return Query(1, 1, a.size(), i + 1, j + 1);
        else
            return 0;
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * obj->update(i,val);
 * int param_2 = obj->sumRange(i,j);
 */
